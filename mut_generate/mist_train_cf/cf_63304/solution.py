"""
QUESTION:
Write a function `kEmptySlots` that determines the earliest day on which there exist two illuminated bulbs with exactly `k` unlit bulbs situated between them. The function takes two parameters: `bulbs` (a list of integers representing the order in which bulbs are turned on) and `k` (an integer representing the number of unlit bulbs between the two illuminated bulbs). The function should return the earliest day on which the condition is met, or `-1` if no such day exists.

Restrictions: `1 <= len(bulbs) <= 2 * 10^4`, `1 <= bulbs[i] <= n`, `bulbs` is a permutation of numbers from `1` to `n`, and `0 <= k <= 2 * 10^4`.
"""

def kEmptySlots(bulbs, k):
    days = [0] * len(bulbs)
    for day, position in enumerate(bulbs):
        days[position - 1] = day + 1

    left, right, res = 0, k + 1, float('inf')

    for i in range(1, len(bulbs)):
        if i + k + 1 < len(bulbs) and days[i] < max(days[left], days[i + k + 1]):
            if i == right:
                res = min(res, max(days[left], days[i + k + 1]))
            left, right = i, k + 1 + i
        elif right == len(bulbs) - 1:
            break

    return res if res < float('inf') else -1