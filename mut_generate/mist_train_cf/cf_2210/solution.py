"""
QUESTION:
Implement a recursive function `generate_month_list` that takes two parameters: a list to store the generated month names and an integer to keep track of the current month. The function should return the list containing the full names of the 12 months in order, starting with January, without using any built-in functions or libraries, loops, or iteration methods.
"""

def generate_month_list(months_list, current_month):
    if current_month > 12:
        return months_list
    else:
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        months_list.append(months[current_month - 1])
        return generate_month_list(months_list, current_month + 1)