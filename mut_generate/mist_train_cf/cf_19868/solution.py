"""
QUESTION:
Design a data structure to store customer information including name, address, phone number, and a list of previous purchases, where the customer information can be efficiently searched and retrieved based on the phone number. The data structure should support efficient search, retrieval, update, and deletion operations.
"""

class Customer:
    def __init__(self, name, address, phone_number, purchases=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.purchases = purchases if purchases is not None else []

class CustomerDatabase:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.phone_number] = customer

    def get_customer(self, phone_number):
        return self.customers.get(phone_number)

    def update_customer(self, phone_number, name=None, address=None, purchases=None):
        customer = self.get_customer(phone_number)
        if customer:
            if name:
                customer.name = name
            if address:
                customer.address = address
            if purchases:
                customer.purchases = purchases

    def delete_customer(self, phone_number):
        if phone_number in self.customers:
            del self.customers[phone_number]

def entrance(name, address, phone_number, purchases=None):
    customer = Customer(name, address, phone_number, purchases)
    database = CustomerDatabase()
    database.add_customer(customer)
    return database