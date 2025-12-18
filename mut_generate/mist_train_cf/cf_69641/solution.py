"""
QUESTION:
Create a function named 'categorized_counter' that takes a string composed of diverse characters (uppercase and lowercase alphabets, numbers, and punctuations) partitioned by spaces. The function should output a dictionary showcasing the most frequent character and its count from each category, with alphabets treated in lowercase. In case a category has multiple characters with similar counts, all should be listed. 

The input string may contain any combination of uppercase and lowercase alphabets, numbers, and punctuation marks. It should ignore whitespace characters and handle alphabets in both uppercase and lowercase forms. The function should also handle cases where a category has no characters. 

The function should return a dictionary with three keys: 'alphabet', 'number', and 'punctuation'. The values of these keys are dictionaries where the keys are the most frequent characters in each category and the values are their respective counts.
"""

def categorized_counter(s):
    count = {'alphabet': {}, 'number': {}, 'punctuation': {}}
    for char in s:
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