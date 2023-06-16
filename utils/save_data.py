
def save(cursor, **data):
    try:
        # cursor =  connect.cursor()
        sql = "INSERT INTO db_compras (precio, ultimo_numero, fecha, hora, referencia) VALUES (%s, %s, %s, %s, %s)"
        values = (data['precio'], data['ultimo_numero'], data['fecha'], data['hora'], data['referencia'])

        # CURSOR PARA ENVIAR LOS DATOS A ALMACENAR
        cursor.execute(sql, values)

    except Exception as error:
        print(f"ERROR AL INSERTAR EL DATO \n {error}")
        pass
