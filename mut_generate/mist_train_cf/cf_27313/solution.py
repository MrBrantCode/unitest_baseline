"""
QUESTION:
Write a function `calculate_and_format_average(nums)` that takes a list of integers `nums` with a length between 0 and 1000 (inclusive), calculates the average, and formats the average into two specified string formats. The first string should contain the average value right-aligned within a 12-character wide field. The second string should contain the average value rounded to two decimal places and displayed with exactly two digits after the decimal point, right-aligned within a 12-character wide field. The function should return these two formatted strings. If the input list is empty, return two empty strings, each 12 characters wide.
"""

def calculate_and_format_average(nums):
    if not nums:
        return (' '*12, ' '*12)  
    average = sum(nums) / len(nums)
    formatted_avg = "%12d" % int(average)  
    rounded_avg = "%12.2f" % average  
    return (formatted_avg, rounded_avg)