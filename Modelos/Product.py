class Product():
    def __init__(self, conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS product
                        (Codigo VARCHAR(15) NOT NULL,
                        Describcion VARCHAR(190) NOT NULL,
                        Codmedidainv VARCHAR(40) NOT NULL,
                        Existencia VARCHAR(10) NOT NULL,
                        Costo VARCHAR(10) NOT NULL,
                        Publico VARCHAR(10) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()

    def obtener_producto(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProduct(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            result = cursor.fetchone()
            if result:
                return result

    def updateProduct(self, codigo, describcion, cod, existencia, costo, publico):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET Describcion = %s, Codmedidainv = %s, Existencia = %s,
            Costo = %s, Publico = %s WHERE Codigo = %s """
            cursor.execute(sql, (codigo, describcion, cod, existencia, costo, publico))
            self.conn.commit()

    def eliminar_producto(self, cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM product WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
