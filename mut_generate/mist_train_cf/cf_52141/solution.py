"""
QUESTION:
Implement a function named `radix_sort` that takes an array of positive integers as input and returns the sorted array. The function should use the Radix sort algorithm, which sorts integers by processing their individual digits from the least significant digit to the most significant digit.
"""

def radix_sort(arr):
    def counting_sort(arr, exp1): 
        n = len(arr) 
        output = [0] * (n) 
        count = [0] * (10) 
  
        for i in range(0, n): 
            index = (arr[i] // exp1) 
            count[ (index)%10 ] += 1
  
        for i in range(1, 10): 
            count[i] += count[i - 1] 
  
        i = n-1
        while i>=0: 
            index = (arr[i] // exp1) 
            output[ count[(index)%10 ] - 1] = arr[i] 
            count[ (index)%10 ] -= 1
            i -= 1
  
        for i in range(0,len(arr)): 
            arr[i] = output[i] 
  
    max1 = max(arr) 
  
    exp = 1
    while max1 / exp > 0: 
        counting_sort(arr,exp) 
        exp *= 10
    return arr