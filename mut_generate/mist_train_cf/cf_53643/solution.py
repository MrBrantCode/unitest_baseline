"""
QUESTION:
Write a function named `countGoodTriplets` that takes in an array of integers `arr` and three integers `a`, `b`, and `c`. Return the number of good triplets and the number of unique good triplets in `arr` where a triplet `(arr[i], arr[j], arr[k])` is good if `0 <= i < j < k < arr.length`, `|arr[i] - arr[j]| <= a`, `|arr[j] - arr[k]| <= b`, and `|arr[i] - arr[k]| <= c`. A unique good triplet is a good triplet that has not been counted before, regardless of order. The input array has a length of 3 to 100, and each element in the array and the integers `a`, `b`, and `c` are between 0 and 1000.
"""

def countGoodTriplets(arr, a, b, c):
    count = 0
    unique_triplets = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    unique_triplets.add(frozenset([arr[i], arr[j], arr[k]]))
                    count += 1
    return count, len(unique_triplets)