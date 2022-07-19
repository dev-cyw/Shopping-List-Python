shopList = []
FuncList = ["shopInput", "itemNum", "listAmount", "delItem"]
def shopInput():
    ItemAdd = 0
    ItemAdd = int(input("Enter the number of items you want to add"))
    while ItemAdd != 0:
        shopItem = input("Enter the name of the item to add.")
        shopList.append(shopItem)
        ItemAdd = ItemAdd - 1
        print(shopList)
def itemNum():
    Numb = int(input("Enter the number to see the item:"))
    Numb = Numb - 1
    listNumb = shopList[Numb]
    print(listNumb)
def listAmount():
    print("The number of items of the shopping list is " + str(len(shopList)))
    print(shopList)
def delItem():

    print(shopList)
    ItemDel = int(input("enter the number of the item you want to delete"))
    ItemDel = ItemDel - 1
    shopList.pop(ItemDel)
    print(shopList)
def OptionSelector():
    x = 1
    while x != 0:
        FuncChoice = int(input("Enter the number of which function you want to choose "))
        if FuncChoice == 1:
            shopInput()
        elif FuncChoice == 2:
            itemNum()
        elif FuncChoice == 3:
            listAmount()
        elif FuncChoice == 4:
            delItem()
        else:
            print("that is not an option")
        x = int(input("Do you want to continue \n1 for yes \n0 for no"))
print(" (1) is to input a new item\n (2) is to see what item\n (3) is to show the amount of items\n (4) is to delete an item ")
OptionSelector()
