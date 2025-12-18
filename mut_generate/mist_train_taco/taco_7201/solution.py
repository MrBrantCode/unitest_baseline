"""
QUESTION:
# Unflatten a list (Harder than easy)

This is the harder version of Unflatten a list (Easy)

So you have again to build a method, that creates new arrays, that can be flattened!

# Shorter: You have to unflatten a list/an array.

You get an array of integers and have to unflatten it by these rules:
```
- You have to do several runs. The depth is the number of runs, you have to do.
- In every run you have to switch the direction. First run from left, next run from right. Next left...
Every run has these rules:
- You start at the first number (from the direction).
- Take for every number x the remainder of the division by the number of still available elements (from 
  this position!) to have the number for the next decision.
- If the remainder-value is smaller than 3, take this number x (NOT the remainder-Value) direct
  for the new array and continue with the next number.
- If the remainder-value (e.g. 3) is greater than 2, take the next remainder-value-number (e.g. 3)
  elements/numbers (inclusive the number x, NOT the remainder-value) as a sub-array in the new array.
  Continue with the next number/element AFTER this taken elements/numbers.
- Every sub-array in the array is independent and is only one element for the progress on the array. 
  For every sub-array you have to follow the same rules for unflatten it.
  The direction is always the same as the actual run.
```

Sounds complicated? Yeah, thats why, this is the harder version...
Maybe an example will help.

```
 Array: [4, 5, 1, 7, 1] Depth: 2 -> [[ 4, [ 5, 1, 7 ] ], 1]
 
Steps: 
First run: (start from left side!)
1. The first number is 4. The number is smaller than the number of remaining elements, so it is the remainder-value (4 / 5 -> remainder 4).
   So 4 numbers (4, 5, 1, 7) are added as sub-array in the new array.
2. The next number is 1. It is smaller than 3, so the 1 is added direct to the new array.
Now we have --> [[4, 5, 1, 7], 1]

Second run: (start from right side!)
1. The last number (first from other side) is 1. So the 1 is added direct to the new array.
2. The next element is the sub-array. So we use the rules for this.
2a.The last number is 7. There are 4 elements in the array. So for the next decision you have to
   take the remainder from 7 / 4 -> 3. So 3 numbers (5, 1, 7) are added as sub-array in the 
   new array.
2b.Now there is the 4 and only one element last in this array. 4 / 1 -> remainder 0. It is smaller
   than 3. So the 4 is added direct to the new array.
Now we have --> [[ 4, [ 5, 1, 7 ] ], 1]
```

The given array will always contain numbers. There will only be numbers > 0.


Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
"""

def unflatten_list(arr, depth):
    def unflatten(m, d, c=0):
        if c == d:
            return m
        return unflatten(parse(m, [0, 1][c & 1]), d, c + 1)

    def parse(ar, lr):
        (sub, i) = ([], [0, len(ar) - 1][lr])
        while 0 <= i < len(ar):
            (j, r) = (ar[i], lr == 1)
            if isinstance(j, list):
                sub.append(parse(j, lr))
                i += [1, -1][r]
            else:
                mod = j % len([ar[i:], ar[:i + 1]][r])
                sub.append([j, ar[i:i + mod * [1, -1][r]:[1, -1][r]][::[1, -1][r]]][mod >= 3])
                i += [mod, 1][mod < 3] * [1, -1][r]
        return sub[::[1, -1][lr]]

    return unflatten(arr, depth)