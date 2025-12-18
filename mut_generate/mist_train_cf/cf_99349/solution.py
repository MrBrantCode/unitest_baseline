"""
QUESTION:
Create a function `categorize_numbers(numbers)` that takes a list of integers `numbers` as input, categorize the numbers into four groups: positive even numbers, positive odd numbers, negative even numbers, and negative odd numbers. Calculate the sum and average of each group. The numbers in the input list range from -1000 to 1000.
"""

def categorize_numbers(numbers):
    pos_even = []
    pos_odd = []
    neg_even = []
    neg_odd = []
    pos_even_sum = pos_odd_sum = neg_even_sum = neg_odd_sum = 0
    pos_even_avg = pos_odd_avg = neg_even_avg = neg_odd_avg = 0.0
    
    for num in numbers:
        if num >= 0:
            if num % 2 == 0:
                pos_even.append(num)
                pos_even_sum += num
            else:
                pos_odd.append(num)
                pos_odd_sum += num
        else:
            if num % 2 == 0:
                neg_even.append(num)
                neg_even_sum += num
            else:
                neg_odd.append(num)
                neg_odd_sum += num
                
    if len(pos_even) > 0:
        pos_even_avg = pos_even_sum / len(pos_even)
    if len(pos_odd) > 0:
        pos_odd_avg = pos_odd_sum / len(pos_odd)
    if len(neg_even) > 0:
        neg_even_avg = neg_even_sum / len(neg_even)
    if len(neg_odd) > 0:
        neg_odd_avg = neg_odd_sum / len(neg_odd)
        
    return {
        'Positive Even': {'Numbers': pos_even, 'Sum': pos_even_sum, 'Average': pos_even_avg},
        'Positive Odd': {'Numbers': pos_odd, 'Sum': pos_odd_sum, 'Average': pos_odd_avg},
        'Negative Even': {'Numbers': neg_even, 'Sum': neg_even_sum, 'Average': neg_even_avg},
        'Negative Odd': {'Numbers': neg_odd, 'Sum': neg_odd_sum, 'Average': neg_odd_avg},
    }