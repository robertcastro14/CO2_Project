from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroCalculo, Notificacao

# View da Página Inicial (Home)
@login_required

# View da Página Inicial (Home)
def home(request):
    # Busca a notificação mais recente e não lida para o usuário logado
    notificacao_recente = Notificacao.objects.filter(
        usuario=request.user, 
        lida=False
    ).order_by('-data_envio').first()

    context = {
        'notificacao': notificacao_recente
    }
    return render(request, 'usuario/home.html', context)

# View da Calculadora (Lógica de Cálculo)
@login_required
def calculadora(request):
    resultado = None

    if request.method == 'POST':
        try:
            # Pega os dados do formulário
            distancia = float(request.POST.get('distancia'))
            transporte = request.POST.get('transporte')

            # Fatores de emissão
            fatores = {
                'carro': 192,
                'onibus': 68,
                'metro': 35,
                'moto': 87,
                'bicicleta': 0,
                'caminhada': 0
            }

            if transporte in fatores:
                # Calcula a emissão total em gramas
                emissao_g = distancia * fatores[transporte]
                
                # Converte para Kg (divide por 1000) e arredonda
                emissao_kg = round(emissao_g / 1000, 2)
                
                # Cálculo estimativo de árvores
                arvores = round(emissao_kg / 15, 4) if emissao_kg > 0 else 0
                
                # --- NOVO BLOCO: SALVAR NO HISTÓRICO ---
                if request.user.is_authenticated:
                    RegistroCalculo.objects.create(
                        usuario=request.user,
                        distancia=distancia,
                        transporte=transporte, # Salva o nome do transporte (ex: 'carro', 'moto')
                        co2_emitido=emissao_kg,
                        arvores=arvores
                    )
                # ---------------------------------------

                resultado = {
                    'distancia': distancia,
                    'transporte': transporte.capitalize(),
                    'emissao_kg': emissao_kg,
                    'arvores': arvores
                }
            else:
                resultado = {'erro': 'Meio de transporte inválido.'}

        except ValueError:
            resultado = {'erro': 'Por favor, insira uma distância válida.'}

    return render(request, 'usuario/calculadora.html', {'resultado': resultado})

def historico(request):
    # Filtra todos os cálculos feitos APENAS pelo usuário logado, 
    # ordenando do mais recente para o mais antigo (o sinal de '-' em 'data_calculo')
    registros = RegistroCalculo.objects.filter(usuario=request.user).order_by('-data_calculo')

    # Calcula o total de CO2 emitido e o total de árvores necessárias
    total_co2 = sum(r.co2_emitido for r in registros)
    total_arvores = sum(r.arvores for r in registros)
    
    context = {
        'registros': registros,
        'total_co2': round(total_co2, 2),
        'total_arvores': round(total_arvores) # Arredondamos árvores para não ter 0.5 árvores
    }
    
    return render(request, 'usuario/historico.html', context)

def marcar_notificacao_lida(request, notificacao_id):
    try:
        # Busca a notificação que pertence ao usuário logado
        notificacao = Notificacao.objects.get(id=notificacao_id, usuario=request.user)
        notificacao.lida = True
        notificacao.save()
    except Notificacao.DoesNotExist:
        pass 
        
    # Redireciona de volta para a home
    return redirect('home')