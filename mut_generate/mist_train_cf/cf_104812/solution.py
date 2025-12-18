"""
QUESTION:
Create a function `get_day_of_week(day)` that takes a number representing a day of the week (1-7) as input and returns a tuple containing the corresponding day in English, Spanish, and French. Implement the function using if-else statements. If the input is invalid, return a tuple with "Invalid input" in all three languages.
"""

def get_day_of_week(day):
    if day == 1:
        return ("Monday", "Lunes", "Lundi")
    elif day == 2:
        return ("Tuesday", "Martes", "Mardi")
    elif day == 3:
        return ("Wednesday", "Miércoles", "Mercredi")
    elif day == 4:
        return ("Thursday", "Jueves", "Jeudi")
    elif day == 5:
        return ("Friday", "Viernes", "Vendredi")
    elif day == 6:
        return ("Saturday", "Sábado", "Samedi")
    elif day == 7:
        return ("Sunday", "Domingo", "Dimanche")
    else:
        return ("Invalid input", "Entrada inválida", "Entrée invalide")