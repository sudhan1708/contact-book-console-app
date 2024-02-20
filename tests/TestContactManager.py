import unittest
import os
import json

from app.ContactManager import *


class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Create a temporary contacts JSON file for testing
        self.filename = '/Users/sudhan.b/PycharmProjects/contact-book-app/tests/test_contacts.json'
        self.test_data = [
            {"name": "John", "email": "john@example.com", "phone": "1234567890", "address": "123 Main St",
             "tag": "friend"},
            {"name": "Alice", "email": "alice@example.com", "phone": "9876543210", "address": "456 Elm St",
             "tag": "family"}
        ]
        with open(self.filename, 'w') as file:
            json.dump(self.test_data, file)

        # Initialize the ContactManager with the temporary contacts file
        self.contact_manager = ContactManager(self.filename)

    def test_add_contact(self):
        new_contact = {"name": "Bob", "email": "bob@example.com", "phone": "1112223333", "address": "789 Oak St",
                       "tag": "work"}
        self.contact_manager.add_contact(new_contact)

        # Verify that the contact was added
        self.assertIn(new_contact, self.contact_manager.contacts)

    def test_search_contact_by_name(self):
        result = self.contact_manager.search_contact_by_name("John")
        expected_result = {"name": "John", "email": "john@example.com", "phone": "1234567890", "address": "123 Main St",
                           "tag": "friend"}
        self.assertEqual(result, expected_result)

    def test_search_contact_by_phone_number(self):
        result = self.contact_manager.search_contact_by_phone_number("9876543210")
        expected_result = {"name": "Alice", "email": "alice@example.com", "phone": "9876543210",
                           "address": "456 Elm St", "tag": "family"}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
