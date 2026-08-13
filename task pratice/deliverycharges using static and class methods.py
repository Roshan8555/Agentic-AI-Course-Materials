class Product:
    platform = "Flipkart"
    delivery_charges = 60

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Class method
    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60

    # Instance method
    def display_items(self):
        if self.price > 30000:
            # Free delivery
            final_price = self.price
            print(f"Item is {self.name}")
            print(f"Product price: {self.price}")
            print("Delivery charges: 0")
            print(f"Final price: {final_price}")
        else:
            # Delivery charges applicable
            final_price = self.price + Product.delivery_charges
            print(f"Item is {self.name}")
            print(f"Product price: {self.price}")
            print(f"Delivery charges: {Product.delivery_charges}")
            print(f"Final price: {final_price}")

    # Static method
    @staticmethod
    def free_delivery(price):
        if price > 30000:
            return 0
        return Product.delivery_charges


# Create objects
obj1 = Product("Oneplus", 45000)
obj2 = Product("Laptop", 25000)

# Update delivery charges using class method
Product.update_delivery()

print("Product 1:")
obj1.display_items()

print("\nProduct 2:")
obj2.display_items()

print("Oneplus delivery:", obj1.free_delivery(45000))
print("Laptop delivery:", obj2.free_delivery(25000))

print("\nObject Dictionary:")
print(obj1.__dict__)
