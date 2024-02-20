import re


def is_email_valid(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


# Condition for valid phone number
# 1) Begins with 0 or 91
# 2) Then contains 6,7 or 8 or 9.
# 3) Then contains 9 digits
def is_phone_number_valid(phone_number):
    Pattern = re.compile("^(\+\d{1,2}\s?)?((\(\d{3}\))|\d{3})[-\s]?\d{3}[-\s]?\d{4}$")
    return Pattern.match(phone_number)


def get_name(contact_manager):
    name = input("Enter name: ")
    while len(name) == 0:
        print("Name cannot be empty!!!")
        name = input("Enter name: ")
    # check whether contact name already exists
    while contact_manager.search_contact_by_name(name) is not None:
        print("contact name already exists. Please enter a new name.")
        name = input("Enter name: ")

    return name


def get_email():
    email = input("Enter email: ")
    # check whether email is in proper format
    while not is_email_valid(email):
        print("Please enter a valid email!!!!!")
        email = input("Enter email: ")
    return email


def get_phone_number():
    # check phone number is valid or not
    phone_number = input("Enter phone number: ")
    while not is_phone_number_valid(phone_number):
        print("Please enter a valid phone number")
        phone = input("Enter phone number: ")

    return phone_number
