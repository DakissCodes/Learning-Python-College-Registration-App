
from pickle import FALSE
import sys
import Classes
import time
import os
new_inventory = Classes.Inventory()

user = ''
new_inventory.add(Classes.Product('Test',1,150,100))
while user != 0:
    print('\nLoading...')
    time.sleep(.25)
    os.system('cls')
    user = int(Classes.user_input())

    if user == 0:
        continue
    elif user == 1:
        os.system('cls')
        name = '0'
        dup = True

        while name.isdigit() or dup:
            name = input('\nEnter Product Name: ')
            dup = new_inventory.check_duplicate(name,None)
            if name.isdigit():
                print('\nInvalid name, must be letters!')

            if dup:
                print('\nName already taken!')
            time.sleep(.5)
            os.system('cls')
            
        id_num = ''
        while not id_num.isdigit() or dup:
            id_num = input('\nEnter Product ID Here: ')
            dup = new_inventory.check_duplicate(None,int(id_num))
            if not id_num.isdigit():
                print('\nInvalid ID, must be numbers!')
            if dup:
                print('\nID already taken!')
            time.sleep(.5)
            os.system('cls')
        
        price = ''
        while not price.isdigit():
            price = input('\nEnter Price Here: ')
            if not id_num.isdigit():
                print('\nInvalid price, must be numbers!')
            time.sleep(.5)
            os.system('cls')

        prod = Classes.Product(name,int(id_num),int(price),0)
        new_inventory.add(prod)
        print(prod)
        print('\nProduct successfully added!')

    elif user == 2: # Delete existing products 
        if len(new_inventory.products) == 0:
            print('\nNo such product found in inventory!')
            time.sleep(.5)
            continue
        
        id_num = ''
        bool = False
        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID Here: ')
            if not id_num.isdigit():
                print('\nMust be numbers!')
                time.sleep(.5)
                os.system('cls')
                continue
            bool = new_inventory.delete_product(int(id_num))
            time.sleep(.5)
            os.system('cls')
                
    elif user == 3: # add quantity 
        os.system('cls')
        id_num = ''
        quantity = ''
        bool = False
        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID Here: ')
            bool = new_inventory.check_duplicate(None,int(id_num))
            if not id_num.isdigit():
                print('\nMust be numbers!')
            if not bool:
                print('\nProduct not found!')
            time.sleep(.5)
            os.system('cls')        
        while not quantity.isdigit():
            quantity = input('\nEnter Amount Here: ')
            if not quantity.isdigit():
                print('\nMust be numbers!')
            time.sleep(.5)
            os.system('cls')
        new_inventory.add_quantity(int(quantity),int(id_num))

        
    elif user == 4: # Remove product quantity 

        id_num = ''
        quantity = ''
        bool = False
        while not id_num.isdigit() or not bool:

            id_num = input('\nEnter Product ID Here: ')
            bool = new_inventory.check_duplicate(None,int(id_num))

            if not id_num.isdigit():
                print('\nMust be numbers!')
                
            if not bool:
                print('\nProduct not found!')
            time.sleep(.5)
            os.system('cls')
        bool = False
        while not quantity.isdigit() or not bool:

            for _ in new_inventory.products:
                if _.id_number == int(id_num):
                    print('\n')
                    print(_)   

            quantity = input('\nEnter Amount Here:')
            if not quantity.isdigit():
                print('\nMust be numbers!')
                time.sleep(.5)
                os.system('cls')
                continue
            bool = new_inventory.minus_quantity(int(quantity),int(id_num))
            if not bool:
                break 


    
    elif user == 5: # Edit product
        os.system('cls')
        if len(new_inventory.products) == 0: 
            print('\nNo such product found in inventory!')
            continue
        id_num = ''
        bool = False
        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID: ')
            if not id_num.isdigit():
                print('\nMust be numbers!')
                time.sleep(.5)
                os.system('cls')
                continue
            bool = new_inventory.check_duplicate(None,int(id_num))
            if not bool:
                print('\nProduct not found!')
            time.sleep(.5)
            os.system('cls')
        index = ''

        while True:


            index = input('\n[0] Exit\n[1] Edit name\n[2] Edit Product ID\n[3] Edit Price\nENTER: ')
            if int(index) == 0:
                break
            new_inventory.product_rename(int(id_num),int(index))  
            time.sleep(.5)

            os.system('cls')
            id_num = _.id_number

    elif user == 6:
        os.system('cls')
        if len(new_inventory.products) == 0:
            print('\nNo product in inventory yet!')
            continue
        id_num = ''
        bool = False
        while not id_num.isdigit() or not bool: # BUG": cannot find the product
            id_num = input('\nEnter Product ID: ')
            if not id_num.isdigit():
                print('\nMust be numbers!')
                continue
            bool = new_inventory.check_duplicate(None,int(id_num))
            if not bool:
                print('\nProduct not found!')
        os.system('cls')
        for _ in new_inventory.products:
            if _.id_number == int(id_num):
                print(_)   
        


    
    elif user == 7:
        if len(new_inventory.products) == 0:
            print('No product in inverntory!')
            continue
        os.system('cls')
        for _ in new_inventory.products:
            print(_)
            print('\n')
    
    exit_prompt = input('\n[Hit Enter to Exit] ')


        
      
