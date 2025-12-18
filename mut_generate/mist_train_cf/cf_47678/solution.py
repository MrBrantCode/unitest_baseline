"""
QUESTION:
Construct a function named `maximum_swaps` that takes two parameters, a string of digits `num` and the number of swaps `k`, and returns the maximum possible number that can be formed by swapping at most `k` pairs of digits in `num`. The function should prioritize choosing the left-most pair if multiple pairs result in equal maximum numbers, and return the original number string if the length of the string or the number of swaps cannot form a pair.
"""

def maximum_swaps(num, k):
    # Convert num into a list because strings are immutable
    num = list(str(num))
  
    # For each digit check if there exists any digit on right side, which is greater than this digit
    for i in range(len(num)):
        # Check only if number of swaps allowed is greater than 0
        if k <= 0:
            break
  
        max_digit_idx = i
        for j in range(i+1, len(num)):
            # If digit is greater and it's index is smaller than max digit found
            # Then update max_digit and its index
            if num[j] >= num[max_digit_idx]:
                max_digit_idx = j
  
        # Swap only when max_digit is greater than current digit
        if num[i] < num[max_digit_idx]:
            num[i], num[max_digit_idx] = num[max_digit_idx], num[i]
            k -= 1  # Decrease the swap count
              
    return "".join(num)