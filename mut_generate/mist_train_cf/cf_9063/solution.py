"""
QUESTION:
Write a function called `parse_json_price` that takes a JSON string as input and returns the value of the 'price' variable as a float without using any built-in JSON parsing functions or libraries. The input JSON string is a valid JSON object with the 'price' variable as a float value.
"""

def parse_json_price(json_str):
    price_index = json_str.find('"price":')
    comma_index = json_str.find(',', price_index)
    price_str = json_str[price_index+len('"price":'):comma_index]
    price_str = price_str.strip()
    return float(price_str)