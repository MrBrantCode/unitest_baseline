"""
QUESTION:
Write a function `find_most_and_second_most_frequent` that finds the most frequent number and the second most frequent number greater than 100 in a list of integers between 1 and 10^6. The function should return a tuple containing the most frequent number and the second most frequent number. If there is a tie for the second most frequent number, return the smallest one. The function should have a time complexity of O(n) and a space complexity of O(m), where n is the number of elements in the list and m is the number of unique numbers greater than 100 in the list.
"""

def find_most_and_second_most_frequent(numbers):
    counter = {}
    max_freq = 0
    second_max_freq = 0
    most_freq_num = None
    second_most_freq_num = None
    
    for num in numbers:
        if num > 100:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            
            if counter[num] > max_freq:
                second_max_freq = max_freq
                second_most_freq_num = most_freq_num
                max_freq = counter[num]
                most_freq_num = num
            elif counter[num] > second_max_freq and counter[num] < max_freq:
                second_max_freq = counter[num]
                second_most_freq_num = num
            elif counter[num] == second_max_freq and num < second_most_freq_num:
                second_most_freq_num = num
    
    return (most_freq_num, second_most_freq_num)