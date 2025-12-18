"""
QUESTION:
It's finally summer in Chefland! So our chef is looking forward to prepare some of the best "beat-the-heat" dishes to attract more customers. He summons the Wizard of Dessert to help him with one such dish.
The wizard provides the chef with a sequence of N ingredients where the i^{th} ingredient has a delish value of D[i]. The preparation of the dish takes place in two phases. 

Phase 1 : The chef chooses two indices i and j and adds the ingredients i, i+1, ..., j to his dish. He also finds the sum of the delish value in this range i.e D[i] + D[i+1] + ... + D[j].  

Phase 2 : The chef chooses two more indices k and l and adds the ingredients k, k+1, ..., l to his dish. He also finds the sum of the delish value in this range i.e D[k] + D[k+1] + ... + D[l]. 

Note that 1  ≤ i  ≤ j < k  ≤ l ≤ N. 

The total delish value of the dish is determined by the absolute difference between the values obtained in the two phases. Obviously, the chef wants to maximize the total delish value for his dish. So, he hires you to help him.
 
------ Input ------ 

First line of input contains an integer T denoting the number of test cases. For each test case, the first line contains an integer N denoting the number of ingredients. The next line contains N space separated integers where the i^{th} integer represents the delish value D[i] of the i^{th} ingredient.

------ Output ------ 

Print the maximum delish value of the dish that the chef can get.

------ Constraints ------ 

$ 1 ≤ T ≤ 50 $
$ 2 ≤ N ≤ 10000 $
$ -1000000000 (−10^{9}) ≤ D[i] ≤ 1000000000 (10^{9}) 

----- Sample Input 1 ------ 
2
5
1 2 3 4 5
4
1 1 -1 -1
----- Sample Output 1 ------ 
13
4
----- explanation 1 ------ 
Example case 1.
Chef can choose i = j = 1, k = 2, l = 5.
The delish value hence obtained  is  | (2+3+4+5) ? (1) | = 13 .
 
Example case 2.
Chef can choose i = 1, j = 2, k = 3, l = 4.
The delish value hence obtained  is  | ( ( ?1 ) + ( ?1 ) ) ? ( 1 + 1 ) | = 4 .
"""

from math import inf

def calculate_max_delish_value(ingredients):
    n = len(ingredients)
    if n < 2:
        return 0
    
    # Helper functions to calculate max and min subarray sums
    def max_subarray_sum(arr):
        max_so_far = -inf
        max_ending_here = 0
        result = []
        for num in arr:
            max_ending_here += num
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
            result.append(max_so_far)
        return result
    
    def min_subarray_sum(arr):
        min_so_far = inf
        min_ending_here = 0
        result = []
        for num in arr:
            min_ending_here += num
            if min_ending_here < min_so_far:
                min_so_far = min_ending_here
            if min_ending_here > 0:
                min_ending_here = 0
            result.append(min_so_far)
        return result
    
    # Calculate max and min subarray sums from left to right
    left_max_sums = max_subarray_sum(ingredients)
    left_min_sums = min_subarray_sum(ingredients)
    
    # Calculate max and min subarray sums from right to left
    reversed_ingredients = ingredients[::-1]
    right_max_sums = max_subarray_sum(reversed_ingredients)[::-1]
    right_min_sums = min_subarray_sum(reversed_ingredients)[::-1]
    
    # Calculate the maximum delish value
    max_delish_value = -1
    for i in range(n - 1):
        max_delish_value = max(max_delish_value, abs(left_max_sums[i] - right_min_sums[i + 1]), abs(right_max_sums[i + 1] - left_min_sums[i]))
    
    return max_delish_value