import smtplib
import email.message
import os
import time
import sys
from datetime import datetime

def Enviar_email():
    # Função de enviar E-mails

    #global remetente
    
    os.system('cls' if os.name == 'nt' else 'clear' )

    corpo_email = """
    <p>Conteúdo</p>
    """
    timeNow()
    # variavel remetente caso queira digitar seu email no terminal
    #remetente = input("---Digite o e-mail que voce quer que vá ai: ").lower()
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = Emails()
    msg['To'] = '' #Email remetente ou a variavel remente com valor de entrada
    password = Senhas() #Função senha que retorna um valor de um Dicionário
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login]
    barraProgresso()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    print('---Email enviado.')

def barraProgresso():
    # Função de Incrementar uma barra de progresso

    def progress_bar(value, max, barsize):
        chars = int(value * barsize / float(max))
        percent = int((value / float(max)) * 100)
        sys.stdout.write("#" * chars)
        sys.stdout.write(" " * (barsize - chars + 2))
        if value >= max:
            sys.stdout.write("concluido. \n\n")
        else:
            sys.stdout.write("[%3i%%]\r" % (percent))
            sys.stdout.flush()
    
    print("---Escrevendo seu e-mail...")
    for i in range(11):
        progress_bar(i, 10, 40)
        time.sleep(0.20)

def timeNow():
    # Função de Informar a data e horas atuais

    DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]

    indice_da_semana = datetime.today().weekday()
    dia_da_semana = DIAS[indice_da_semana]
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

    print(f"\t\t\t\t\t\t {data_e_hora_em_texto}({dia_da_semana})\n")

def Emails():
    # Função de retornar um valor

    global email_enviar

    # Dicionario Emails, onde voce vai colocar suas senhas,
    # o login do E-mail automatico vai depender do retorno dele.
    EMAILS = {
        1:'',
        2:'',
        3:'',
        4:'',
        5:'',
        6:'',
        7:''
    }
    email_enviar = EMAILS[1][:]
    return email_enviar

def Senhas():
    # Função de retornar um valor

    global senha

    # Dicionario Senhas, onde voce vai colocar suas senhas,
    # o login do E-mail automatico vai depender do retorno dele.
    SENHAS = {
        1:'',
        2:'',
        3:'',
        4:'',
        5:'',
        6:'',
        7:''
    }
    senha = SENHAS[1][:]
    return senha

def main():

    # Função main, ela roda o programa
    Enviar_email()
main()