"""
QUESTION:
Create a function called "generateLink" that takes two parameters, "baseUrl" and "product", and returns a generated link by combining these two parameters with a forward slash in between. The function must meet the following requirements:
- The function should handle cases where either "baseUrl" or "product" is an empty string and return an error message.
- The generated link must be in lowercase characters only.
- The function should check if the generated link is already in use and return an error message if it is.
- The function should handle special characters in the "product" variable and replace them with their corresponding URL-encoded values.
- The function should track the number of times the link is generated and return it as a separate variable called "numGeneratedLinks".
"""

import urllib.parse

numGeneratedLinks = 0
existingLinks = set()

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