"""
QUESTION:
Write a function `validate_phone_number(phone_num, country)` that takes a phone number and a country as input and returns `True` if the phone number is valid according to the standard format of the given country, and `False` otherwise. The function should support the following countries: US, UK, India, Canada, and Australia. The standard formats for each country are: 
- US and Canada: XXX-XXX-XXXX
- UK: (XXXX) XXXX XXXX
- India: +91-XXXXXXXXXX
- Australia: (0X) XXXX XXXX
If the country is not one of the specified ones, the function should return `False`.
"""

import re

def validate_phone_number(phone_num, country):
    if country == 'US' or country == 'Canada':
        pattern = re.compile(r'^\+?1?\d{3}-\d{3}-\d{4}$')
    elif country == 'UK':
        pattern = re.compile(r'^(?:\+44)?\s?(\(?\d{4}\)?\s?\d{3,4}\s?\d{4})$')
    elif country == 'India':
        pattern = re.compile(r'^\+91-\d{10}$')
    elif country == 'Australia':
        pattern = re.compile(r'^\(\d{2}\)\s?\d{4}\s?\d{4}$')
    else:
        return False

    if pattern.match(phone_num):
        return True
    else:
        return False