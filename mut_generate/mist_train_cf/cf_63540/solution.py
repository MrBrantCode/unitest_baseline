"""
QUESTION:
You are given an array of positive integers `candiesCount` where `candiesCount[i]` represents the number of candies of the `ith` type you have, and a 2D array `queries` where `queries[i] = [favoriteTypei, favoriteDayi, dailyCapi, leastFavoriteTypei]`. 

Construct a boolean array `answer` such that `answer.length == queries.length` and `answer[i]` is `true` if you can eat a candy of type `favoriteTypei` on day `favoriteDayi` without eating more than `dailyCapi` candies on any day, and `false` otherwise.

The game rules are as follows: 
- You start eating candies on day `0`.
- You cannot eat any candy of type `i` unless you have eaten all candies of type `i - 1`.
- You must eat at least one candy per day until you have eaten all the candies.
- You cannot eat any candy of type `leastFavoriteTypei` unless you have eaten all candies of other types.

Restrictions: `1 <= candiesCount.length <= 105`, `1 <= candiesCount[i] <= 105`, `1 <= queries.length <= 105`, `queries[i].length == 4`, `0 <= favoriteTypei < candiesCount.length`, `0 <= favoriteDayi <= 109`, `1 <= dailyCapi <= 109`, `0 <= leastFavoriteTypei < candiesCount.length`. 

Implement a function named `canEat` to solve this problem.
"""

def canEat(candiesCount, queries):
    prefix = [0]
    for cc in candiesCount:
        prefix.append(prefix[-1] + cc)

    ans = []
    for q in queries:
        fav_type, day, daily_cap, least_fav_type = q
        fav_1_index = fav_type + 1
        fav_pre_day = prefix[fav_type]
        fav_last_day = prefix[fav_1_index] - 1

        least_last_day = prefix[least_fav_type] - 1

        atleast = day
        atlast = day * daily_cap
        
        if not (atlast <= fav_pre_day or atleast >= fav_last_day or atleast >= least_last_day):
            ans.append(True)
        else:
            ans.append(False)
    return ans