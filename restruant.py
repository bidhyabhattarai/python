class Resturant:
    # class variable
    menu = {
        "Pizza": 500,
        "burger": 600,
        "pasta": 400,
        "salad": 300
    }

    def __init__(self, customer_name):
        # objects attributes
        self.customer_name = customer_name
        self.order = []
        self.order_summary = {}
        self.discount = 0

    # order process for customer
    def place_order(self, item, quantity):
        if item in Resturant.menu:
            price = Resturant.menu[item] * quantity
            order = (item, quantity, price)
            self.order.append(order)
            print("Order placed successfully")
        else:
            print("Item not in menu")

    def show_summary(self):
        print("Order Summary ")
        print("Customer Name: {}".format(self.customer_name))

        total_bill = 0
        for item, qnty, price in self.order:
            print("Item: {:<8} | Qty: {:<3} | Price: {}".format(item, qnty, price))
            total_bill += price

        print("Total Amount: {}".format(total_bill))


customer1 = Resturant("bidhya")
customer1.place_order("Pizza", 5)
customer1.place_order("burger", 2)

customer1.show_summary()