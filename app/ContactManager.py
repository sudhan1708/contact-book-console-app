import json
import sys
import os


class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        self.filename = os.path.join(os.path.dirname(__file__), 'datastore', self.filename)
        try:
            with open(self.filename, 'r') as file:
                contacts = json.load(file)
        except FileNotFoundError:
            sys.exit("Json file not found. Please check the file path.")

        return contacts

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact)
        # Convert each JSON object to a string and add it to a set to handle duplicate contacts
        unique_json_strings = set(json.dumps(contact) for contact in self.contacts)
        self.contacts = [json.loads(obj_str) for obj_str in unique_json_strings]
        self.save_contacts()

    def search_contact_by_name(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                return contact
        return None

    def search_contact_by_phone_number(self, phone):
        for contact in self.contacts:
            if contact['phone'].lower() == phone.lower():
                return contact
        return None

    def update_contact(self, phone, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact['phone'].lower() == phone.lower():
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact['name'].lower() == name.lower():
                del self.contacts[i]
                self.save_contacts()
                return True
        return False

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("List of Contacts \n")
            for contact in self.contacts:
                print("Name:", contact['name'])
                print("Email:", contact['email'])
                print("Phone:", contact['phone'])
                print("Address:", contact['address'])
                print("Tag:", contact['tag'])
                print("\n")

    def filter_by_tag(self, tag):
        tag_found = False
        for contact in self.contacts:
            if contact['tag'].lower() == tag.lower():
                tag_found = True
                print("Name:", contact['name'])
                print("Email:", contact['email'])
                print("Phone:", contact['phone'])
                print("Address:", contact['address'])
                print("Tag:", contact['tag'])
                print("\n")
        if not tag_found:
            print("No contacts found with the tag:", tag)
