from admin import Admin
from guest import Guest

a1 = Admin(1, "Admin")

a1.add_products(1, "Milk", "Dairy", "Milk")
a1.add_products(2, "Eggs", "Dairy", "Eggs")
a1.add_products(3, "Bread", "Bakery", "Bread")
a1.add_products(4, "Butter", "Dairy", "Butter")
a1.add_products(5, "Cheese", "Dairy", "Cheese")
a1.add_products(6, "Yogurt", "Dairy", "Yogurt")
a1.add_products(7, "Curd", "Dairy", "Curd")
a1.add_products(8, "Ice Cream", "Dairy", "Ice Cream")
a1.add_products(9, "Cakes", "Bakery", "Cakes")
a1.add_products(10, "Cookies", "Bakery", "Cookies")

# a1.view_products(self=Admin)

# a1.delete_products("Milk")
# a1.view_products(self=Admin)
# a1.modify_products(self=Admin, product_name="Milk")
# a1.view_products(self=Admin)


# guest registration
# g1 = Guest()
# g1.view_products()
# g1.get_registered(self=Guest)
# a1.view_customers(self=Admin)
