# Countdown Web App

Uma aplicação web moderna com um countdown de 30 dias, construída com Flask e design responsivo.

## Funcionalidades

- ⏰ Countdown em tempo real (dias, horas, minutos, segundos)
- 📊 Barra de progresso visual
- 🎨 Design moderno e responsivo
- 📱 Compatível com dispositivos móveis
- 🌈 Gradientes e animações suaves

## Setup

1. Criar e ativar o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Executar a aplicação:
   ```bash
   python app.py
   ```

4. Abrir no navegador:
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
Project1/
├── app.py              # Aplicação Flask principal
├── templates/
│   └── index.html      # Template HTML da página
├── static/
│   └── css/
│       └── style.css   # Estilos CSS
├── requirements.txt    # Dependências Python
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação
```

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: CSS Grid, Flexbox, Gradientes
- **Fontes**: Google Fonts (Inter)
- **Responsividade**: Media Queries

## Personalização

Para alterar o período do countdown, edite a linha 8 no arquivo `app.py`:
```python
target_date = datetime.now() + timedelta(days=30)  # Altere o número 30
```