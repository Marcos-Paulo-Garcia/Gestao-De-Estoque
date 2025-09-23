import os
import random
from pathlib import Path
from dotenv import load_dotenv
from twilio.rest import Client

# --- Localizar o .env na raiz do projeto ---
# __file__ = caminho do script atual
# parents[3] = três níveis acima, que é a raiz do projeto
env_path = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=env_path)

# --- Pegar credenciais do Twilio ---
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")

# Verificação rápida das credenciais
if not all([ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER]):
    raise ValueError(f"As credenciais do Twilio não foram encontradas no .env! "
                     f"Checado em: {env_path}")

class WhatsApp:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        self.from_number = FROM_NUMBER

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

# --- Exemplo de uso ---
if __name__ == "__main__":
    to_number = 'whatsapp:+5511960691978'  # Coloque seu número aqui
    whatsapp = WhatsApp()
    codigo = whatsapp.send_code(to_number)
    print("Código enviado:", codigo)
