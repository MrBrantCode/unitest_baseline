"""
QUESTION:
Write a function called `parse_xml_to_json(xml_string)` that takes a string representing an XML document and returns a JSON string. The XML document may have multiple levels of nested elements, and you should properly represent this nesting in the JSON string. The function should be able to handle any structure of XML, not just the one provided in the example.
"""

import xml.etree.ElementTree as ET
import json

def parse_xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    library = {}

    sections = []
    for section_elem in root.find('sections').findall('section'):
        section = {}
        section['name'] = section_elem.find('name').text

        books = []
        for book_elem in section_elem.find('books').findall('book'):
            book = {}
            book['title'] = book_elem.find('title').text
            book['author'] = book_elem.find('author').text
            book['year'] = book_elem.find('year').text

            genres = []
            for genre_elem in book_elem.find('genres').findall('genre'):
                genres.append(genre_elem.text)
            book['genres'] = genres

            books.append(book)
        section['books'] = books

        magazines = []
        for magazine_elem in section_elem.find('magazines').findall('magazine'):
            magazine = {}
            magazine['title'] = magazine_elem.find('title').text
            magazine['issue'] = magazine_elem.find('issue').text
            magazines.append(magazine)
        section['magazines'] = magazines

        sections.append(section)
    library['sections'] = sections

    return json.dumps({'library': library}, indent=2)