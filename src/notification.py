import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE_ID = os.environ.get("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.environ.get("ZAPI_TOKEN")

def send_whatsapp_message(contact_name: str, contact_phone: str) -> bool:
    if not ZAPI_INSTANCE_ID or not ZAPI_TOKEN:
        logging.error("As variáveis de ambiente da Z-API não foram configuradas.")
        return False

    api_url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_TOKEN
    }
    payload = {
        "phone": contact_phone,
        "message": f"Olá {contact_name}, tudo bem com você?",
    }

    try:
        logging.info(f"Enviando mensagem para {contact_name} ({contact_phone})...")
        response = requests.post(api_url, json=payload, headers=headers)

        response.raise_for_status()
        logging.info(f"Mensagem enviada com sucesso para {contact_name}.")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao enviar mensagem para {contact_name}: {e}")
        if e.response is not None:
            logging.error(f"Detalhe da API: {e.response.text}")
        return False