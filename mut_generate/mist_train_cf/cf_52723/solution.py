"""
QUESTION:
Implement a function `segregate_and_sort` that takes an integer array as input and returns three separate lists: one for even numbers, one for odd numbers, and one for prime numbers. The elements within each list should be ordered in increasing order. The implementation should not use any built-in sorting or prime-checking functions.
"""

def segregate_and_sort(arr):
    even_numbers = []
    odd_numbers = []
    prime_numbers = [] 
    
    # function to check prime numbers
    def check_prime(num):
        if num <= 1 :
            return False
        else :
            for i in range(2,num):
                if num % i == 0:
                    return False

            return True            

    # partition the list into even, odd and prime number lists
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)

            # 2 is the only even prime number
            if num == 2:
                prime_numbers.append(num)
        else:
            odd_numbers.append(num)
            if check_prime(num):
                prime_numbers.append(num)

    # custom Bubble sort implementation
    def bubble_sort(lst):
        for i in range(len(lst)):
            for j in range(len(lst) - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst  
    
    # sort all the lists
    even_numbers = bubble_sort(even_numbers)
    odd_numbers = bubble_sort(odd_numbers)
    prime_numbers = bubble_sort(prime_numbers)
    
    return even_numbers, odd_numbers, prime_numbers