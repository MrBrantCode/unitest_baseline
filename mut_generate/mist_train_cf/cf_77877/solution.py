"""
QUESTION:
Create a recursive function named `get_day` that takes an integer representing the day of the week (where Monday is 0 and Sunday is 6) and returns a dictionary with language as the key and the corresponding day of the week as the value. The function should support at least five languages. If the input integer is out of the range [0, 6], the function should return the corresponding day of the week by adjusting the input integer.
"""

def get_day(day, mapping=None):
    # If the given day is out of range, call itself again with a proper day
    if day < 0 or day > 6:
        return get_day(day % 7)

    # Initialize the mapping if it doesn't exist
    if mapping is None:
        mapping = {
            'English': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'Spanish': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
            'French': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
            'German': ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
            'Italian': ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
        }

    # Create a new dictionary to hold the results
    result = {}

    # For each language in the mapping, get the day of the week
    for language, days in mapping.items():
        result[language] = days[day]

    return result