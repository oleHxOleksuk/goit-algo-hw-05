from function_chat import add_contact,show_all,show_phone,change_contact

CLOSE_EXIT = ("close", "exit")
HELLO = ("hello")
ALL = ("all")
ADD = ("add")
CHANGE = ("change")
PHONE = ("phone")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in CLOSE_EXIT:
            print("Good bye!")
            break
        elif command == HELLO:
            print("How can I help you?")
        elif command == ADD:
            print(add_contact(args, contacts))
        elif command == ALL:
            print(show_all(contacts))
        elif command == PHONE:
            print(show_phone(args, contacts))
        elif command == CHANGE:
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()