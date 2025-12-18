"""
QUESTION:
Create a function `generate_html_table(numbers)` that takes a list of integers, generates an HTML table displaying the integers in ascending order with alternating background colors for each row, and highlights cells containing prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_html_table(numbers):
    numbers.sort()
    html = "<table>\n"
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            html += "  <tr style='background-color: #f2f2f2;'>\n"
        else:
            html += "  <tr>\n"
        if is_prime(num):
            html += f"    <td style='background-color: yellow;'>{num}</td>\n"
        else:
            html += f"    <td>{num}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html