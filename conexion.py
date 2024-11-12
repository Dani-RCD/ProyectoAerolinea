import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # No tiene contraseña según tu descripción
        database='a_carillo'
    )
    return conn
