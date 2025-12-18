"""
QUESTION:
Create a function `calculate_frequencies_and_averages` that takes an array of integers as input and returns the frequency and average of even, odd, and zero numbers. The function should run in O(n) time complexity. The average of zero numbers should be considered as "Not applicable". If there are no even or odd numbers in the array, the average should be reported as "No even numbers" or "No odd numbers" respectively.
"""

def calculate_frequencies_and_averages(arr):
    even_count = 0
    even_sum = 0
    odd_count = 0
    odd_sum = 0
    zero_count = 0
    
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num % 2 == 0:
            even_count += 1
            even_sum += num
        else:
            odd_count += 1
            odd_sum += num
    
    even_avg = even_sum/even_count if even_count else "No even numbers"
    odd_avg = odd_sum/odd_count if odd_count else "No odd numbers"
    zero_avg = "Not applicable" 

    return {"Even": {"Frequency": even_count, "Average" : even_avg}, 
            "Odd": {"Frequency": odd_count, "Average" : odd_avg},
            "Zero": {"Frequency": zero_count, "Average" : zero_avg}}