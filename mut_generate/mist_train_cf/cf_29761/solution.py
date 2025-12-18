"""
QUESTION:
You are given an array of integers representing candy weights, two pointers initially at the start and end of the array, and a goal to divide the candies equally between Alice and Bob by moving the pointers. Write a function `findEqualCandiesTotalNumber` that takes an array of candy weights and returns the total number of candies that can be equally divided between Alice and Bob. If it is not possible to divide the candies equally, return 0. The function should move the pointers and add the weights of the candies to find an equal division, if possible.
"""

from typing import List

def findEqualCandiesTotalNumber(candies_weights: List[int]) -> int:
    number_of_candies = len(candies_weights)
    alice_pos = 0
    bob_pos = number_of_candies - 1
    alice_current_weight = 0
    bob_current_weight = 0
    last_equal_candies_total_number = 0

    while alice_pos <= bob_pos:
        if alice_current_weight <= bob_current_weight:
            alice_current_weight += candies_weights[alice_pos]
            alice_pos += 1
        else:
            bob_current_weight += candies_weights[bob_pos]
            bob_pos -= 1

        if alice_current_weight == bob_current_weight:
            last_equal_candies_total_number = alice_current_weight + bob_current_weight

    return last_equal_candies_total_number