from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import RegistroCalculo, Notificacao

# --- CONFIGURAÇÕES GLOBAIS ---
# Preço médio da gasolina travado (Dez/2025)
PRECO_GASOLINA_FIXO = 6.17

@login_required
def home(request):
    notificacao_recente = Notificacao.objects.filter(
        usuario=request.user, 
        lida=False
    ).order_by('-data_envio').first()

    context = {
        'notificacao': notificacao_recente
    }
    return render(request, 'usuario/home.html', context)

@login_required
def calculadora(request):
    resultado = None

    if request.method == 'POST':
        try:
            # 1. TRATAMENTO DE ERRO: Troca vírgula por ponto para evitar crash
            distancia_str = request.POST.get('distancia', '').replace(',', '.')
            distancia = float(distancia_str)
            
            transporte = request.POST.get('transporte')

            # Tratamento seguro para o Consumo (se vier vazio ou com vírgula)
            consumo_str = request.POST.get('consumo', '0').replace(',', '.')
            if not consumo_str: consumo_str = '0'
            consumo_medio = float(consumo_str)

            # Usa a constante definida no topo do arquivo
            preco_combustivel = PRECO_GASOLINA_FIXO

            fatores = {
                'carro': 192, 'onibus': 68, 'metro': 35, 
                'moto': 87, 'bicicleta': 0, 'caminhada': 0
            }

            if transporte in fatores:
                emissao_g = distancia * fatores[transporte]
                emissao_kg = round(emissao_g / 1000, 2)
                arvores = round(emissao_kg / 15, 4) if emissao_kg > 0 else 0
                
                # --- CÁLCULO DE CUSTO ---
                custo = 0.0
                if transporte in ['carro', 'moto'] and consumo_medio > 0:
                    litros_necessarios = distancia / consumo_medio
                    custo = round(litros_necessarios * preco_combustivel, 2)
                
                # --- SALVAR NO BANCO ---
                if request.user.is_authenticated:
                    RegistroCalculo.objects.create(
                        usuario=request.user,
                        distancia=distancia,
                        transporte=transporte,
                        co2_emitido=emissao_kg,
                        arvores=arvores,
                        custo_estimado=custo  # Importante: Salvando o novo campo
                    )

                resultado = {
                    'distancia': distancia,
                    'transporte': transporte.capitalize(),
                    'emissao_kg': emissao_kg,
                    'arvores': arvores,
                    'custo': custo,
                    'consumo': consumo_medio,
                    'preco': PRECO_GASOLINA_FIXO
                }
            else:
                resultado = {'erro': 'Meio de transporte inválido.'}

        except ValueError:
            resultado = {'erro': 'Por favor, insira apenas números válidos na distância e consumo.'}
    
    # Se for a primeira vez abrindo a página (GET), mostra o preço fixo no form
    if not resultado:
        resultado = {'preco': PRECO_GASOLINA_FIXO}

    return render(request, 'usuario/calculadora.html', {'resultado': resultado})

@login_required
def historico(request):
    termo_busca = request.GET.get('transporte')
    registros = RegistroCalculo.objects.filter(usuario=request.user)

    if termo_busca:
        registros = registros.filter(transporte__icontains=termo_busca)

    registros = registros.order_by('-data_calculo')

    total_co2 = sum(r.co2_emitido for r in registros)
    total_arvores = sum(r.arvores for r in registros)
    
    # Opcional: Somar também o custo total gasto
    # total_custo = sum(r.custo_estimado for r in registros)
    
    context = {
        'registros': registros,
        'total_co2': round(total_co2, 2),
        'total_arvores': round(total_arvores)
    }
    
    return render(request, 'usuario/historico.html', context)

@login_required
def ranking(request):
    users = User.objects.all()
    ranking_list = []
    
    # Fator: Carro emite ~0.192 kg/km
    FATOR_CARRO_KG = 0.192

    for user in users:
        calculos = RegistroCalculo.objects.filter(usuario=user)
        total_economizado = 0.0
        
        for calc in calculos:
            # 1. Quanto emitiria de carro?
            emissao_referencia = calc.distancia * FATOR_CARRO_KG
            # 2. Economia = Referência - Realidade
            economia = emissao_referencia - calc.co2_emitido
            total_economizado += economia
            
        ranking_list.append({
            'usuario': user,
            'nome': user.first_name if user.first_name else user.username,
            'cidade': 'Brasil',
            'total_economizado': round(total_economizado, 1)
        })

    ranking_list.sort(key=lambda x: x['total_economizado'], reverse=True)

    for i, item in enumerate(ranking_list):
        item['posicao'] = i + 1

    context = {'ranking': ranking_list}
    return render(request, 'usuario/ranking.html', context)

def marcar_notificacao_lida(request, notificacao_id):
    try:
        notificacao = Notificacao.objects.get(id=notificacao_id, usuario=request.user)
        notificacao.lida = True
        notificacao.save()
    except Notificacao.DoesNotExist:
        pass 
    return redirect('home')

def sobre(request):
    return render(request, 'usuario/sobre.html')

def contato(request):
    return render(request, 'usuario/contato.html')