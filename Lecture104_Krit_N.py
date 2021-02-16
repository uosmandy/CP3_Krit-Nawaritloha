class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to", self.name, self.lastname,"Cart.")

customer1 = Customer()
customer1.name = "Bird"
customer1.lastname = "NL"
customer1.addCart()

customer2 = Customer()
customer2.name = "Thana"
customer2.lastname = "KHO"
customer2.addCart()

customer3 = Customer()
customer3.name = "Bill"
customer3.lastname = "HO"
customer3.addCart() 