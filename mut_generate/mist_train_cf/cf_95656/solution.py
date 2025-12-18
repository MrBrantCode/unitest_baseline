"""
QUESTION:
Design a data structure in Python to store customer contact details, where each customer can have multiple contact numbers and email addresses associated with them. Implement a function `get_customers_by_email_domain` that retrieves all customers who have a specific email domain. The `get_customers_by_email_domain` function should take a list of customer objects and a domain as input and return a list of customer names who have emails with the specified domain.
"""

class Customer:
    def __init__(self, name):
        self.name = name
        self.emails = []
        self.numbers = []

    def add_email(self, email):
        self.emails.append(email)
        
    def add_number(self, number):
        self.numbers.append(number)


def get_customers_by_email_domain(customers, domain):
    customers_with_domain = []
    for customer in customers:
        for email in customer.emails:
            if domain in email:
                customers_with_domain.append(customer.name)
    return customers_with_domain