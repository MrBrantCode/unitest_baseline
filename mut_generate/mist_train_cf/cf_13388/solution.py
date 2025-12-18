"""
QUESTION:
Create a function `print_combinations` that takes two integers `N` and `M` and prints all unique combinations of numbers that add up to `N` and are at most `M`. The function should not print duplicate combinations.
"""

def print_combinations(N, M):
    def backtrack(remaining_sum, current_combination):
        if remaining_sum == 0:
            print("+".join(str(num) for num in current_combination))
            return
        if len(current_combination) == 0:
            start_num = 1
        else:
            start_num = current_combination[-1]
        
        for num in range(start_num, min(remaining_sum, M) + 1):
            if num not in current_combination:
                backtrack(remaining_sum - num, current_combination + [num])
    
    backtrack(N, [])