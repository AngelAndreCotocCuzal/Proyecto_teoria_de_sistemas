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

    def updateProduct(self, codigo, describcion, cod, existencia, costo, publico):
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario_proyecto SET Describcion = %s, Codmedidainv = %s, Existencia = %s,
            Costo = %s, Publico = %s WHERE Codigo = %s """
            cursor.execute(sql, (codigo, describcion, cod, existencia, costo, publico))
            self.conn.commit()

    def eliminar_producto(self, cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM inventario_proyecto WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
