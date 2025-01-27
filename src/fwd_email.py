import os
import logging
import imaplib
import smtplib
import email
import pandas as pd
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr
from email import encoders

load_dotenv("config.env")

# Configuração de logs
LOG_FILE = "email_processing.log"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", handlers=[
    logging.FileHandler(LOG_FILE), logging.StreamHandler()
])
logger = logging.getLogger(__name__)

# Configurações do servidor de email
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_PORT = int(os.getenv("IMAP_PORT", 993))
EMAIL = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def forward_email(mail, e_id, to_emails, subject, body):
    """
    Encaminha o email identificado pelo ID e_id para os destinatários fornecidos. (Forward identified email to provided recipients.)

    Args:
        mail (imaplib.IMAP4_SSL): Conexão IMAP com o servidor de emails.
        e_id (bytes): ID do email a ser encaminhado.
        to_emails (list): Lista de destinatários.
        subject (str): Assunto do email original.
        body (str): Corpo do email original.
    """
    try:
        # Processar e criar uma mensagem de encaminhamento (Process and create a forward message)
        forward_msg = MIMEMultipart()
        forward_msg['From'] = SMTP_USERNAME
        forward_msg['To'] = ", ".join(to_emails)
        forward_msg['Subject'] = f"FW: {subject}"

        # Adicionar o corpo ao email (Add the body to the email)
        body_part = MIMEText(body, 'plain')
        forward_msg.attach(body_part)

        # Conectar e enviar via SMTP (Connect and send via SMTP)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, to_emails, forward_msg.as_string())
            logging.info(f"Email {e_id.decode()} encaminhado para: {', '.join(to_emails)}") # (Email forwarded to: )

    except Exception as e:
        logging.error(f"Erro ao encaminhar email ID {e_id}: {e}") # (Error forwarding email ID: )

def decode_email_body(msg):
    """
    Decodifica o corpo do email fornecido. (Decode the provided email body.)

    Args:
        msg (email.message.Message): Mensagem de email. (Email message)

    Returns:
        str: Corpo do email como texto plano. (Email body as plain text.)
    """
    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode("utf-8", errors="ignore")
        return msg.get_payload(decode=True).decode("utf-8", errors="ignore")
    except Exception as e:
        logging.error(f"Erro ao decodificar corpo do email: {e}")
        return ""

def main():
    """
    Processa emails na caixa de entrada, aplicando regras específicas de encaminhamento. (Process emails in the inbox, applying specific forwarding rules.)
    """
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()

        for e_id in email_ids:
            _, data = mail.fetch(e_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg.get("Subject", "(Sem Assunto)")
            body = decode_email_body(msg)

            logging.info(f"Processando email ID {e_id.decode()}: Assunto - {subject}") # (Processing email ID: Subject - ")

            forward_email(mail, e_id, ["exemplo@destinatario.com"], subject, body)

        mail.logout()
    except Exception as e:
        logging.error(f"Erro ao processar emails: {e}") # (Error processing emails: )

if __name__ == "__main__":
    main()
