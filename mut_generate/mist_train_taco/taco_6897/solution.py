"""
QUESTION:
You are given three piles of casino chips: white, green and black chips:

* the first pile contains only white chips
* the second pile contains only green chips
* the third pile contains only black chips

Each day you take exactly two chips of different colors and head to the casino. You can choose any color, but you are not allowed to take two chips of the same color in a day.

You will be given an array representing the number of chips of each color and your task is to return the maximum number of days you can pick the chips. Each day you need to take exactly two chips.

```python 
solve([1,1,1]) = 1, because after you pick on day one, there will be only one chip left
solve([1,2,1] = 2, you can pick twice; you pick two chips on day one then on day two
solve([4,1,1]) = 2
```

```javascript 
solve([1,1,1]) = 1, because after you pick on day one, there will be only one chip left
solve([1,2,1]) = 2, you can pick twice; you pick two chips on day one then on day two
solve([4,1,1]) = 2
```

```go 
solve([1,1,1]) = 1, because after you pick on day one, there will be only one chip left
solve([1,2,1]) = 2, you can pick twice; you pick two chips on day one then on day two
solve([4,1,1]) = 2
```


```ruby 
solve([1,1,1]) = 1, because after you pick on day one, there will be only one chip left
solve([1,2,1]) = 2, you can pick twice; you pick two chips on day, two chips on day two
solve([4,1,1]) = 2
```

More examples in the test cases. Good luck!

Brute force is not the way to go here. Look for a simplifying mathematical approach.
"""

def max_days_with_chips(chips):
    # Sort the chips to get the smallest, middle, and largest piles
    x, y, z = sorted(chips)
    # The maximum number of days is the minimum of the sum of the two smallest piles
    # and half the total number of chips (since each day requires two chips)
    return min(x + y, (x + y + z) // 2)