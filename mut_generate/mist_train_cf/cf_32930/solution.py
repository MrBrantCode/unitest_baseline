"""
QUESTION:
Create a function `process_response(response_text)` that takes a string `response_text` as input and returns a dictionary with keys "po_number" and "pdf_url". The function should extract the purchase order number enclosed within `<po-number>` tags and the URL of a PDF file enclosed within `<link rel="artifact" href="...">` tags from the `response_text`. The function should also construct and return a database update query in the format `UPDATE manifest_links SET po_number = 'extracted_po_number', pdf_url = 'extracted_pdf_url' WHERE condition;`.
"""

import re

def process_response(response_text):
    po_number = re.search(r'<po-number>(.*?)</po-number>', response_text).group(1)
    pdf_url = re.search(r'<link rel="artifact" href="(.*?)"', response_text).group(1)
    
    # Construct dictionary
    result = {"po_number": po_number, "pdf_url": pdf_url}
    
    # Construct database update query
    update_query = f"UPDATE manifest_links SET po_number = '{po_number}', pdf_url = '{pdf_url}' WHERE condition;"
    
    return result, update_query