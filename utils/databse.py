import mysql.connector
from controller.config import DATABASE_CONFIG


def set_connection():
    try:
        connect = mysql.connector.connect(**DATABASE_CONFIG)
        return connect
    except mysql.connector.Error as db_error:
        print(f"LA CONEXIÓN A LA BASE DE DATOS HA SIDO ERRONEA {1}\n", db_error)
