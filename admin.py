from products import Product
from customer import Customer


class Admin:
    def __init__(self, admin_id=0, admin_name=""):
        self.admin_id = admin_id
        self.admin_name = admin_name

    @staticmethod
    def view_products(self):
        view = Product()
        view.display_products()

    @staticmethod
    def add_products(product_id=0, name="", group="", sub_group=""):
        p1 = Product(product_id, name, group, sub_group)
        p1.product_shop.append(p1)
        # p2 = Product(2, "Eggs", "Dairy", "Eggs")
        # p2.product_shop.append(p2)
        # p3 = Product(3, "Bread", "Bakery", "Bread")
        # p3.product_shop.append(p3)
        # p4 = Product(4, "Butter", "Dairy", "Butter")
        # p4.product_shop.append(p4)
        # p5 = Product(5, "Cheese", "Dairy", "Cheese")
        # p5.product_shop.append(p5)
        # p6 = Product(6, "Yogurt", "Dairy", "Yogurt")
        # p6.product_shop.append(p6)
        # p7 = Product(7, "Curd", "Dairy", "Curd")
        # p7.product_shop.append(p7)
        # p8 = Product(8, "Ice Cream", "Dairy", "Ice Cream")
        # p8.product_shop.append(p8)
        # p9 = Product(9, "Cakes", "Bakery", "Cakes")
        # p9.product_shop.append(p9)
        # p10 = Product(10, "Cookies", "Bakery", "Cookies")
        # p10.product_shop.append(p10)

    @staticmethod
    def delete_products(self, product_name):
        delete = Product()
        for product in delete.product_shop:
            if product.name == product_name:
                delete.product_shop.remove(product)
                print("Product deleted successfully")
                break
            else:
                print("Product not found")

    @staticmethod
    def modify_products(self, product_name=""):
        modify = Product()
        for product in modify.product_shop:
            if product.name == product_name:
                print("Product found")
                print("Enter new product details")
                product.product_id = int(input("Enter product id: "))
                product.name = input("Enter product name: ")
                product.group = input("Enter product group: ")
                product.sub_group = input("Enter product sub group: ")
                p1 = Product(product.product_id, product.name, product.group, product.sub_group)
                print("Product modified successfully")
                break
            else:
                print("Product not found")

    @staticmethod
    def view_customers(self):
        view = Customer()
        view.display_customers()

    def make_shipment(self):
        pass

    def confirm_delivery(self):
        pass
