"""
QUESTION:
Write a function `extract_bold_text` that takes an HTML code string as input and returns a list of strings representing the bold text within the HTML code. The function should identify all occurrences of bold text, handle nested HTML tags within the bold tags, and extract the bold text even if it is surrounded by other HTML tags. The function should not use any built-in HTML parsing libraries or functions.
"""

def extract_bold_text(html_code):
    bold_texts = []
    start_tag = "<b>"
    end_tag = "</b>"
    start_index = 0

    while True:
        start = html_code.find(start_tag, start_index)
        end = html_code.find(end_tag, start_index)
        if start == -1 or end == -1:
            break

        start_index = end + len(end_tag)
        bold_text = html_code[start + len(start_tag):end]
        bold_texts.append(bold_text)

    return bold_texts