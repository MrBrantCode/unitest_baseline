"""
QUESTION:
Chef recently learned about ratios and proportions. He wrote some positive integers a, b, c, d on a paper. Chef wants to know whether he can shuffle these numbers so as to make some proportion? Formally, four numbers x, y, z, w are said to make a proportion if ratio of x : y is same as that of z : w.

-----Input-----
Only line of the input contains four space separated positive integers - a, b, c, d.

-----Output-----
Print "Possible" if it is possible to shuffle a, b, c, d to make proportion, otherwise "Impossible" (without quotes).

-----Constraints-----
- 1 ≤ a, b, c, d  ≤ 1000

-----Example-----
Input:
1 2 4 2

Output:
Possible

-----Explanation-----
By swapping 4 and the second 2, we get 1 2 2 4. Note that 1 2 2 4 make proportion as 1 : 2 = 2 : 4. Hence answer is "Possible"
"""

def is_proportion_possible(a, b, c, d):
    def permutate(arr):
        if len(arr) == 1:
            yield arr
        for x in range(len(arr)):
            for perm in permutate(arr[:x] + arr[x + 1:]):
                yield ([arr[x]] + perm)
    
    vals = [a, b, c, d]
    for val in permutate(vals):
        if val[0] / float(val[1]) == val[2] / float(val[3]):
            return 'Possible'
    return 'Impossible'