"""
QUESTION:
Write two functions, `add_even_odd_elements(my_list, n)` and `max_sum_non_consecutive(my_list)`, that take a list of integers `my_list` and its length `n` as input. 

In `add_even_odd_elements(my_list, n)`, add the elements at even indices to the elements at odd indices and return the total sum. 

In `max_sum_non_consecutive(my_list)`, find the maximum sum of non-consecutive elements that can be obtained from the list. 

The function `add_even_odd_elements(my_list, n)` should print the total sum of elements at even indices added to elements at odd indices. The function `max_sum_non_consecutive(my_list)` should print the maximum sum of non-consecutive elements.
"""

def add_even_odd_elements(my_list, n):
    even_sum = 0
    odd_sum = 0
    
    for i in range(n):
        if i % 2 == 0:  # even index
            even_sum += my_list[i]
        else:  # odd index
            odd_sum += my_list[i]
    
    return even_sum + odd_sum


def max_sum_non_consecutive(my_list):
    if len(my_list) == 0:
        return 0
    elif len(my_list) == 1:
        return my_list[0]
    elif len(my_list) == 2:
        return max(my_list[0], my_list[1])
    
    dp = [0] * len(my_list)
    dp[0] = my_list[0]
    dp[1] = max(my_list[0], my_list[1])
    
    for i in range(2, len(my_list)):
        dp[i] = max(dp[i-1], dp[i-2] + my_list[i])
    
    return dp[-1]