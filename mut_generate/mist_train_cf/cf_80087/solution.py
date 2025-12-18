"""
QUESTION:
Write a function `maxSum` that takes two parameters: a list of integers and an integer `N`. The function should return the maximum sum that can be obtained by adding four numbers from the list. The list can contain both positive and negative numbers, and N is always 4.
"""

def maxSum(lst, N):
    final_list = []
  
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                for l in range(k+1, len(lst)):
                    final_list.append([lst[i], lst[j], lst[k], lst[l]])
   
    max_sum = float('-inf')
    res_list = []

    for i in final_list:
        if max_sum < sum(i):
            max_sum = sum(i)
            res_list = i
                
    return max_sum