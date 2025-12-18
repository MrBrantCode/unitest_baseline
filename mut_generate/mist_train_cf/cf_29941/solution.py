"""
QUESTION:
Write a function called `cancellation_analysis` that takes a pandas DataFrame `tabela` as input, where `tabela` contains a column named "Categoria". The function should return a report in the form of a dictionary where the keys are the unique categories in the "Categoria" column, and the values are tuples containing the count of customers and the percentage of customers in each category. The percentage should be rounded to two decimal places.
"""

import pandas as pd

def cancellation_analysis(tabela):
    quantidade_categoria = tabela["Categoria"].value_counts()  
    quantidade_categoria_percentual = tabela["Categoria"].value_counts(normalize=True)  

    report = {}
    for category, count in quantidade_categoria.items():
        percentage = quantidade_categoria_percentual.get(category, 0) * 100  
        report[category] = (count, round(percentage, 2))  

    return report