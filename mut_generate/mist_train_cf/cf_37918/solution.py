"""
QUESTION:
Create a function `extract_member_info` that takes an HTML snippet as input and returns a dictionary containing the values of "Jurusan", "Tanggal Lahir", and "Jenis Kelamin" attributes. The function should extract these values from the HTML snippet and store them in a structured format. The HTML snippet contains rows and columns where each row represents a different attribute of a member. The function should be able to handle HTML snippets with the same structure as the given example.
"""

import re

def extract_member_info(html_snippet):
    member_info = {}
    matches = re.findall(r'<td class="textt">(.*?)<\/td>\s*<td.*?>(.*?)<\/td>', html_snippet)
    for match in matches:
        attribute, value = match
        member_info[attribute] = value.strip()
    return member_info