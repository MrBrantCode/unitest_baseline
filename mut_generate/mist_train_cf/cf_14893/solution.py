"""
QUESTION:
Create a class named `FrequencyTable` that takes an array of numbers as input and returns a sorted frequency table in descending order based on count. The frequency table should include both the count and the percentage of each number in the array. The input array can contain both integers and floating-point numbers.
"""

def entrance(numbers):
    frequency_table = {}
    total_count = len(numbers)

    for number in numbers:
        if number in frequency_table:
            frequency_table[number] += 1
        else:
            frequency_table[number] = 1

    for number, count in frequency_table.items():
        percentage = (count / total_count) * 100
        frequency_table[number] = {'count': count, 'percentage': percentage}

    sorted_table = sorted(frequency_table.items(), key=lambda x: x[1]['count'], reverse=True)
    return sorted_table