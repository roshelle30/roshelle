class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class OrderSystem:
    def __init__(self):
        self.menu = {
            1: MenuItem(1, "Cheesy Smash Burger", 89.00),
            2: MenuItem(2, "Double Bacon Royale", 145.00),
            3: MenuItem(3, "Spicy Zinger Chicken Sandwich", 115.00),
            4: MenuItem(4, "1-Pc. Herb Chicken w/ Rice", 99.00),
            5: MenuItem(5, "2-Pc. Crispy Chicken Mega Meal", 169.00),
            6: MenuItem(6, "Crispy Golden Fries (Large)", 65.00),
            7: MenuItem(7, "Creamy Mashed Potato w/ Gravy", 45.00),
            8: MenuItem(8, "Mozzarella Cheese Sticks (4pcs)", 79.00),
            9: MenuItem(9, "Classic Vanilla Milkshake", 75.00),
            10: MenuItem(10, "Chocolate Brownie Sundae", 55.00),
            11: MenuItem(11, "Ice Cold Soda (Medium)", 35.00),
            12: MenuItem(12, "Brewed Iced Tea (Large)", 45.00)
        }
        self.cart = []

    def display_menu(self):
        print("\n|==================== FAST FOOD MENU ========================|")
        print(f"|{'ID':<8} {'Item Name':<32} {'Price':>8}          |")
        print("|============================================================|")
        for item_id, item in self.menu.items():
            print(f"|  {item_id:<6} {item.name:<32} ₱{item.price:>7.2f}          |")
        print("|============================================================|")

    def print_error_message(self, message_type):
        if message_type == "id_range":
            print(" Invalid Choice. Please select from 1 to 12.")
        elif message_type == "value_error":
            print(" Numbers only, please!")
        elif message_type == "qty_range":
            print(" Quantity must be at least 1.")
        elif message_type == "invalid_yes_no":
            print(" Invalid answer! Please type 'y' for Yes or 'n' for No.")

    def ask_yes_no(self, prompt_message):
        while True:
            answer = input(prompt_message).strip().lower()
            if answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            self.print_error_message("invalid_yes_no")

    def print_receipt(self):
        print("\n|========================================================|")
        print("|                    OFFICIAL RECEIPT                    |")
        print("|========================================================|")
        print(f"|{'Item Name':<30} {'Qty':<5} {'Price':>8} {'Total':>9} |")
        print("|--------------------------------------------------------|")

        subtotal = 0.0
        for item in self.cart:
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

    def start_order(self):
        # 1. Unang pangutana sa ubos
        if not self.ask_yes_no("Do you want to order? (y/n): "):
            print("\nThank you for visiting! Goodbye.")
            return

        # 2. I-display ang Menu
        self.display_menu()

        ordering = True
        while ordering:
            # 3. Prompt nga "Enter Choice (1-12):"
            while True:
                try:
                    item_id = int(input("\nEnter Choice (1-12): "))
                    if item_id in self.menu:
                        break
                    self.print_error_message("id_range")
                except ValueError:
                    self.print_error_message("value_error")

            while True:
                try:
                    quantity = int(input("Enter Quantity: "))
                    if quantity > 0:
                        break
                    self.print_error_message("qty_range")
                except ValueError:
                    self.print_error_message("value_error")

            item = self.menu[item_id]
            self.cart.append({
                "name": item.name,
                "price": item.price,
                "quantity": quantity
            })
            print(f" Added {quantity}x {item.name} to your order.")

            ordering = self.ask_yes_no("\nDo you want to order another item? (y/n): ")

        # 4. Receipt
        self.print_receipt()