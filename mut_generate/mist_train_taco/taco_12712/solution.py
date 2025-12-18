"""
QUESTION:
The goal of this Kata is to remind/show you, how Z-algorithm works and test your implementation.

For a string str[0..n-1], Z array is of same length as string. An element Z[i] of Z array stores length of the longest substring starting from str[i] which is also a prefix of str[0..n-1]. The first entry of Z array is meaning less as complete string is always prefix of itself.

Example:

Index:            0   1   2   3   4   5   6   7   8   9  10  11


Text:             "a   a   b   c   a   a   b   x   a   a   a   z"


Z values:         [11,   1,   0,   0,   3,   1,   0,   0,   2,   2,   1,   0]



Your task will be to implement Z algorithm in your code and return Z-array.

For empty string algorithm should return [].

Input: string str 

Output: Z array

For example:

print zfunc('ababcaba')

[8, 0, 2, 0, 0, 3, 0, 1]

Note, that an important part of this kata is that you have to use
efficient way to get Z-array (O(n))
"""

def compute_z_array(str_):
    n = len(str_)
    if n == 0:
        return []
    
    z = [0] * n
    l, r, k = 0, 0, 0
    
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and str_[r] == str_[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and str_[r] == str_[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    
    z[0] = n
    return z