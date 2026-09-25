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

inventory = 0
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

    if inventory > 500:
        print(f"OVERSTOCK ALERT! Total inventory ({inventory}) exceeds 500 units.")
        break

generate_report(inventory, failed_entries)