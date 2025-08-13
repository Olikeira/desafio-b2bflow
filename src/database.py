import os
import logging
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def get_supabase_client() -> Client | None:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        logging.error("Credenciais do Supabase (URL e KEY) não encontradas no .env.")
        return None
    try:
        logging.info("Conectando ao Supabase...")
        return create_client(url, key)
    except Exception as e:
        logging.error(f"Falha ao criar o cliente Supabase: {e}")
        return None

def fetch_contacts(client: Client) -> list:
    if not client: return []
    try:
        logging.info("Buscando contatos no banco de dados...")
        response = client.table("contacts").select("name, phone").execute()
        logging.info(f"{len(response.data)} contatos encontrados.")
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []