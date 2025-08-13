import logging
import time
from database import get_supabase_client, fetch_contacts
from notification import send_whatsapp_message

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Iniciando o processo de envio de mensagens.")
    supabase_client = get_supabase_client()
    contacts = fetch_contacts(supabase_client)

    if not contacts:
        logging.info("Nenhum contato para processar. Encerrando.")
        return

    success_count = 0
    fail_count = 0
    for contact in contacts:
        name = contact.get("name")
        phone = contact.get("phone")
        if name and phone:
            if send_whatsapp_message(name, phone):
                success_count += 1
            else:
                fail_count += 1
            time.sleep(2)
        else:
            logging.warning(f"Registro de contato incompleto e ignorado: {contact}")
            fail_count += 1

    logging.info("Processo finalizado.")
    logging.info(f"Resumo: {success_count} mensagens enviadas com sucesso, {fail_count} falhas.")

if __name__ == "__main__":
    main()