inventory = []

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)

    print("\nProduct added successfully!")

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
display_all(inventory)          # should print "No products in inventory."
for _ in range(3):
    add_product(inventory)
display_all(inventory)
