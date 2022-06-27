class Product():
    def __init__(self, conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS inventario_proyecto
                        ( `Codigo` VARCHAR(15) NOT NULL , `Descripcion` VARCHAR(100) NOT NULL ,
                         `Cantidad` VARCHAR(15) NOT NULL , `Existencias` INT(15) NOT NULL ,
                          `Costo` REAL NOT NULL , `Publico` REAL NOT NULL )"""
            cursor.execute(sql)
            self.conn.commit()

    def obtener_producto(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario_proyecto"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProduct(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario_proyecto WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            result = cursor.fetchone()
            if result:
                return result

    def updateProduct(self, Codigo, Describcion, Cantidad, Existencia, Costo, Publico):
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario_proyecto SET Describcion = %s, Cantidad = %s, Existencia = %s,
            Costo = %s, Publico = %s WHERE Codigo = %s """
            cursor.execute(sql, (Describcion, Cantidad, Existencia, Costo, Publico, Codigo))
            self.conn.commit()

    def eliminar_producto(self, cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM inventario_proyecto WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()

    def insertProduct(self,codigo, describcion, media, existencia, costo, publico):
        print("datos recibidos")
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO inventario_proyecto (Codigo,Descripcion,Cantidad,Existencias,Costo,Publico) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (codigo, describcion, media, existencia, costo, publico))
            self.conn.commit()

    def modificar_inventario(self, codigo, numero):
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario_proyecto SET Existencias = %s WHERE Codigo = %s """
            cursor.execute(sql, (numero, codigo))
            self.conn.commit()

    # def modificar_inventario(self, codigo, numero):
    #    with self.conn.cursor() as cursor:
    #        sql = """UPDATE inventario_proyecto SET Publico = 200 WHERE Codigo = "ACA0005" """
    #        cursor.execute(sql)
    #        self.conn.commit()