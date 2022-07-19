def shopInput():
    shopItem = input("Enter the name of the item to add.")
    shopList.append(shopItem)
def itemNum():
    Numb = int(input("Enter the number to see the item:"))
    Numb = Numb - 1
    listNumb = shopList[Numb]
    print(listNumb)
def listAmount():
    print("The number of items of the shopping list is " + str(len(shopList)))
    print(shopList)
shopList = ["Milk", "Bread"]
print(shopList)
listAmount()
