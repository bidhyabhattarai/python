class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Laptop brand : {} ".format(self.brand))
        print("Laptop price : {} ".format(self.price))


order1 = Laptop(brand="dell", price=10000)
order2 = Laptop(brand="hp", price=20000)

print(order1.brand, order1.price)
print(order2.brand, order2.price)