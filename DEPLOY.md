# 🚀 Guia de Deploy - Countdown Vilela

## Opções Gratuitas para Deploy

### 1. **Render** (Recomendado)

#### Passos:
1. **Criar conta** em [render.com](https://render.com)
2. **Conectar GitHub** (fazer push do código)
3. **Criar novo Web Service**
4. **Configurar:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python Version:** 3.9

#### Vantagens:
- ✅ Totalmente gratuito
- ✅ Deploy automático
- ✅ Domínio personalizado
- ✅ SSL gratuito

---

### 2. **Railway**

#### Passos:
1. **Criar conta** em [railway.app](https://railway.app)
2. **Conectar GitHub**
3. **Deploy automático**

#### Vantagens:
- ✅ Interface muito simples
- ✅ Deploy rápido
- ✅ Plano gratuito generoso

---

### 3. **Heroku** (Alternativa)

#### Passos:
1. **Criar conta** em [heroku.com](https://heroku.com)
2. **Instalar Heroku CLI**
3. **Comandos:**
   ```bash
   heroku create countdown-vilela
   git push heroku main
   ```

---

## 📁 Arquivos Necessários

O projeto já inclui todos os arquivos necessários:
- ✅ `requirements.txt` - Dependências
- ✅ `Procfile` - Comando de execução
- ✅ `runtime.txt` - Versão Python
- ✅ `app.py` - Aplicação Flask

## 🔧 Configuração Local

Para testar localmente antes do deploy:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar localmente
python app.py

# Ou com gunicorn (produção)
gunicorn app:app
```

## 🌐 URLs Finais

Após o deploy, terás URLs como:
- **Render:** `https://countdown-vilela.onrender.com`
- **Railway:** `https://countdown-vilela.railway.app`
- **Heroku:** `https://countdown-vilela.herokuapp.com`

## 📱 Funcionalidades

O site inclui:
- ⏰ Countdown de 30 dias
- 📊 Barra de progresso
- 🎨 Design responsivo
- 📱 Compatível mobile
- �� Animações suaves 