"""
QUESTION:
Write a function `sum_of_unique_numbers(all_abund_numbers, end)` that takes a list of abundant numbers `all_abund_numbers` and an integer `end` as parameters. The function should return the sum of all unique numbers within the range from 1 to `end` that are not present in the set of all possible sums of pairs of numbers from `all_abund_numbers`.
"""

def entance(all_abund_numbers, end):
    def sums(abund_numbers, end):
        pairs = set()
        for i in range(len(abund_numbers)):
            for j in range(i, len(abund_numbers)):
                pair_sum = abund_numbers[i] + abund_numbers[j]
                if pair_sum <= end:
                    pairs.add(pair_sum)
        return pairs

    all_pairs = sums(all_abund_numbers, end)
    unique = [x for x in range(1, end + 1) if x not in all_pairs]
    return sum(unique)