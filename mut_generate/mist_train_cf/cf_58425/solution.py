"""
QUESTION:
Write a function named `calculate_interest` that takes a list of dictionaries as input. Each dictionary in the list should contain the keys 'Principal', 'Rate', and 'Time'. The function should calculate the compound interest for each dictionary using the formula `p * (1 + r/100) ** t - p` (where p is Principal, r is Rate, and t is Time), and return a list of dictionaries with the calculated interest added to each dictionary. Handle exceptions for missing keys and non-numeric values. The function should perform calculations yearly.
"""

def calculate_interest(data):
    results = []
    for item in data:
        try:    
            p = item['Principal']
            r = item['Rate']
            t = item['Time']
            i = p * ((1 + r/100) ** t) - p
            results.append({'Principal': p, 'Rate': r, 'Time': t, 'Interest': i})
        except KeyError:
            print('One of the dictionaries has missing keys.')
        except TypeError:
            print('Principal, Rate, and Time must be numbers.')
    return results