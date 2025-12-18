"""
QUESTION:
Create a function `xml_to_dict` that takes the root of an XML document as input and returns a dictionary where each key is the id of a book and the corresponding value is another dictionary containing the book's title, author, publish year, and price. 

Additionally, create two more functions: `add_book` that takes a dictionary of books, a book id, title, author, publish year, price, and optional description as input and adds a new book to the dictionary, and `modify_price` that takes a dictionary of books, a book id, and a new price as input and updates the price of the book with the given id.

The XML document is assumed to have the following structure:
```xml
<bookstore>
    <book id="id">
        <title>title</title>
        <author>author</author>
        <publish_year>year</publish_year>
        <price>price</price>
        <description>description</description> <!-- optional -->
    </book>
</bookstore>
```
The functions should handle cases where a book with the given id does not exist in the dictionary.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(root):
    result = {}
    for child in root:
        child_data = {grandchild.tag: grandchild.text for grandchild in child}
        result[child.attrib["id"]] = child_data
    return result

def add_book(books, id, title, author, publish_year, price, description=None):
    books[id] = {"title": title, "author": author, "publish_year": publish_year, "price": price}
    if description is not None:
        books[id]["description"] = description
    return books

def modify_price(books, id, new_price):
    book = books.get(id)
    if book is None:
        print(f"No book with id {id}.")
        return
    book["price"] = new_price
    return books