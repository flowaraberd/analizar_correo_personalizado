import imapclient
from controller.readSMS import read_sms
from controller.config import (
    HOST,
    USERNAME,
    PASSWORD
)


def connect_with_sms():
    # Conexión al servidor IMAP
    with imapclient.IMAPClient(HOST) as client:
        # Inicio de sesión
        client.login(USERNAME, PASSWORD)

        # Seleccionar la carpeta de entrada (INBOX)
        client.select_folder('INBOX')

        # Buscar todos los correos no leídos
        messages = client.search(['SEEN'])
        # messages = client.search(['UNSEEN'])

        read_sms(client=client, messages=messages)

        # # Obtener información de los correos no leídos
        # for uid, message_data in client.fetch(messages, ['RFC822']).items():
        #     print(f'UID: {uid}')
        #     print(f'Cuerpo: {message_data[b"RFC822"].decode()}')
        #     print('---')
        #
        # # Marcar los correos como leídos
        # # client.set_flags(messages, [imapclient.SEEN])

    # Fin de la conexión
