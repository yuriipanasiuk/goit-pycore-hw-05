from decorators.input_error import input_error

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    else:
        return f'Contact {name} not found in contacts list'