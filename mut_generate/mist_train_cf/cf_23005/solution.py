"""
QUESTION:
Write a function `sum_greater_than_10` that recursively sums all unique integers greater than 10 in a list, where the integers are also divisible by 7. The function should use tail recursion and have a time complexity of O(n). The input list contains at least 20 elements.
"""

def sum_greater_than_10(lst):
    def sum_helper(lst, total_sum, seen):
        if not lst:
            return total_sum
        else:
            current = lst[0]
            rest = lst[1:]

            if current > 10 and current % 7 == 0 and current not in seen:
                return sum_helper(rest, total_sum + current, seen | {current})
            else:
                return sum_helper(rest, total_sum, seen)

    return sum_helper(lst, 0, set())