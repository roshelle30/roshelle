from menu_data import MENU
from display import print_menu, print_error_message, print_order_success, print_exit_message, print_receipt
from helpers import ask_yes_no

def main():
    # 1. Unang pangutana sa ubos
    want_to_order = ask_yes_no("Do you want to order? (y/n): ")

    if not want_to_order:
        print_exit_message()
        return

    # 2. I-display ang Menu pag human og pili og 'y'
    print_menu()

    cart = []
    ordering = True

    while ordering:
        # 3. Prompt nga "Enter Choice (1-12):"
        while True:
            try:
                item_id = int(input("\nEnter Choice (1-12): "))
                if item_id in MENU:
                    break
                print_error_message("id_range")
            except ValueError:
                print_error_message("value_error")

        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity > 0:
                    break
                print_error_message("qty_range")
            except ValueError:
                print_error_message("value_error")

        selected_item = MENU[item_id]
        cart.append({
            "name": selected_item["name"],
            "price": selected_item["price"],
            "quantity": quantity
        })

        print_order_success(quantity, selected_item['name'])
        ordering = ask_yes_no("\nDo you want to order another item? (y/n): ")

    # 4. Receipt inig humana sa tanang order
    print_receipt(cart)

if __name__ == "__main__":
    main()