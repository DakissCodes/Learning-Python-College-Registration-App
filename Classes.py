
'''
PRODUCT INVENTORY

'''
import time 
import os

def user_input(): # User prompt in terminal

    prompt = input('\n[0] Exit application\n[1] Add New Product\n[2] Delete Existing Product\
        \n[3] Delete All Products\n[4] Add Product Quantity\n[5] Remove Product Quantity\n[6] Edit Product\n[7] View Product\
        \n[8] View All Products\n\nENTER: ')

    return int(prompt)

class Inventory:

    def __init__(self): # List where products are stored
        self.products = []

    def add(self,prod): # Appends products to the list
        self.products.append(prod)

    def get_len(self):
        if len(self.products) == 0:
            print('Inventory is empty!')
        return len(self.products)

    def delete_product(self,id_number): # Deletes a product

        for _ in self.products:

            if _.id_number == id_number:

                self.products.remove(_)
                print('\nProduct successfully removed!')
                return True

            else:

                print('Product not found!')
                return False


    def add_quantity(self,quantity,id_number,product): # Add quantities to existing products
        for _ in self.products:

            if _.id_number == id_number:

                _.quantity += quantity
                print(product)
                print('\nProduct quantity increased!')

    def minus_quantity(self,quantity,id_number,product): # Substratcs quantities to existing products

        for _ in self.products:

            if _.id_number == id_number:

                if _.quantity >= quantity:
                    _.quantity -= quantity
                    print(product)
                    print('\nProduct successfully decreased!')    
                    return True  

                else:

                    print('\nInsufficient amount!')
                    return False

    def product_rename(self,id_number,product):   # Edits product attributes

        index = int(input('\n[0] Exit\n[1] Edit name\n[2] Edit Product ID\n[3] Edit Price\nENTER: '))

        if index == 1: # Edit name
            time.sleep(.5)
            os.system('cls')
            print(product)
            new = '5'

            while new.isdigit():
                new = input('\nEnter New Product Name: ')

                if new.isdigit():
                    
                    print('\nMust be letters!')
                    time.sleep(.5)
                    os.system('cls')
                    print(product)

            product.name = new
            print('\nSuccessfully changed!')
            
        elif index == 2: # Edit product ID
            time.sleep(.5)
            os.system('cls')
            print(product)                    
            new = ''
            while not new.isdigit(): 

                new = input('\nEnter new ID: ')

                if not new.isdigit():

                    print('\nMust be numbers!')
                    time.sleep(.5)
                    os.system('cls')
                    print(product)

            product.id_number = int(new)
    
            print('\nSuccessfully changed!')

        elif index == 3: # Edit price
            time.sleep(.5)
            os.system('cls')
            print(product)
            new = ''

            while not new.isdigit():
                
                new = input('\nEnter New Product Price: ')

                if not new.isdigit():

                    print('\nMust be numbers!')
                    time.sleep(.5)
                    os.system('cls')
                    print(product)

            product.price = int(new)

            print('\nSuccessfully changed!')
        else:
            return 0
 
    def check_duplicate(self,id_num,name_given): # Checks whether name/id_number is already chosen
        for _ in self.products:

            if _.name == name_given:
                return True
            elif _.id_number == id_num:
                return True
            else:
                continue
            
        return False
        

    def product_display(self,id_num): # Prints a product
        for _ in self.products:
            if _.id_number == id_num:
                print(_)
        return _

            


class Product(Inventory):

    def __init__(self,name,id_number,price,quantity): # Adds a new type of product to the inventory

        self.name = name
        self.id_number = id_number
        self.price = price
        self.quantity = quantity
    
    def __str__(self): 

        return f'\nProduct Name: {self.name}\nProduct ID: {str(self.id_number)}\
            \nProduct Price: PHP {int(self.price)}\nProduct Quantity: {str(self.quantity)}'


new_inventory = Inventory() # Inventory

