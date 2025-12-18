"""
QUESTION:
Igor has fallen in love with Tanya. Now Igor wants to show his feelings and write a number on the fence opposite to Tanya's house. Igor thinks that the larger the number is, the more chance to win Tanya's heart he has. 

Unfortunately, Igor could only get v liters of paint. He did the math and concluded that digit d requires a_{d} liters of paint. Besides, Igor heard that Tanya doesn't like zeroes. That's why Igor won't use them in his number.

Help Igor find the maximum number he can write on the fence.


-----Input-----

The first line contains a positive integer v (0 ≤ v ≤ 10^6). The second line contains nine positive integers a_1, a_2, ..., a_9 (1 ≤ a_{i} ≤ 10^5).


-----Output-----

Print the maximum number Igor can write on the fence. If he has too little paint for any digit (so, he cannot write anything), print -1.


-----Examples-----
Input
5
5 4 3 2 1 2 3 4 5

Output
55555

Input
2
9 11 1 12 5 8 9 10 6

Output
33

Input
0
1 1 1 1 1 1 1 1 1

Output
-1
"""

def maximum_number_on_fence(v, a):
    mi = -1
    mc = 10 ** 18
    
    # Find the digit with the minimum paint requirement
    for i in range(len(a)):
        if a[i] <= mc:
            mc = a[i]
            mi = i
    
    # Calculate the maximum number of digits Igor can write
    digits = v // mc
    
    # If Igor cannot write any digit, return -1
    if digits == 0:
        return "-1"
    
    # Calculate the remaining paint after writing the maximum number of digits
    v -= mc * digits
    
    # Initialize the answer with the digit that requires the least paint
    ans = [str(mi + 1)] * digits
    
    # Try to maximize the number by replacing digits from left to right
    index = 0
    while index < digits:
        for i in range(len(a)):
            if 9 - i <= mi + 1:
                return ''.join(ans)
            if v - a[i] + mc >= 0:
                v = v - a[i] + mc
                ans[index] = str(9 - i)
                break
        index += 1
    
    return ''.join(ans)