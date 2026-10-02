import json
import os
inventory = []

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        print("Inventory loaded successfully.")
        return data

    print("inventory.json not found. Starting with an empty inventory.")
    return []
def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)

    print("\nProduct added successfully!")


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    new_stock = int(input("\nNew Stock Quantity: "))
    product["stock"] = new_stock

    print("\nStock updated successfully!")


def display_all(inventory):
    if not inventory:
        print("No products in inventory.")
        return

    print("\nCurrent Inventory")
    print("-" * 48)
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)


# --- temporary test (delete once the menu is built) ---
inventory.append({"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15})
inventory.append({"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40})

search_product(inventory)    # enter P002 -> shows Mouse
search_product(inventory)    # enter P999 -> Product not found.
update_stock(inventory)      # enter P002, then 50
update_stock(inventory)      # enter P999 -> Product not found.
display_all(inventory)       # Mouse should show Stock: 50
