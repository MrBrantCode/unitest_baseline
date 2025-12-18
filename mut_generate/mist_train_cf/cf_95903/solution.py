"""
QUESTION:
Write a function `generateLink` that takes two parameters, `baseUrl` and `product`, and returns a link in the format `baseUrl/product`. The function should convert both `baseUrl` and `product` to lowercase and URL-encode any special characters in `product`. It should also check if either `baseUrl` or `product` is an empty string, and if so, return an error message. Additionally, it should keep track of the number of times a link is generated and check if the generated link is already in use. The function should return an error message if the link is already in use.
"""

import urllib.parse

existingLinks = set()
numGeneratedLinks = 0

def generateLink(baseUrl, product):
    global numGeneratedLinks
    numGeneratedLinks += 1

    if baseUrl == "" or product == "":
        return "Error: Base URL and product cannot be empty."

    url = baseUrl.lower() + "/" + urllib.parse.quote(product.lower())

    if url in existingLinks:
        return "Error: Link already in use."

    existingLinks.add(url)

    return url