import os
import random
from dotenv import load_dotenv
from twilio.rest import Client

# Carregar variáveis do .env
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")

class WhatsApp:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_message(self, to_number, text):
        message = self.client.messages.create(
            from_=self.from_number,
            body=text,
            to=to_number
        )
        print("Mensagem enviada! SID:", message.sid)
        return message.sid

    def send_code(self, to_number):
        code = random.randint(1000, 9999)
        text = f"Seu código de verificação é: {code}"
        self.send_message(to_number, text)
        return code

# --- USO ---
'''if __name__ == "__main__":
    to_number = 'whatsapp:+5511985478886'  # Seu número
    whatsapp = WhatsApp(account_sid, auth_token, from_number)
    codigo = whatsapp.send_code(to_number)
    print("Código enviado:", codigo)'''