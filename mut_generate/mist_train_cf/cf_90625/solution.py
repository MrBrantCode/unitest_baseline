"""
QUESTION:
Write a function `find_most_frequent_numbers` that takes a list of integers as input and returns the most frequent number greater than 100, the second most frequent number greater than 100 (in case of a tie, return the smallest one), and the count of each unique number greater than 100 in descending order of frequency (in case of a tie, return them in ascending order). The function should have a time complexity of O(n) and a space complexity of O(m), where n is the number of elements in the list and m is the number of unique numbers greater than 100 in the list.
"""

def find_most_frequent_numbers(numbers):
    count = {}
    for num in numbers:
        if num > 100:
            count[num] = count.get(num, 0) + 1

    max_freq = 0
    second_max_freq = 0
    most_freq_num = None
    second_most_freq_num = None

    for num, freq in count.items():
        if freq > max_freq:
            second_max_freq = max_freq
            max_freq = freq
            second_most_freq_num = most_freq_num
            most_freq_num = num
        elif freq > second_max_freq:
            second_max_freq = freq
            second_most_freq_num = num

    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    return most_freq_num, second_most_freq_num, sorted_count