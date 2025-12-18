"""
QUESTION:
Create a function called `determine_language` that takes a string as input and determines the most likely language of the string, choosing from English, Greek, or Russian, based on the characters present in the string.
"""

def determine_language(text):
    english = "abcdefghijklmnopqrstuvwxyz"
    greek = "αβγδεζηθικλμνξοπρστυφχψω"
    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    counter_en = 0
    counter_gr = 0
    counter_ru = 0

    for char in text.lower():
        if char in english:
            counter_en += 1
        elif char in greek:
            counter_gr += 1
        elif char in russian:
            counter_ru += 1

    if counter_en > counter_gr and counter_en > counter_ru:
        return "The text is most likely in English."
    elif counter_gr > counter_en and counter_gr > counter_ru:
        return "The text is most likely in Greek."
    elif counter_ru > counter_en and counter_ru > counter_gr:
        return "The text is most likely in Russian."
    else:
        return "The text could not be identified confidently."