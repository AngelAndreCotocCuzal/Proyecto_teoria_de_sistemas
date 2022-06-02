import sys
import os
from Base_de_datos.Connection import connection
from Modelos.Product import Product

myDir = os.getcwd()
sys.path.append(myDir)


class CreateProductController():
    def __init__(self, create_product):
        self.product = Product(connection())
        self.create_product = create_product
    
    def createProduct(self, codigo, describcion, media, existencia, costo, publico, CreateProduct):
        if codigo and describcion and media and existencia and costo and publico:
            self.product.insertProduct(codigo, describcion, media, existencia, costo, publico)
            CreateProduct.hide()
