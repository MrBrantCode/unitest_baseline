"""
QUESTION:
Write a function `custom_list` that takes a list `l` and an integer `k` as inputs. If `l` is empty, return a list containing `k`. If `k` is negative, remove the `k`th element from the end of `l`. If `k` is non-negative and less than the length of `l`, remove the `k`th element from `l`. If `k` is greater than or equal to the length of `l`, return `l` in reverse order.
"""

def custom_list(l, k):
    # If l is an empty list, return [k]
    if not l:
        return [k]
    # If k is negative, remove the k'th element from the end
    elif k < 0:
        if abs(k) > len(l):
            return l[::-1]
        else:
            return l[:k] + l[k+1:]
    # If k is non-negative and doesn't surpass the list's length, remove the k'th element
    elif k < len(l):
        return l[:k] + l[k+1:]
    # If k surpasses the list's length, return the list in reverse order
    else:
        return l[::-1]