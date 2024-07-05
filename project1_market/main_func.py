#Task1: Dictionaries
items = []

#Task3: Viewing and Adding Items
def view_items():
    print("--------------View Items--------------")
    print("The number of items in the inventory are: %d" %len(items))
    if len(items) != 0:
        print("Here are all the items avaialble in the shop: ")
        for item in items:
            for key, value in item.items():
                print("%s: %s" %(key,value))

def add_items():
     print("---------------Add Items---------------")
     print("To add an item in cart fill form")
     item = {}
     item["name"] = input("item name: ")
     while True:
        try:
            item["quantity"] = int(input("Item quantity:"))
            break
        except ValueError:
            print("Quantity should be in Digits")
     while True:
        try:
            item["price"] = int(input("Item price:"))
            break
        except ValueError:
            print("Quantity should be in Digits")
     print("***Item has been sucessfully added!***")
     items.append(item)

#Task4: Purchasing and Searching for Items
def purchase_items():
    print("--------------Purchase Items--------------")
    print(items)
    purchase_item = input("Which item would you like to choose? Enter name of product")
    purchase_quantity = int(input("Quantity?"))
    for item in items:
        if purchase_item.lower()==item["name"].lower():
            if item["quantity"] != 0:
                if purchase_quantity <= item["quantity"]:
                    print("Pay %d at the checkout" %(item["price"] * purchase_quantity))
                    item["quantity"] -= purchase_quantity
                else:
                        print("Quantity does not meet availability")
            else:
                print("Item out of STOCK!")

def search_items():
        print("--------------Search Items--------------")
        find_item = input("Enter the item name to search in the inventory: ")
        for item in items:
            if item["name"].lower() == find_item.lower():
                print("The Item name" + find_item + "is displayed below with details")
                print(item)
            else:
                print("item not found!")

def edit_items():
      print("--------------Edit Items--------------")
      item_name = input("Enter the name of the item you want to edit: ")
      for item in items:
        if item_name.lower()==item["name"].lower():
            print("Here are the current details of " + item_name)
            print(item)
            item["name"]= input("item name: ")
            while True:
                try:
                    item["quantity"] = int(input("item quantity: "))
                    break
                except ValueError:
                        print("invalid_quantity:The quantity should only be digits")
            while True:
                try:
                    item["price"] = int(input("item price: "))
                    break
                except ValueError:
                    print("invalid_price: The price should only be digits")
                print(item)
        else:
            print("not_found: item not found")


while True:
    print("-------------Welcome to Tech Shop-------------")
    print(" 1.View Items \n 2.Add Items \n 3.Purchase Items \n 4.Search Items \n 5.Edit Items \n 6.Exit")
    choice = int(input("Enter the number of your choice:  "))
    if choice == 1:
        view_items()
    elif choice == 2:
        add_items()
    elif choice == 3:
        purchase_items()
    elif choice == 4:
        search_items()
    elif choice == 5:
        edit_items()
    elif choice == 6:
        print("-------------- -> Exiting Shop -> --------------")
        break
    else:
        print("Invalid option, please try again")

