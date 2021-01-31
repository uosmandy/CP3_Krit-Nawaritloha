menuList = []
priceList = []
def showBill():
    print("--- Order ---")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
def total():
    print("--- Total ---")
    totalPrice = 0
    for p in priceList:
        totalPrice = totalPrice + int(p)
    print(totalPrice, "THB")
while True:
    menuName = input("Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
total()

