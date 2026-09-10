#antes de compilar e rodar o código, rodar no terminal os dois comandos:
#python3 -m venv .venv
#source .venv/bin/activate

#Para reutilizar o código:

# 1- entrar em resend.com
# 2- logar
# 3- gerar nova API
# 4- trocar a  API do código pela nova

import secrets
import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")

usuarios = {}
tokens_ativos = {}

def gerar_Token(usuario):
    token = secrets.token_hex(16)
    tokens_ativos [token] = usuario
    return token

def cadastrar_usuario(usuario, senha, email):
    if usuario in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[usuario] = {'senha': senha, 'email': email}

def fazer_login(usuario, senha):
    if usuario in usuarios:
        if senha == usuarios[usuario]['senha']:
            token = gerar_Token(usuario)
            email = usuarios[usuario]['email']
            enviar_email(email, token)
            return token
        else:
            print("Erro!")
    else:
        print("Erro!")

def enviar_email(email, token):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "Seu Código de Acesso",
        "html": f"<p>Seu token de autenticação é: <strong>{token}</strong></p>"
    })

def validar_token(token):
    if token in tokens_ativos:
        return True
    else:
        return False

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
email = input("Digite seu email: ")
cadastrar_usuario(nome, senha, email)

usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")
x = fazer_login(usuario, senha)
validacao = input("Digite o token recebido por E-mail: ")
if validar_token(validacao):
    print("Acesso liberado!")
else:
    print("Token inválido")