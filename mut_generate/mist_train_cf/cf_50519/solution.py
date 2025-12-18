"""
QUESTION:
Create a function `sort_numbers` that takes a string of space-separated word numerals from "zero" to "nine", converts these words to their corresponding numeric forms, sorts them in ascending order, and then converts them back to word form. The function should return the original string with the word numerals in sorted order.
"""

def sort_numbers(numbers):
    word_to_num = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    num_to_word = {v: k for k, v in word_to_num.items()}
    
    nums = [word_to_num[word] for word in numbers.split()]
    nums.sort()
    
    return ' '.join(num_to_word[num] for num in nums)