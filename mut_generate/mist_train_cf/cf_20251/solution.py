"""
QUESTION:
Design an efficient search function `search_terms` that takes a sorted list of search terms and a user's input as parameters. The function should return two lists: 
1. A list of autocomplete suggestions (at most 5 terms that start with the user's input) with a time complexity of O(log n).
2. A list of exact match search results (at most 10 terms that match the user's input) with a time complexity of O(1) for updating the results.

Note that the function should be designed to handle a large dataset of search terms efficiently.
"""

def search_terms(search_dataset, user_input):
    def modified_binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid].startswith(target):
                if mid == 0 or not arr[mid - 1].startswith(target):
                    return mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    autocomplete_suggestions = []
    exact_match_results = []

    index = modified_binary_search(search_dataset, user_input)
    if index != -1:
        for i in range(index, min(index + 5, len(search_dataset))):
            if search_dataset[i].startswith(user_input):
                autocomplete_suggestions.append(search_dataset[i])

        for i in range(index, min(index + 10, len(search_dataset))):
            if search_dataset[i] == user_input:
                exact_match_results.append(search_dataset[i])

    return autocomplete_suggestions, exact_match_results