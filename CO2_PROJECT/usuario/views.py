from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View da Página Inicial (Home)
@login_required

# View da Página Inicial (Home)
def home(request):
    return render(request, 'usuario/home.html')

# View da Calculadora (Lógica de Cálculo)
def calculadora(request):
    resultado = None
    
    if request.method == 'POST':
        try:
            # Pega os dados enviados pelo formulário HTML
            distancia = float(request.POST.get('distancia'))
            transporte = request.POST.get('transporte')
            
            # Fatores de emissão (em g CO2/km)
            fatores = {
                'carro': 192,
                'onibus': 68,
                'metro': 35,
                'trem': 35,
                'moto': 103,
                'bicicleta': 0,
                'a_pe': 0
            }
            
            # Realiza o cálculo
            fator = fatores.get(transporte, 0)
            emissao_g = distancia * fator
            emissao_kg = emissao_g / 1000
            
            # Estimativa de árvores (1 árvore ~ 22kg CO2/ano)
            arvores = emissao_kg / 22 
            
            # Prepara os dados para enviar de volta para a tela
            resultado = {
                'emissao_kg': round(emissao_kg, 2),
                'arvores': round(arvores, 1),
                'distancia': distancia,
                'transporte': transporte.capitalize()
            }
            
        except (ValueError, TypeError):
            resultado = {'erro': 'Por favor, insira valores válidos.'}

    return render(request, 'usuario/calculadora.html', {'resultado': resultado})