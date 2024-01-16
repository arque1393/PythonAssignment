# -*- coding: utf-8 -*-
"""
    Created on Tue Jan 8 11:51:16 2024
    Title   :   Encription-Decription Program
    @author :   Aritr Ranjan Chowdhury 
"""
# %% Required Function Development Block
def make_type(key:int) -> callable: # 
    ''' This generate a function that apply on single charector to shift the ascci value.
Takes an integer argument and return a function that take a charecter and shift charector by the given key value.
key : the integer value to be shifted 
Example:
    fun = make_type(3)
    value = fun('a')
    print(value)
Output: 
    'e'
    '''
    return lambda v : chr(32 + (ord(v)+key)%127) if (ord(v)+key)%127 < 32 else chr((ord(v)+key)%127)
# %% Main Function Defination Block 
def main(): # Defining the main funtion 
    option:str = ''         # option value decide the program will continue or not 
    while option !='e':    # e stands for exit 
        message:str = input("\nEnter the Message : ") 
        while True:  # Loop to Validate key value
            try :    # trying to conver key value in integer 
                key:int = int(input( "enter the Key :"))
                break
            except: 
                print ("key Must be an integer! Try Again!")
        while True :  # loop to validate Correct option between Encription and Decription
            encript_type = input("Choose mode.. Encrypt[e] Decrypt[d] : ")
            if encript_type in ['e','d']:break
            else:print('Wrong option' )         
        if encript_type == 'e':
            # incase of encription we pass the key value through the shift function 
            # and map over the whole string 
            print("Encrypted message: "+"".join(map(make_type(key),message)))
        elif encript_type == 'd' : 
            # incase of decription we just make negative the key value and pass through the shift function 
            # and map over the whole string
            print("Encrypted message: "+"".join(map(make_type(-1*key),message)))
        option = input("\nEnter Choice Continue[c]  Exit[e]:")


# %% Main Function Call 
if __name__ == '__main__':
    main() # calling main 
    
