import pymysql


# Establecemos Coneccion con nuestro host
def connection():
    # Conn empieza la coneccion
    conn = pymysql.connect(
        host="localhost", port=3306, user="root",
        password="", db="base_empresa_proyecto"  # Conectamos con el host
    )
    # Para saber si nuestra base esta conectada
    print('Database is Connected!')
    return conn
