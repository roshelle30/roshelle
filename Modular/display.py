from menu_data import MENU

def print_menu():
    print("\n|==================== FAST FOOD MENU ========================|")
    print(f"|{'ID':<8} {'Item Name':<32} {'Price':>8}          |")
    print("|============================================================|")
    for item_id, details in MENU.items():
        print(f"|  {item_id:<6} {details['name']:<32} ₱{details['price']:>7.2f}          |")
    print("|============================================================|")

def print_error_message(message_type):
    if message_type == "id_range":
        print(" Invalid Choice. Please select from 1 to 12.")
    elif message_type == "value_error":
        print(" Numbers only, please!")
    elif message_type == "qty_range":
        print(" Quantity must be at least 1.")
    elif message_type == "invalid_yes_no":
        print(" Invalid answer! Please type 'y' for Yes or 'n' for No.")

def print_order_success(quantity, item_name):
    print(f" Added {quantity}x {item_name} to your order.")

def print_exit_message():
    print("\nThank you for visiting! Goodbye.")

def print_receipt(cart):
    print("\n|========================================================|")
    print("|                    OFFICIAL RECEIPT                    |")
    print("|========================================================|")
    print(f"|{'Item Name':<30} {'Qty':<5} {'Price':>8} {'Total':>9} |")
    print("|--------------------------------------------------------|")

    subtotal = 0.0
    for item in cart:
        total_price = item['price'] * item['quantity']
        subtotal += total_price
        print(f"|{item['name']:<30} {item['quantity']:<5} ₱{item['price']:>7.2f} ₱{total_price:>8.2f} |")

    discount = subtotal * 0.10 if subtotal >= 500.0 else 0.0
    grand_total = subtotal - discount

    print("|--------------------------------------------------------|")
    print(f"| Subtotal:                                     ₱{subtotal:>8.2f}|")
    print(f"| Discount (10% off >= ₱500):                  -₱{discount:>8.2f}|")
    print("|--------------------------------------------------------|")
    print(f"| TOTAL AMOUNT TO PAY:                          ₱{grand_total:>8.2f}|")
    print("|========================================================|")
    print("|          Thank you for ordering! Come again!           |")
    print("|========================================================|\n")