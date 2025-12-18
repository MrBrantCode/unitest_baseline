"""
QUESTION:
Implement a function named `moeda_resumo` that takes three parameters: `valor`, `largura`, and `altura`, representing the transaction amount, width, and height of the summary output respectively. The function should generate a visual summary of the transaction using a grid of characters, where each character represents a unit of currency. Each cell in the grid should be filled with a '$' symbol if the transaction amount has units remaining, and a space otherwise. The function should return the visual summary grid as a string.
"""

def moeda_resumo(valor, largura, altura):
    # Calculate the number of currency units to be displayed
    currency_units = int(valor)

    # Create the visual summary grid
    summary_grid = ""
    for _ in range(altura):
        row = ""
        for _ in range(largura):
            if currency_units > 0:
                row += "$"
                currency_units -= 1
            else:
                row += " "
        summary_grid += row + "\n"

    return summary_grid