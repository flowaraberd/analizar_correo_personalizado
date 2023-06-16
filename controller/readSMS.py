from utils.databse import set_connection
from utils.save_data import save


def action_save_data(message_data, cursor):
    sms_data = []
    try:
        sms_data = str(message_data[b"BODY[TEXT]"].decode("utf-8")).replace('\r', '').replace('\n', '').split(
            " ")
    except UnicodeDecodeError as e:
        try:
            sms_data = str(message_data[b"BODY[TEXT]"].decode("latin-1")).replace('\r', '').replace('\n', '').split(
                " ")
        except Exception as err:
            print("Error linia 45 archivo readSMS.py")

    try:
        sms_data_result = list(filter(lambda x: (x != '' and x != '/'), sms_data))
        try:
            precio_in = sms_data_result.index('Bs.')
        except Exception as err:
            precio_in = sms_data_result.index('Bs,')

        fecha_in = sms_data_result.index('día')
        referencia_in = sms_data_result.index('referencia')
        numero_in = sms_data_result.index("celular")

        precio = sms_data_result[precio_in + 1]
        fecha = sms_data_result[fecha_in + 1]
        hora = sms_data_result[fecha_in + 4].replace(',', '')
        referencia = sms_data_result[referencia_in + 1].replace('.', '')
        numero = sms_data_result[numero_in + 1].replace('*', '').replace('-', '').replace(',', '')

        data = {"precio": precio, "fecha": fecha, "ultimo_numero": numero, "hora": hora, "referencia": referencia}
        save(cursor=cursor, **data)
    except Exception as error_:
        print("Error(CONTROLADO) linea 37 archivo readSMS.py", error_)


def read_sms(client, messages):
    connect = set_connection()
    cursor = connect.cursor()

    # Obtener información de los correos no leídos
    for uid, message_data in client.fetch(messages, ["BODY[TEXT]"]).items():
        action_save_data(message_data, cursor)

    # COMMIT PARA GUARDAR LA TRANSFERENCIA DEL MOMENTO
    connect.commit()
    # CERRAR LA CONEXIÓN
    connect.close()

    # Marcar los correos como leídos
    # client.set_flags(messages, [imapclient.SEEN])


