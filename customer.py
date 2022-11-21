from products import Product
class Customer:
    number_of_customers = 0

    def __init__(self, id="", name="", address="", phone=0):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        Customer.number_of_customers += 1

    customer_list = []

    def buy_products(self):
        pass

    @staticmethod
    def view_products(self):
        product = Product()
        product.display_products()

    def make_payment(self):
        pass

    def add_to_cart(self):
        pass

    def delete_from_cart(self):
        pass

    def display_customers(self):
        for customer in self.customer_list:
            print(customer.id, customer.name, customer.address, customer.phone)
