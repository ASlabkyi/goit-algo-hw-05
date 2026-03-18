from functools import wraps

def input_error(msg):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                return msg
            except KeyError:
                return "Contact not found."
        return wrapper
    return decor

def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

@input_error("Input error! Use format: cmd name number.")
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exist. Please use 'change' to change your phone number."
    contacts[name] = phone
    return "Contact added."

@input_error("Input error! Use format: cmd name number.")
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."

@input_error("Input error! Use format: cmd name.")
def contact_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error("No contacts found.")
def show_all_contacts(contacts):
    if not contacts:
        raise ValueError
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(contact_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()