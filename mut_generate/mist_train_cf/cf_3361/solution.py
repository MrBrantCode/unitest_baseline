"""
QUESTION:
Write a function named `extract_bold_text(html_code)` that takes a string `html_code` as input and returns a list of bold text extracted from the HTML code. The function should not use any built-in HTML parsing libraries or functions and should handle cases with multiple occurrences of bold text, nested HTML tags within bold tags, and bold text surrounded by other HTML tags.
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