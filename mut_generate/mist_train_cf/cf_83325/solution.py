"""
QUESTION:
Create a function `count_and_freq` that takes a list of elements as input and returns a dictionary containing the frequency of distinct strings that start with the letter 'a' (case insensitive). The function should ignore non-string elements in the list and treat 'Apple' and 'apple' as distinct strings. The function should also handle potential errors without interrupting its functionality.
"""

def count_and_freq(lst):
    freq_dict = {}
    for element in lst:
        try:
            if element[0].lower() == 'a':
                if element in freq_dict:
                    freq_dict[element] += 1
                else:
                    freq_dict[element] = 1
        except TypeError:  
            continue  
        except IndexError:  
            continue

    return freq_dict