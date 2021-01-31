systemMenu = {"ข้าว":5,"ขนมจีน":15,"ก๋วยเตี๋ยว":30,"หมูปิ้ง":10}
menuList = []
def showBill():
    print("--- Order ---")
    totalPrice = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

def total():
    print("--- Total ---")
    totalPrice = 0
    for i in range(len(menuList)):
        totalPrice += menuList[i][1]
    print(totalPrice, "THB")

while True:
    menuName = input("Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
        #menuList.append(menuName)
showBill()
total()