from decorators.input_error import input_error

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    
    name = args[0]
    
    if contacts.get(name):
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f'Contact {name} not found in contacts list'