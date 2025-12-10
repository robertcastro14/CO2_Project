# 🌳 CO2_PROJECT: Calculadora de Emissões de Carbono

Este projeto consiste em um website desenvolvido para calcular a quantidade de dióxido de carbono ($\text{CO}_2$) emitida por diferentes trajetos de transporte, visando a conscientização e o incentivo a escolhas de mobilidade mais sustentáveis.

---

## 👥 Componentes do Grupo

* Eric Bittencourt Grillo
* Guto Tardin
* Thiago Duarte
* Robert Castro

---

## 📝 Descrição e Objetivo

O site é uma ferramenta interativa que permite ao usuário estimar o impacto ambiental de seus deslocamentos.

**Funcionalidade:**
1.  O usuário informa o **tipo de veículo**, a **distância percorrida** e a **frequência da viagem**.
2.  O sistema retorna uma estimativa das **emissões de carbono** correspondentes.
3.  O site sugere a **melhor opção de transporte** para o trajeto informado, incentivando escolhas mais sustentáveis no dia a dia.

**Objetivo:** Conscientizar sobre o impacto ambiental dos deslocamentos e promover a redução da pegada de carbono individual.

---

## 🚀 Como Usar o Site (Guia de Instalação)

Siga os passos abaixo para clonar, configurar e rodar o projeto em seu ambiente local.

### 1. Preparação

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/robertcastro14/CO2_PROJECT.git](https://github.com/robertcastro14/CO2_PROJECT.git)
    ```
2.  **Entre na pasta do projeto:**
    ```bash
    cd CO2_PROJECT
    ```
3.  **Ative o Ambiente Virtual (`venv`):**
    * **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
4.  **Instale as Dependências (Django e outras):**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Configuração Rápida (Banco de Dados e Admin)

Depois de ativar o `venv` e instalar as dependências, configure o banco de dados:

1.  **Crie e Aplique as Migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2.  **Crie um Superusuário (Opcional - para área administrativa):**
    ```bash
    python manage.py createsuperuser
    ```

### 3. Execução

1.  **Rode o Servidor Django:**
    ```bash
    python manage.py runserver
    ```
2.  **Acesse o Site no Navegador:**
    ```
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    ```

**Observações de Acesso:**
* **Calculadora:** Use a interface principal para calcular as emissões de $\text{CO}_2$.
* **Administração:** Acesse a área de gestão de dados em `http://127.0.0.1:8000/admin/`.
* **Autenticação:** As rotas padrão de login/logout estão em `/accounts/` (ex: `/accounts/login/`).

---

## 📸 Imagens do Projeto

| Tela | Visualização |
| :--- | :--- |
| **Página Inicial** | ![Página inicial](img/home.png) |
| **Página Cálculo** | ![Página cálculo](img/calculadora.png) |