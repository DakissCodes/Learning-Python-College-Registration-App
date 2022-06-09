
import Classes
import time
import os


user = '' 

while user != 0:

    time.sleep(.25) # Clears the terminal
    os.system('cls')

    user = int(Classes.user_input()) # Query 

    if user == 0:  # Exits the application
        continue

    elif user == 1: # Add new product 
 
        os.system('cls')

        name = '0'
        price = ''
        id_num = ''

        dup = True

        while name.isdigit() or dup: 
            name = input('\nEnter Product Name: ')
            dup = Classes.new_inventory.check_duplicate(None,name) # Checks if name already in Inventory

            if name.isdigit():
                print('\nInvalid name, must be letters!') 

            if dup:
                print('\nName already taken!')

            time.sleep(.25)
            os.system('cls')
            
        

        while not id_num.isdigit() or dup:
            id_num = input('\nEnter Product ID Here: ')
            dup = Classes.new_inventory.check_duplicate(int(id_num),None) # Checks if ID already in inventory

            if not id_num.isdigit():
                print('\nInvalid ID, must be numbers!')

            if dup:
                print('\nID already taken!')

            time.sleep(.25)
            os.system('cls')
        
        

        while not price.isdigit():
            price = input('\nEnter Price Here: ')

            if not id_num.isdigit():
                print('\nInvalid price, must be numbers!')

            time.sleep(.25)
            os.system('cls')

        prod = Classes.Product(name,int(id_num),int(price),0) # Creates the object 
        Classes.new_inventory.add(prod) # Adds the object in list/inventory

        print(prod)
        print('\nProduct successfully added!')

    elif user == 2: # Delete existing products 

        if Classes.new_inventory.get_len() == 0: 
            continue

        id_num = ''
        bool = False

        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID Here: ')

            if not id_num.isdigit():

                print('\nMust be numbers!')
                time.sleep(.25)
                os.system('cls')
                continue

            bool = Classes.new_inventory.delete_product(int(id_num)) # Deletes the product
            time.sleep(.25)
            os.system('cls')

    elif user == 3: # Clears the entire inventory
        Classes.new_inventory.products.clear()
        print('\nAll products successfully cleared!')
                
    elif user == 4: # Add quantity to existing product

        if Classes.new_inventory.get_len() == 0: 
            continue

        os.system('cls')
        id_num = ''
        quantity = ''
        bool = False

        while not id_num.isdigit() or not bool: 
            id_num = input('\nEnter Product ID Here: ')
            bool = Classes.new_inventory.check_duplicate(int(id_num),None) # Checks if product is in inventory

            if not id_num.isdigit():
                print('\nMust be numbers!')

            if not bool:
                print('\nProduct not found!')

            time.sleep(.25)
            os.system('cls')        

        while not quantity.isdigit():
            product = Classes.new_inventory.product_display(int(id_num)) # Displays product info in terminal
            quantity = input('\nEnter Amount Here: ')

            if not quantity.isdigit():
                print('\nMust be numbers!')

            time.sleep(.25)
            os.system('cls')

        Classes.new_inventory.add_quantity(int(quantity),int(id_num),product) # Adds quantity 

        
    elif user == 5: # Deposits product quantity 
        if Classes.new_inventory.get_len() == 0: 
            continue
        time.sleep(.25)
        os.system('cls')

        id_num = ''
        quantity = ''
        bool = False

        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID Here: ')
            bool = Classes.new_inventory.check_duplicate(int(id_num),None) # Checks if product in inventory 

            if not id_num.isdigit():
                print('\nMust be numbers!')
                
            if not bool:
                print('\nProduct not found!')
            time.sleep(.25)
            os.system('cls')

        bool = False

        while not quantity.isdigit() or not bool:
            product = Classes.new_inventory.product_display(int(id_num))

            quantity = input('\nEnter Amount Here:')

            if not quantity.isdigit():

                print('\nMust be numbers!')
                time.sleep(.25)
                os.system('cls')
                continue

            time.sleep(.25)
            os.system('cls')
            bool = Classes.new_inventory.minus_quantity(int(quantity),int(id_num),product) # Deposits quantity 

            if not bool:
                continue 


    
    elif user == 6: # Edit product information
        if Classes.new_inventory.get_len() == 0: 
            continue
        
        id_num = ''
        index = ''
        os.system('cls')


        bool = False

        while not id_num.isdigit() or not bool:
            id_num = input('\nEnter Product ID: ')

            if not id_num.isdigit():

                print('\nMust be numbers!')
                time.sleep(.25)
                os.system('cls')
                continue

            bool = Classes.new_inventory.check_duplicate(int(id_num),None)

            if not bool:
                print('\nProduct not found!')
            time.sleep(.25)
            os.system('cls')


        while True:
            product = Classes.new_inventory.product_display(int(id_num)) # Displays newly edited product information in terminal

            x = Classes.new_inventory.product_rename(int(id_num),product)
            
            if x == 0: break

            time.sleep(.25)
            os.system('cls')
            id_num = product.id_number # Updates id_number if edited

    elif user == 7: # View single product



        if Classes.new_inventory.get_len() == 0: 
            continue
        id_num = ''

        bool = False
        
        while not id_num.isdigit() or not bool: 
            os.system('cls')
            id_num = input('\nEnter Product ID: ')

            if not id_num.isdigit():
                print('\nMust be numbers!')
                continue

            bool = Classes.new_inventory.check_duplicate(int(id_num),None)

            if not bool:
                print('\nProduct not found!')
        time.sleep(.5)
        os.system('cls')
        product = Classes.new_inventory.product_display(int(id_num))

    elif user == 8: # View all products in inventory

        if Classes.new_inventory.get_len() == 0: 
            continue

        os.system('cls')

        for _ in Classes.new_inventory.products:
            print(_)
            print('\n')
    
    exit_prompt = input('\n[Hit Enter to Exit] ')


        
      
