import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    try:
        # Configurações do servidor SMTP
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
        smtp_username = 'sanjavalley@outlook.com'
        smtp_password = 'isaAlexiaGui23'

        # Criando objeto da mensagem
        data = request.json
        destinatarios = data['destinatarios']
        msg = MIMEMultipart()
        msg['From'] = smtp_username

        msg['Subject'] = 'Alerta'

        # Corpo da mensagem
        body = 'Seus dados podem estar em perigo. Recomendamos que altere sua senha.'

        # Conectando-se ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Enviando o e-mail para cada destinatário separadamente
        for destinatario in destinatarios:
            # Criando um novo objeto de mensagem para cada destinatário
            individual_msg = MIMEMultipart()
            individual_msg['From'] = smtp_username
            individual_msg['To'] = destinatario
            individual_msg['Subject'] = msg['Subject']

            # Copiando o corpo da mensagem para o objeto individual
            individual_msg.attach(MIMEText(body, 'plain'))

            # Enviando o e-mail para o destinatário atual
            server.send_message(individual_msg)

        server.quit()
        return "E-mail enviado com sucesso"
    except:
        traceback.print_exc()
        return "Erro ao enviar e-mail"
