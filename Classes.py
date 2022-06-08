
'''
PRODUCT INVENTORY PROJECT

'''


class Inventory:
    def __init__(self):
        self.products = []

    def add(self,prod):
        self.products.append(prod)

    def delete_product(self,id_number):
        for _ in self.products:
            if _.id_number == id_number:
                self.products.remove(_)
                print('Product successfully removed!')
                return True
            else:
                print('Product not found!')
                return False


    def add_quantity(self,quantity,id_number): # Add quantities to existing products
        for _ in self.products:
            if _.id_number == id_number:
                _.quantity += quantity
                print('Product quantity increased!')

    def minus_quantity(self,quantity,id_number): # Substratcs quantities to existing products

        for _ in self.products:
            if _.id_number == id_number:
                if _.quantity >= quantity:
                    _.quantity -= quantity
                    print('Product successfully decreased!')    
                    return True           
                else:
                    print('Insufficient amount!')
                    return False
    def product_rename(self,id_number,index): # Edits product attributes
        for _ in self.products:
            if _.id_number == id_number:
                
                if index == 1: # Edit name
                    new = '5'
                    while new.isdigit():
                        new = input('\nEnter New Product Name: ')
                        if new.isdigit():
                            print('\nMust be letters!')
                            continue
                    _.name = new
                    print('\nSuccessfully changed!')

                elif index == 2: # Edit product ID
                    new = ''
                    while not new.isdigit(): 
                        new = input('\nEnter new ID: ')
                        if not new.isdigit():
                            print('\nMust be numbers!')
                            continue

                    _.id_number = int(new)
                    print('\nSuccessfully changed!')

                elif index == 3: # Edit price
                    new = ''
                    while not new.isdigit():
                        new = input('\nEnter New Product Price: ')
                        if not new.isdigit():
                            print('\nMust be numbers!')
                            continue
                    _.price = int(new)
                    print('\nSuccessfully changed!')

                elif index == 0:
                    break


    def check_duplicate(self,name_given,id_num,): # Checks whether name/id_number is already chosen
        for _ in self.products:

            if _.name == name_given:
                return True
            elif _.id_number == id_num:
                return True
            else:
                continue
        return False
            
            



class Product(Inventory):
    def __init__(self,name,id_number,price,quantity): # Adds a new type of product to the inventory

        self.name = name
        self.id_number = id_number
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f'Product Name: {self.name}\nProduct ID: {str(self.id_number)}\
            \nProduct Price: {int(self.price)}\nProduct Quantity: {str(self.quantity)}'
def user_input():
    prompt = input('[0] Exit application\n[1] Add New Product\n[2] Delete Existing Product\
        \n[3] Add Product Quantity\n[4] Remove Product Quantity\n[5] Edit Product\n[6] View Product\
        \n[7] View All Products\nENTER:')
    return int(prompt)
#edit = input('[1] Edit Product Name:\n[2] Edit Product ID:\n[3] Edit Product Price:')
