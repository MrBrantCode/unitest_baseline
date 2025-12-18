"""
QUESTION:
Implement a function `quicksort(arr, low, high)` that sorts an array of strings `arr` in ascending order based on the number of vowels in each sentence. The `quicksort` function should use the `partition` and `count_vowels` functions to achieve this. The `count_vowels` function should count the number of vowels in a given sentence, and the `partition` function should rearrange the elements in the array such that all elements with fewer vowels than the pivot are to its left, and all elements with more vowels than the pivot are to its right. 

The array `arr` is 0-indexed, and the parameters `low` and `high` represent the starting and ending indices of the subarray to be sorted. 

The function should modify the original array in place. The time complexity of the implementation should be O(n log n) in the best case and O(n^2) in the worst case. 

Note that the `count_vowels` function should count both lowercase and uppercase vowels, and the comparison in the `partition` function should be done correctly to ensure ascending order.
"""

def quicksort(arr, low, high):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if count_vowels(arr[j]) <= count_vowels(pivot):
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def count_vowels(sentence):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in sentence.lower():
            if char in vowels:
                count += 1
        return count

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)