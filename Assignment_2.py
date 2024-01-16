# -*- coding: utf-8 -*-
"""
    Created on Tue Jan 6 05:02:32 2024
    Title   :   Inventory Manaement Program
    @author :   Aritr Ranjan Chowdhury 
"""
# %%

class Product (object):
    '''
    Simple Product class to track a single product information.
    NAME, PRICE, QUANTITY and TYPE attributes are there
    NAME is the unique for all product
    '''
    def __init__(self, name, price, quantity, _type):
        super().__init__()
        self.__name = name 
        self.price = price
        self.quantity = quantity
        self.type = _type
    @property
    def name(self):         # Getter Property of Price 
        return self.__name
    @property
    def price (self):       # Getter Property of Price 
        return self.__price
    @property               # Getter Property of Quantity 
    def quantity (self):
        return self.__quantity
    @property
    def type(self):         # Getter Property of type
        return self.__type
    @price.setter
    def price (self, price):     # Setter Property of Price 
        if type(price) not in [int, float]:
            raise Exception("Price is not a number ")
        if price>0: self.__price = price
        else : raise Exception("Price properties of the Product can not be negative")
    @quantity.setter
    def quantity (self, quantity):   # Setter Property of Quantity 
        if type(quantity) not in [int, float]:
            raise Exception("Price is not a number ")
        if quantity>0: self.__quantity = quantity
        else : raise Exception("Price properties of the Product can not be negative")
    @type.setter     # Setter Property of type
    def type(self, type:str):
        self.__type = type
    def __str__(self):      # Display or Print function overloading 
        return f'''Product (
    name = {self.name}
    price = Rs.{self.price}
    quantity = {self.quantity}
    type = {self.type}  )'''

class ProductList(list):
    '''
    Class to track of all Product or do few operation on Product List
    It is a derived class of list that only contains Product type element 
    '''
    def __init__(self, *args):
        for elements in args: 
            if type(elements) is not Product:   # validating Type 
                raise Exception("ProductList can only contain Product")
        super().__init__(args)
    def search_by_name(self,name):
        '''
        Take a name as string and return a Product instance.
        If name is not match with the product in the list it return None
        As name is unique for all product there must be single Product or None
        '''
        for product in self:
            if product.name == name:
                return product
    def total_product(self):
        '''Retuen the total quantity of product in the inventry
Return Sum of all Quantity '''
        return sum([product.quantity for product in self])
    def search_by_type(self,type):
        '''
        Take a type as string and return a new ProductList instance.
        If type is not match with the product in the list it return empty ProductList
        As type is not unique for all product there must be list of multiple Product 
        '''
        return self.__class__(*[product for product in self 
                                if product.type == type])
    def view_product(self):
        '''Display all product available in product in a form of a table'''
        print( 'Profuct List :\n' + '-'*70 +
            '\n%-20sPrice\tQuantity\tType\n'%'Name'+'-'*70 )
        for product in self:
            print("%-20s%.2f\t%5d\t\t%-30s"
                  %(product.name,product.price,product.quantity,product.type))
    def append(self, _product: Product) -> None:
        '''override version the append method that only alows to append only Product element'''
        if type(_product) is not Product: 
            raise Exception("Only Product type element can be append")
        if self.search_by_name(_product.name):
            raise Exception("Duplicat Product Entry is not allow")
        return super().append(_product)
    def insert(self, _index: int, _product: Product) -> None:
        '''override version the insert method that only alows to insert only Product element'''
        if type(_product) is not Product: 
            raise Exception("Only Product type element can be append")
        return super().insert(_index, _product)
    def remove(self, _value:Product) -> None:
        '''remove by the entire product element'''
        return super().remove(_value)
    def remove(self, _value:str) -> None:
        '''remove by the product name(string)'''
        remove_value = self.search_by_name(_value)
        return super().remove(remove_value)
    
# Defing the Product list that are given in question as Default
DEFAULT_PRODUCT_LIST =  ProductList(           
        Product('lettuce',    410.5,  50, 'Leafy green' ),
        Product('cabbage',    20,    100, 'Cruciferous' ),
        Product('pumpkin',    30,    30,  'Marrow'      ),
        Product('cauliflower',10,    25,  'Cruciferous' ),
        Product('zucchini',   20.5,  50,  'Marrow'      ),
        Product('yam',        30,    50,  'Root'        ),
        Product('spinach',    10,    100, 'Leafy green' ),
        Product('broccoli',   20.2,  75,  'Cruciferous' ),
        Product('garlic',     30,    20,  'Leafy green' ),
        Product('silverbeet', 10,    50,  'Marrow'      ))

def take_input(product_list):
    '''function that take input of products from console line by line
It process data and create a ProductList container and return it'''

    print('''Enter Product details as [NAME , PRICE, QUANTITY, TYPE] seperated by coma(,)
        - Enter only value.Avoid Rs or other unit symbol
        - PRICE and QUANTITY mustbe numeric
        - Make sure Product name should be unique''')
    count = 0 ; input_string = input(f"{count} >>")
    while input_string:
        try:
            name,price,quantity,type = input_string.split(',')
            try:
                product_list.append(Product(name,float(price),int(quantity),type))
            except Exception as e:
                print(e)
            count+=1
        except:
            print('Wrong Input format')
        input_string=input(f"{count} >>")
        

    return product_list

def assignment_solution():   
    '''Solution funtion of the assignment '''
    product_list = ProductList( *DEFAULT_PRODUCT_LIST)
    
    print('\nQ: Print the total number of products in the list.')
    print(f'Total number of unique product ={len(product_list)} ')
    print(f'Total number of product = {product_list.total_product()}')

    print('\nQ: Add a new product (Potato,10RS, 50, Root). And print the list of all products and a total number of products(integer).')
    product_list.append(Product('Potato',10, 50, 'Root'))
    product_list.view_product() 
    print(f"Total number of Products = {product_list.total_product()}")

    print('\nQ: Print all the products of which have the type Leafy green.')
    product_list.search_by_type('Leafy green').view_product()

    print('\nQ: As all the garlic is sold out, Remove Garlic from the list and print the total number of products that are left on the list.')

    product_list.remove('garlic')
    print(f"Total number of Products = {product_list.total_product()}")
 
    print('\nQ: If the user adds 50 cabbages to the inventory, print the final quantity of cabbage in the inventory.')
    cabbages = product_list.search_by_name('cabbage').price + 50 
    print(f"Total cabbages will be {cabbages} ")
 
    print('\nQ: If a user purchases 1kg lettuce, 2 kg zucchini, 1 kg broccoli the what is the round figure that the user needs to pay?')
    cost = (product_list.search_by_name('lettuce').price 
            +product_list.search_by_name('zucchini').price * 2
            +product_list.search_by_name('broccoli').price )
    print ( f'Total Cost will be {cost}')

def print_ui():
    '''Printing Function of Basic UI '''
    print('\n\n'+'-'*50+'\nMENU :\n' +'-'*50+'''
 1) Add Products            2) Add Default Products
 3) View All Products       4) Remove Product        
 5) Edit Quantity           6) Serach by Name
 7) Serach by Type          8) Assignment Solution   
 9) Exit
'''+'-'*50)

def main():
    product_list = ProductList() # Creating Empty Product list
    while True:
        print_ui()
        # Choice Validation
        try:
            choice = int(input('Choice : '))
        except: 
            print("Choice must be integer. ")
            continue
        #  switch-case structure based on user's choice
        if choice == 1:     # for adding products
           take_input(product_list)
        elif choice == 2:   # for adding default products
            product_list = ProductList(*DEFAULT_PRODUCT_LIST) # Copy from the DEFAULT_PRODUCT_LIST
        elif choice == 3:   # for viewing all products
            product_list.view_product()
        elif choice == 4:   # for removing a product
            name = input("Enter name of the product :")
            try: 
                product_list.remove(name)
            except:
                print("Element is not present")
        elif choice == 5:   # for editing quantity
            name = input("Enter name of the product :")
            try:
                new_quantity = int(input("Enter new quantity:"))
            except : 
                print('Wrong quantity')
                continue
            if(new_quantity>0):
                product = product_list.search_by_name(name)
                if product: 
                    product.quantity = new_quantity
                else:
                    print("Nme is not in List")
        elif choice == 6:   # for searching by name
            name = input("Enter name of the product :")
            print(product_list.search_by_name(name))
        elif choice == 7:   # for searching by type
            type = input("Enter type of the product :")
            product_list.search_by_type(type).view_product()
        elif choice == 8:   # for assignment solution
            assignment_solution()
        elif choice == 9:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")



#%%
if __name__ == '__main__':
    main()
# %%
