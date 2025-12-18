"""
QUESTION:
Create a function named `rotate_list` that takes two parameters: `my_list` and `k`, where `my_list` is a list of integers and `k` is the number of positions to rotate the list to the right. The function should rotate the list in-place, meaning it should modify the original list without creating a new one, and return the rotated list. The time complexity of the function should be O(n), where n is the length of the list, and the space complexity should be O(1), meaning it should not use any additional data structures or create new lists.
"""

def rotate_list(my_list, k):
    if k == 0 or len(my_list) == 0:
        return my_list
    
    n = len(my_list)
    k = k % n
    
    def get_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    gcd = get_gcd(n, k)
    
    for i in range(gcd):
        temp = my_list[i]
        j = i
        while True:
            next_index = (j + k) % n
            if next_index == i:
                break
            my_list[j] = my_list[next_index]
            j = next_index
        my_list[j] = temp
    
    return my_list