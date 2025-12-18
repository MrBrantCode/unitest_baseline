"""
QUESTION:
Write a function `stable_flight(q, w, k)` that takes in a list of integers `q`, a maximum weight `w`, and a threshold `k`. The function should return `True` if `q` can attain a stable flying state and `False` otherwise. A stable flying state is achieved if the following conditions are met: the list `q` is a palindrome, the sum of its elements does not exceed `w`, and no element in the list exceeds `k`.
"""

def stable_flight(q, w, k):
    # Check whether q is a palindrome
    if q != q[::-1]:
        return False
    # Check whether sum of elements in q doesn't exceed w
    elif sum(q) > w:
        return False
    # Check whether no element in q exceeds k
    elif any(i > k for i in q):
        return False
    # If q satisfies all conditions, return True
    else:
        return True