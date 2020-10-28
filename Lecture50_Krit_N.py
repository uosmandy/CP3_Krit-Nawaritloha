Method = input("Select function : ")
if Method == "+":
    def AddNumber(x, y):
        print(x + y)
    AddNumber(9, 3)
elif Method == "-":
    def AddNumber(x, y):
        print(x - y)
    AddNumber(8, 1)
elif Method == "*":
    def AddNumber(x, y):
        print(x * y)
    AddNumber(2, 2)
elif Method == "/":
    def AddNumber(x, y):
        print(int(x / y))
    AddNumber(12, 4)


