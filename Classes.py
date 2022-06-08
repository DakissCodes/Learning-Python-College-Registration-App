
'''
PRODUCT INVENTORY PROJECT

'''
import time 
import os


class Inventory:
    def __init__(self):
        self.products = []

    def add(self,prod):
        self.products.append(prod)

    def delete_product(self,id_number):
        for _ in self.products:
            if _.id_number == id_number:
                self.products.remove(_)
                print('\nProduct successfully removed!')
                return True
            else:
                print('Product not found!')
                return False


    def add_quantity(self,quantity,id_number): # Add quantities to existing products
        for _ in self.products:
            if _.id_number == id_number:
                _.quantity += quantity
                print('\nProduct quantity increased!')

    def minus_quantity(self,quantity,id_number): # Substratcs quantities to existing products

        for _ in self.products:
            if _.id_number == id_number:
                if _.quantity >= quantity:
                    _.quantity -= quantity
                    print('\nProduct successfully decreased!')    
                    return True           
                else:
                    print('\nInsufficient amount!')
                    return False
    def product_rename(self,id_number,index): # Edits product attributes
        for _ in self.products:
            if _.id_number == id_number:
                
                if index == 1: # Edit name
                    new = '5'
                    while new.isdigit():
                        product_display(id_number)
                        new = input('\nEnter New Product Name: ')
                        if new.isdigit():
                            print('\nMust be letters!')

                    _.name = new
                    os.system('cls')
                    print('\nSuccessfully changed!')
                elif index == 2: # Edit product ID
                    new = ''
                    while not new.isdigit(): 
                        product_display(id_number)
                    
                        new = input('\nEnter new ID: ')
                        if not new.isdigit():
                            print('\nMust be numbers!')


                    _.id_number = int(new)
                    os.system('cls')            
                    print('\nSuccessfully changed!')
                elif index == 3: # Edit price
                    new = ''
                    while not new.isdigit():
                        product_display(id_number)
                        
                        new = input('\nEnter New Product Price: ')
                        if not new.isdigit():
                            print('\nMust be numbers!')

                    _.price = int(new)
                    print('\nSuccessfully changed!')
                elif index == 0:
                    break



def product_display(id_num):
    pass
    #for _ in new_inventory.products:
    #    if _.id_number == id_num:
    #        print(_)

            


class Product(Inventory):
    def __init__(self,name,id_number,price,quantity): # Adds a new type of product to the inventory

        self.name = name
        self.id_number = id_number
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f'\nProduct Name: {self.name}\nProduct ID: {str(self.id_number)}\
            \nProduct Price: PHP {int(self.price)}\nProduct Quantity: {str(self.quantity)}'
def user_input():
    prompt = input('\n[0] Exit application\n[1] Add New Product\n[2] Delete Existing Product\
        \n[3] Add Product Quantity\n[4] Remove Product Quantity\n[5] Edit Product\n[6] View Product\
        \n[7] View All Products\n\nENTER:')
    return int(prompt)
#edit = input('[1] Edit Product Name:\n[2] Edit Product ID:\n[3] Edit Product Price:')
