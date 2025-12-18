"""
QUESTION:
Filter Restaurants by Criteria

Create a function `filterRestaurants` that takes in a list of restaurants `restaurants` where each restaurant is a list of five integers `[idi, ratingi, veganFriendlyi, pricei, distancei]` and four filters: `veganFriendly`, `maxPrice`, `maxDistance`, and `minRating`. The function should filter the restaurants based on the given criteria and return a list of restaurant IDs ordered by rating from highest to lowest, and for restaurants with the same rating, order them by ID from highest to lowest.

Constraints:
- `1 <= restaurants.length <= 10^4`
- `restaurants[i].length == 5`
- `1 <= idi, ratingi, pricei, distancei <= 10^5`
- `1 <= maxPrice, maxDistance, minRating <= 10^5`
- `veganFriendlyi` and `veganFriendly` are 0 or 1.
- All `idi` are distinct.
"""

def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance, minRating):
    filtered = filter(lambda r: (r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance and r[1] >= minRating), restaurants)
    sorted_restaurants = sorted(filtered, key = lambda r: (-r[1], -r[0]))
    return [r[0] for r in sorted_restaurants]