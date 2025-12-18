"""
QUESTION:
Median of K numbers is defined as the (K/2)th smallest number, if K is even; and the ((K+1)/2)th smallest number if K is odd. For example, 

median of the 4 numbers: 2 1 8 7 is the 2nd smallest number i.e. 2, 

and the median of the 5 numbers:  2 1 8 7 6  is the 3rd smallest number i.e. 6.

In this problem, you'll be given N numbers.  Let the kth median or m(k) be defined as the median of the first k numbers (1 ≤ k ≤ N). i.e. the 5th median or m(5)  is the median of the first 5 numbers, the 8th median or  m(8) is the  median of the first 8 numbers, etc.
In other words, let Ai denote the ith number, then the kth median or m(k) is defined as the median of the numbers A1,A2,…,AK.

Your task is to find m(1) + m(2) + m(3) + ...+ m(n)
Output the answer modulo 100000 (10^5).

INPUT:

There is only one test case. The first line contains N, the count of numbers. N lines follow, each containing one number.

OUTPUT:

Output a single line, containing the sum of the medians.

CONSTRAINTS:

1 ≤ N ≤ 100000

0 ≤ each number Ni ≤ 100000

SAMPLE INPUT
5
10
5
1
2
15

SAMPLE OUTPUT
27

Explanation

m(1)=median of [ 10 ]=10
m(2)=median of [ 10 5 ]=5
m(3)=median of [ 10 5 1 ]=5
m(4)=median of [ 10 5 1 2 ]=2
m(5)=median of [ 10 5 1 2  15 ]=5
( m(1) + m(2) + m(3) + m(4) + m(5) ) % 100000=27
"""

import bisect

def calculate_median_sum(numbers, modulo=100000):
    def median(nums, k):
        K = k + 1
        return nums[(K // 2) - 1] if K % 2 == 0 else nums[((K + 1) // 2) - 1]
    
    sorted_numbers = []
    median_sum = 0
    
    for k, number in enumerate(numbers):
        bisect.insort(sorted_numbers, number)
        median_sum += median(sorted_numbers, k)
    
    return median_sum % modulo