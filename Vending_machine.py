items = [
    {
        'code':1,
        'name':'Coca cola can',
        'price':30
    },
    
    {
        'code':2,
        'name':'Cadbury',
        'price':50
    },
    
    {
        'code':3,
        'name':'Chips',
        'price':30
    },
    
    {
        'code':4,
        'name':'Packet of dry fruits',
        'price':105
    },
    
    
    
    {
        'code':5,
        'name':'Sprite Can',
        'price':50
    },
    
    
    
    {
        'code':6,
        'name':'Cup Noodles',
        'price':65
    },
] # This is the items list which contains information related to the food product within a nested dictionary.


run_vend = True # This is a flag variable that will help to run the loop inside and in later case to exit the program to stop it.
item = ''

''' This is the main part of the program. It runs a while loop when the flag variable is true.
It prints the list of items present and its details like code number and the price. Then it 
asks for the code number of the particular item. After entering it asks to enter the money.
If the amount of money is not sufficient, it will ask to either renew or exit the transaction.
If the amount entered is exact, then it will print thank you and will ask to either exit or renew
transaction process for new item. If the amount entered is more, the program will print the amount
refunded as balance money.'''

while run_vend == True:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} Rupees")

        price = int(input(f"Enter {item['price']} money to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        elif price > item['price']:
            print("The balance amount is:", price-item['price'])
        else:
            print(f"Please enter only {item['price']} Rupees")

# This part of the program helps us to exit the loop of vending machine or continue further transactions.

    query = input("To quit the machine enter q and to continue buying enter c: ")
    if query == 'c':
        run_vend = True
    else:
        break
    if query == 'q':
        run_vend = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# This project has been developed independently by me(Roham Maiti) so no illegal coppyig ;).
