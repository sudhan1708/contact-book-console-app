# Press the green button in the gutter to run the script.
from ContactManager import *
from utils.utils import *

import yaml
import os


def main():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    json_file_path = config.get("json_file_name")
    contact_manager = ContactManager(json_file_path)

    while True:
        print("\n Contact Book Application \n")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Filter by tags")
        print("7. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = get_name(contact_manager)
            email = get_email()
            phone = get_phone_number()

            #optional inputs
            address = input("Enter address: ")
            tag = input("Enter tag: ")

            contact = {'name': name, 'email': email, 'phone': phone, 'address': address, 'tag': tag}
            # duplicate contacts will be handled by adding it into a set
            contact_manager.add_contact(contact)
            print("Contact added successfully!!!")

        elif choice == '2':
            name = input("Enter the name to search: ")
            contact = contact_manager.search_contact_by_name(name)
            if contact:
                print("Contact found")
                print("Name:", contact['name'])
                print("Email:", contact['email'])
                print("Phone:", contact['phone'])
                print("Address:", contact['address'])
            else:
                print("Contact not found!!! Please search for different name")

        elif choice == '3':
            # updating based on phone number as it is unique
            phone = input("Enter phone_number of the contact to update: ")
            contact = contact_manager.search_contact_by_phone_number(phone)
            if contact:
                new_name = get_name(contact_manager)
                new_email = get_email()
                new_phone = get_phone_number()
                new_address = input("Enter address: ")
                new_tag = input("Enter tag: ")
                new_contact = {'name': new_name, 'email': new_email, 'phone': new_phone, 'address': new_address,
                               'tag': new_tag}
                if contact_manager.update_contact(phone, new_contact):
                    print("Contact updated successfully!")
                else:
                    print("Failed to update contact.")
            else:
                print("Contact not found!!!!")

        elif choice == '4':
            name = input("Enter name to delete: ")
            if contact_manager.delete_contact(name):
                print("Contact deleted successfully!")
            else:
                print("Failed to delete contact.")

        elif choice == '5':
            contact_manager.list_contacts()

        elif choice == '6':
            tag = input("Enter tag to filter: ")
            contact_manager.filter_by_tag(tag)

        elif choice == '7':
            print("Exiting the application...........")
            break

        else:
            print("Invalid choice. Please enter a valid option listed above.")


if __name__ == '__main__':
    main()
