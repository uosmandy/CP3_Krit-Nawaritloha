menuList = []
priceList = []
def showBill():
    print("--- Order ---")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
while True:
    menuName = input("Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])
showBill()