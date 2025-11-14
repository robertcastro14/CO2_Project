# CO2_PROJECT

## Componentes do grupo
- Eric Bittencourt Grillo
- Guto Tardin
- Thiago Duarte
- Robert Castro

## Descrição do tema
Este site foi desenvolvido para calcular a quantidade de CO₂ emitida por diferentes trajetos de transporte. O usuário informa o tipo de veículo, a distância percorrida e a frequência da viagem, e o site retorna uma estimativa das emissões de carbono correspondentes. Além disso, o site sugere a melhor opção de transporte para o determinado trajeto informado. O objetivo é conscientizar sobre o impacto ambiental dos deslocamentos e incentivar escolhas mais sustentáveis no dia a dia.

## Como usar o site
. **Clone este repositório:**
```bash
git clone <https://github.com/robertcastro14/CO2_PROJECT.git>
Entre na pasta do projeto:
cd CO2_PROJECT
Ative o ambiente virtual:
source venv/bin/activate
No Windows, use:
venv\Scripts\activate
Instale as dependências:
pip install -r requirements.txt
Rode o servidor Django:
python manage.py runserver
Abra o navegador e acesse:
http://127.0.0.1:8000/
Use o site para calcular as emissões de CO₂, informando:
Tipo de veículo
Distância do trajeto
Frequência da viagem
O site vai mostrar a quantidade estimada de CO₂ emitida para o trajeto informado. 

## Configuração rápida (autenticação e banco)

Depois de ativar o `venv` e instalar dependências, crie as migrações e atualize o banco:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie um superusuário para acessar a área administrativa:

```bash
python manage.py createsuperuser
```

Acesse a administração em `http://127.0.0.1:8000/admin/` para adicionar dados (contatos) manualmente.

As rotas de autenticação do Django estão habilitadas em `/accounts/` — por exemplo, o login fica em `/accounts/login/`.

### Imagens
![Página inicial](img/home.png) 
![Página cálculo](img/calculadora.png)

