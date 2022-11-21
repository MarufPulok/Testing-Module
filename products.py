class Product:
    number_of_products = 0

    def __init__(self, product_id=0, name="", group="", sub_group=""):
        self.product_id = product_id
        self.name = name
        self.group = group
        self.sub_group = sub_group
        Product.number_of_products += 1

    product_shop = []

    # def add_product(self):
    #     self.product_shop.append(self)

    def display_products(self):
        print("Products available in the shop are:")
        for product in self.product_shop:
            print(product.product_id, product.name, product.group, product.sub_group)
