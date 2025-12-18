"""
QUESTION:
Create a function named `convert_to_text_orig_unicode` that takes a list of strings as input and converts each string to the "text-orig-unicode" format. The format represents numerals with repeats by placing that many copies of the corresponding Cuneiform Unicode character. The function should return a list of the converted strings.

The Cuneiform Unicode characters for numerals are: 
"1" -> "𐏑",
"2" -> "𐏁",
"3" -> "𐏂",
"4" -> "𐏃",
"5" -> "𐏄".
"""

def convert_to_text_orig_unicode(lines):
    cuneiform_numerals = {
        "1": "𐏑",
        "2": "𐏁",
        "3": "𐏂",
        "4": "𐏃",
        "5": "𐏄",
    }
    
    converted_lines = []
    for ln in lines:
        converted_ln = ""
        for char in ln:
            if char.isdigit():
                converted_ln += cuneiform_numerals[char] * int(char)
            else:
                converted_ln += char
        converted_lines.append(converted_ln)
    
    return converted_lines