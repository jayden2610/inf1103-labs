def get_valid_input():

    failed_count = 0

    while True:
        user_input = input("Enter stock quantity (or 'quit' to stop): ").strip()

        if user_input.lower() == "quit":
            return "quit", failed_count

        if not user_input.isdigit():
            print("Error: Invalid input. Please enter a whole positive number.")
            failed_count += 1
            continue

        return int(user_input), failed_count

def process_delivery(current_total, new_value):

    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):

    print("\n--- Summary Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

    save_inventory(total_units, failed_attempts)


def load_inventory():
    try:
        with open("inventory_log.txt", "r") as log:
            lines = log.readlines()
    except FileNotFoundError:
        return 0

    inventory = 0
    for line in lines:
        if "Inventory: " in line:
            inventory = int(line.split("Inventory: ")[1].strip())
        elif "Total Units Processed: " in line:
            inventory = int(line.split("Total Units Processed: ")[1].strip())

    return inventory


def save_inventory(total_units, failed_attempts):
    with open("inventory_log.txt", "a") as log:
        log.write("--- Summary Report ---\n")
        log.write(f"Total Units Processed: {total_units}\n")
        log.write(f"Failed/Rejected Entries: {failed_attempts}\n")


inventory = load_inventory()
failed_entries = 0

while True:
    result, failed_count = get_valid_input()
    failed_entries += failed_count

    if result == "quit":
        break

    quantity = result
    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)
    print(f"Delivery of {quantity} units added. Tax on this delivery: {tax:.2f}")

    with open("inventory_log.txt", "a") as log:
        log.write(f"Delivery: +{quantity} units | Tax: {tax:.2f} | Inventory: {inventory}\n")

    if inventory > 500:
        print(f"OVERSTOCK ALERT! Total inventory ({inventory}) exceeds 500 units.")
        break

generate_report(inventory, failed_entries)
