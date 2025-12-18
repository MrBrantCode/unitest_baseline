"""
QUESTION:
Write a function named `generate_formatted_address` that takes seven parameters: `org_name`, `dept_name`, `street_address`, `city`, `postal_code`, `phone_number`, and `email`. The function should return a string representing the formatted address in the following format:

`<Organization Name>
<Department Name>
<Street Address>, <City> <Postal Code>
Tel: <Phone Number>
Email: <Email Address>`

The input parameters are all strings. There are no specific restrictions on the input values.
"""

def generate_formatted_address(org_name, dept_name, street_address, city, postal_code, phone_number, email):
    formatted_address = f"{org_name}\n{dept_name}\n{street_address}, {city} {postal_code}\nTel: {phone_number}\nEmail: {email}"
    return formatted_address