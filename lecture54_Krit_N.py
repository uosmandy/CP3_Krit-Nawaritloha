def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("--- Invalid username or password ---")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Menu select : "))
    if userSelected == 1:
        print("--- Vat Calculator ---")
        return vatCalculator()
    elif userSelected == 2:
        print("--- Price Calculator ---")
        return priceCalculator()

def vatCalculator():
    price = int(input("price : "))
    vat = 7
    result = price + (price * vat / 100)
    print(result)
    return menuSelect()

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    priceVat = price1 + price2
    vat = 7
    print(priceVat + (priceVat * vat / 100))
    return menuSelect()

print(login())


