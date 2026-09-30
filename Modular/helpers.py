from display import print_error_message

def ask_yes_no(prompt_message):
    while True:
        answer = input(prompt_message).strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        print_error_message("invalid_yes_no")