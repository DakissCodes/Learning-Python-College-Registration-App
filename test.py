from distutils.ccompiler import new_compiler
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from math import prod
from msilib.schema import Class
import Classes

new_inventory = Classes.Inventory()

prod_1 = Classes.Product('Soap',1,50,100)

new_inventory.add(prod_1)
prod_1 = Classes.Product('Beer',12,1,190)

new_inventory.add(prod_1)

for _ in new_inventory.products:
    print(_.name)
    print(_.id_number)
    print(_.price)
    print(_.quantity)