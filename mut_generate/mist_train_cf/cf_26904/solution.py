"""
QUESTION:
Create a function named `generate_links` that takes a list of addresses as input and returns a list of links. Each link should be formed by appending an address to a base URL 'https://bcy.net'. The function should have the signature `def generate_links(adrs: list) -> list`.
"""

def generate_links(adrs: list) -> list:
    adress_link = []
    for adr in adrs:
        adress_link.append('https://bcy.net' + adr)
    return adress_link