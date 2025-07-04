# Countdown Vilela - Web App

Uma aplicação web moderna com um countdown de 30 dias, construída com Flask e design responsivo.

## 🌐 **Site Online**
**URL:** https://countdown-vilela.onrender.com/

## ✅ **Status do Projeto**
- **Desenvolvimento:** ✅ Concluído
- **Deploy:** ✅ Online e funcionando
- **Última atualização:** 4 de Julho de 2025

## 🎯 **Funcionalidades**

- ⏰ Countdown em tempo real (dias, horas, minutos, segundos)
- 📊 Barra de progresso visual
- 🎨 Design moderno e responsivo
- 📱 Compatível com dispositivos móveis
- 🌈 Gradientes e animações suaves
- 🔄 Atualização automática a cada segundo

## 🚀 **Setup Local**

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/JoaoPavlo/countdown-vilela.git
   cd countdown-vilela
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a aplicação:**
   ```bash
   python app.py
   ```

5. **Abrir no navegador:**
   ```
   http://localhost:3000
   ```

## 📁 **Estrutura do Projeto**

```
countdown-vilela/
├── app.py              # Aplicação Flask principal
├── templates/
│   └── index.html      # Template HTML da página
├── static/
│   └── css/
│       └── style.css   # Estilos CSS
├── requirements.txt    # Dependências Python
├── Procfile           # Configuração para deploy
├── runtime.txt        # Versão do Python
├── .gitignore         # Arquivos ignorados pelo Git
├── README.md          # Documentação principal
├── PROJECT_INFO.md    # Informações do projeto
└── DEPLOY.md          # Guia de deploy
```

## 🛠️ **Tecnologias Utilizadas**

- **Backend:** Flask (Python 3.11)
- **Frontend:** HTML5, CSS3, JavaScript
- **Design:** CSS Grid, Flexbox, Gradientes
- **Fontes:** Google Fonts (Inter)
- **Responsividade:** Media Queries
- **Deploy:** Render.com
- **Servidor:** Gunicorn

## ⚙️ **Personalização**

Para alterar o período do countdown, edite a linha 9 no arquivo `app.py`:
```python
target_date = datetime.now() + timedelta(days=30)  # Altere o número 30
```

## 🌐 **Deploy**

Este projeto está hospedado no Render.com com deploy automático do GitHub. Para mais informações sobre o processo de deploy, consulte o arquivo `DEPLOY.md`.

## 📞 **Contacto**

- **Desenvolvedor:** João Pavlo
- **GitHub:** [@JoaoPavlo](https://github.com/JoaoPavlo)
- **Repositório:** [countdown-vilela](https://github.com/JoaoPavlo/countdown-vilela)