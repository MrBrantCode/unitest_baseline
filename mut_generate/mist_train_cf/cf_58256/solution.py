"""
QUESTION:
Write a function `count_subcommittees(n, committee_size, subcommittee_size)` that calculates the total number of different possible subcommittees of `subcommittee_size` people that can be formed within a main committee of `committee_size` people, chosen from an initial group of `n` people. The function should use the combination formula `C(n, k) = n! / [(n-k)! * k!]` to calculate combinations and return the total number of subcommittees.
"""

import math

def count_subcommittees(n, committee_size, subcommittee_size):
    """
    Calculate the total number of different possible subcommittees of subcommittee_size people 
    that can be formed within a main committee of committee_size people, chosen from an initial 
    group of n people.

    Args:
        n (int): The initial group of people.
        committee_size (int): The size of the main committee.
        subcommittee_size (int): The size of the subcommittee.

    Returns:
        int: The total number of subcommittees.
    """
    main_committee = math.comb(n, committee_size)
    sub_committee = math.comb(committee_size, subcommittee_size)
    return main_committee * sub_committee