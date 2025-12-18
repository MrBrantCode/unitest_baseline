"""
QUESTION:
Write a function `novel_sorting(sys, count, genre, pricing)` where `sys` is a list of strings representing the novels with their genres (e.g., "3 Romance"), `count` is the total number of novels, `genre` is a list of possible genres, and `pricing` is a dictionary with genres as keys and their prices as values. 

The function should calculate and return a dictionary where the keys are the genres and the values are the number of novels of each genre, such that the total number of novels does not exceed `count` and the total price does not exceed the total price of `count` novels. If a genre has zero novels, it should not be included in the output dictionary.
"""

def novel_sorting(sys, count, genre, pricing):
    distributed_novels = {}
    remaining_novels = count

    # calculate number of novels already included in 'sys'
    for s in sys:
        num, genre_name = s.split(' ', 1)
        distributed_novels[genre_name] = int(num)
        remaining_novels -= pricing[genre_name] * int(num)

    # calculate distribution for remaining genres (those not in 'distributed_novels')
    remaining_genre = [g for g in genre if g not in distributed_novels]
    for gen in remaining_genre:
        if pricing[gen] <= remaining_novels:  # check if there's enough money to buy at least one novel of this genre
            num_novels = remaining_novels // pricing[gen]
            if num_novels > 0:  # store in the dictionary if the distribution is non-zero
                distributed_novels[gen] = num_novels
            remaining_novels -= pricing[gen] * num_novels

    # remove genres that were in 'sys' but with zero distributions
    for gen in list(distributed_novels.keys()):
        if distributed_novels[gen] == 0:
            del distributed_novels[gen]

    return distributed_novels