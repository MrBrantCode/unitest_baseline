"""
QUESTION:
Find the restaurant(s) with the least index sum and the highest preference from two lists of favorite restaurants. Write a function `findRestaurant(list1, list2, pref1, pref2)` that takes two lists of restaurant names `list1` and `list2`, and their corresponding preference lists `pref1` and `pref2`. The function should return a list of restaurant(s) with the minimum index sum and the highest total preference. 

Note that `list1` and `list2` are lists of unique strings, and `pref1` and `pref2` are lists of unique integers, where 1 <= length of `list1`, `list2` <= 1000, and 1 <= length of each string in `list1`, `list2` <= 30.
"""

def findRestaurant(list1, list2, pref1, pref2):
    map1 = {list1[i]: (i, pref1[i]) for i in range(len(list1))}
    least_sum, max_pref, res = float('inf'), float('-inf'), []

    for j, rest in enumerate(list2):
        idx_sum_and_pref = map1.get(rest)
        if idx_sum_and_pref is not None:
            idx_sum, pref_sum = idx_sum_and_pref[0] + j, idx_sum_and_pref[1] + pref2[j]
            if idx_sum < least_sum or (idx_sum == least_sum and pref_sum > max_pref):
                least_sum, max_pref = idx_sum, pref_sum
                res = [rest]
            elif idx_sum == least_sum and pref_sum == max_pref:
                res.append(rest)
    
    return res