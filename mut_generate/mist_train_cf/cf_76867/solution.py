"""
QUESTION:
Write a function `will_it_fly(q, w, g)` that calculates the probability of an object `q` to fly. The function takes three parameters: `q`, a list of integers representing the object's weights; `w`, the maximum possible weight; and `g`, the gravity factor. The object has a higher probability to fly if it is balanced (i.e., its weights are palindromic) and the sum of its elements is less than `w`. The function should also consider the effect of gravity `g` on the probability of flying.
"""

def will_it_fly(q, w, g):
    total_weight = sum(q)
    if total_weight > w:
        return 0
    elif q == q[::-1] and total_weight < w:
        if total_weight < g:
            return 1
        else:
            probability = (w-total_weight)/(g-total_weight)
            return probability
    else:
        return 0.4