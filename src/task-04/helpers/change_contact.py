"""
Module for managing contacts.

Provides functions for adding, changing, and retrieving contacts.
"""

from decorators.input_error import input_error


@input_error
def change_contact(args, contacts):
    """Change the phone number of an existing contact."""

    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."

    return f"Contact {name} not found in contacts list"
