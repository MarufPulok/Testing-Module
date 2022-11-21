from products import Product
from customer import Customer

id = 0


class Guest:
    @staticmethod
    def view_products():
        for product in Product.product_shop:
            print(product.product_id, product.name, product.group, product.sub_group)

    @staticmethod
    def get_registered(self):
        print("Enter your details to get registered")
        # id = input("Enter your id: ")

        name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone = int(input("Enter your phone number: "))
        c1 = Customer(id + 1, name, address, phone)
        c1.customer_list.append(c1)
        print("You have been registered successfully")
        print("You can now buy products")
