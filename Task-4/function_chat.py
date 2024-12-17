from decorators import input_error

@input_error
def add_contact(args:list, contacts:dict):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_all(contacts:dict):
    if contacts:
        all_contact = "Contcts:"
        for name,phone in contacts.items():
            all_contact += f"\n{name}:{phone}"
        return all_contact
    else:
        return "Is not contacts"

@input_error
def show_phone(args:list, contacts:dict):
    name = args[0]
    if name not in contacts:
        return "Contact does not exist"
    else:
        return contacts[name]

@input_error   
def change_contact(args:list, contacts:dict):
    if contacts:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Contact {name} updated number {phone}."
        else:
            return "Contact does not exist"