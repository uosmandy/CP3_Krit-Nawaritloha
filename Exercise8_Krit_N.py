username = input("username : ")
password = input("password : ")
if username == "Krit" and password == "1234":
    print("***   Welcome Krit :)   ***")
    print("***    Product list     ***")
    print("1.Hat        :  250 THB")
    print("2.Shoes      :  990 THB")
    print("3.Mask       :   50 THB")
    print("* no VAT include")
    print("*** please select as you wish ***")
    userSelected1 = input("Product name : ")
    amount1 = int(input("amount : "))
    userSelected2 = input("Product name : ")
    amount2 = int(input("amount : "))
    userSelected3 = input("Product name : ")
    amount3 = int(input("amount : "))
    userSelected4 = input("Completed ? : ")
    if userSelected1 == "Hat":
        price1 = 250
        vat = 7
        HPrice = (price1 * amount1) + (price1 * vat/100)
        print("Hat   ", amount1,"x", ": ",    HPrice, " THB")
    if userSelected2 == "Shoes":
        price2 = 990
        vat = 7
        SPrice = (price2 * amount2) + (price2 * vat/100)
        print("Shoes ", amount2,"x", ": ",     SPrice, "THB")
    if userSelected3 == "Mask":
        price3 = 50
        vat = 7
        MPrice = (price3 * amount3) + (price3 * vat / 100)
        print("Mask  ", amount3,"x", ": ",    MPrice, " THB")
    if userSelected4 == "Yes":
        price4 = HPrice + SPrice + MPrice
        print("*** Include VAT")
        print("**** Total : ",   float(price4), "THB")
        print("*** Thank you to shopping ***")

else :
    print("---    Invalid :(    ---")








