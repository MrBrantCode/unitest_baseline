"""
QUESTION:
Write a function `find_three_elements` that takes a list of positive integers `arr` and a target value `target` as input, and returns all possible combinations of three elements in the list that sum up to the target value. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the input list.
"""

def find_three_elements(arr, target):
    arr.sort()
    combinations = []
    n = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            current_sum = arr[i] + arr[j] + arr[k]

            if current_sum == target:
                combinations.append([arr[i], arr[j], arr[k]])

                while j < k and arr[j] == arr[j + 1]:
                    j += 1
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1

                j += 1
                k -= 1
            elif current_sum < target:
                j += 1
            else:
                k -= 1

    return combinations