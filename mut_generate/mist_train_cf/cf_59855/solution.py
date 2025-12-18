"""
QUESTION:
Write a function `categorized_counter` that takes a string `case` as input and returns a dictionary containing the maximum occurrence of each alphabet, number, and punctuation in the string. The function should categorize each character in the string into 'alphabet', 'number', or 'punctuation' and count the occurrence of each character in each category. The function should then filter the dictionary to only include characters with the maximum count in each category.
"""

def categorized_counter(case):
    count = {'alphabet': {}, 'number': {}, 'punctuation': {}}
    for char in case:
        if char == ' ':
            continue
        elif char.isalpha():
            char = char.lower()
            if char in count['alphabet']:
                count['alphabet'][char] += 1
            else:
                count['alphabet'][char] = 1
        elif char.isdigit():
            if char in count['number']:
                count['number'][char] += 1
            else:
                count['number'][char] = 1
        else:
            if char in count['punctuation']:
                count['punctuation'][char] += 1
            else:
                count['punctuation'][char] = 1

    max_alpha_count = max(count['alphabet'].values()) if count['alphabet'] else 0
    max_num_count = max(count['number'].values()) if count['number'] else 0
    max_punct_count = max(count['punctuation'].values()) if count['punctuation'] else 0

    count['alphabet'] = {key: value for key, value in count['alphabet'].items() if value == max_alpha_count}
    count['number'] = {key: value for key, value in count['number'].items() if value == max_num_count}
    count['punctuation'] = {key: value for key, value in count['punctuation'].items() if value == max_punct_count}

    return count