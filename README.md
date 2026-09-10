# Sistema de Autenticação com Envio de Token (Resend API)

Projeto em Python que simula cadastro e login de usuários com autenticação via e-mail utilizando a API do **Resend**.

## 🚀 Funcionalidades

- **Cadastro de Usuário:** Registro de nome, senha e e-mail.
- **Autenticação:** Validação das credenciais do usuário.
- **Geração de Token:** Criação de tokens de segurança aleatórios com a biblioteca `secrets`.
- **Envio de E-mail:** Envio do token de verificação para o e-mail cadastrado usando o serviço Resend.
- **Validação de Token:** Confirmação do código digitado para liberação do acesso.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **[Resend SDK](https://resend.com)** (para envio de e-mails transacionais)
- **Secrets & OS** (módulos nativos do Python para geração de tokens e leitura de variáveis de ambiente)

## 📋 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/CaioVinicius365/sistema-autenticacao-python.git
cd sistema-autenticacao-python
```

### 2. Criar e ativar o ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Linux/Mac
# .venv\Scripts\activate  # No Windows
```

### 3. Instalar as dependências
```bash
pip install resend
```

### 4. Configurar a Chave de API do Resend
Para funcionar corretamente, obtenha uma chave de API no [Resend](https://resend.com) e defina a variável de ambiente:

**Linux / Mac:**
```bash
export RESEND_API_KEY="sua_chave_aqui"
```

**Windows (CMD):**
```cmd
set RESEND_API_KEY="sua_chave_aqui"
```

**Windows (PowerShell):**
```powershell
$env:RESEND_API_KEY="sua_chave_aqui"
```

### 5. Executar o código
```bash
python3 auth.py
```

---
Desenvolvido por [Caio Vinícius](https://github.com/CaioVinicius365) 🚀
