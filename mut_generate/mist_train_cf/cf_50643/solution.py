"""
QUESTION:
Write a function named `transform_and_count` that takes a list of integers as input. The function should remove all even digits from each integer, sort the remaining odd digits in descending order, and keep track of any repeated sequences among the resulting numbers. If an integer consists only of even digits, it should return 'None, all digits are even'. The function should output the list of transformed integers and a dictionary with repeated sequences and their counts.
"""

def transform_and_count(input_list):
    transformed_list = []
    rep_count = {}
    for number in input_list:
        number_str = str(number)
        number_str = ''.join([digit for digit in number_str if int(digit) % 2 != 0])
        final_number = ''.join(sorted(number_str, reverse=True))
        if final_number:
            transformed_list.append(int(final_number))
            if final_number in rep_count:
                rep_count[final_number] += 1
            else:
                rep_count[final_number] = 1
        else:
            transformed_list.append('None, all digits are even')
    return transformed_list, {k: v for k, v in rep_count.items() if v > 1}