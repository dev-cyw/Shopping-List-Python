from FunctionsShop import OptionSelector
from FunctionsShop import shopList
print(" (1) is to input a new item\n (2) is to see what item\n (3) is to show the amount of items\n (4) is to delete an item\n (5) is to read the current list")
OptionSelector()
#Creates a text file/Edits the file
if len(shopList) == 0:
    exit()
else:
    txtfile = open('ShoppingList.txt', 'w')
    txtfile.write(str(shopList))
    txtfile.close()
