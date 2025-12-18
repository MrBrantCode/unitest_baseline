"""
QUESTION:
Create a function called `mergeSort` that sorts an array of words in alphabetical order, handles duplicates in a case-insensitive manner, and treats special characters as separate words to be placed before alphabetical characters in the sorted array. The function should not use any built-in sorting functions and have a time complexity of O(n log n). The function should remove any duplicate words and special characters, considering words with the same letters but different cases and special characters as duplicates.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    return merge(mergeSort(leftHalf), mergeSort(rightHalf))


def merge(left, right):
    mergedArray = []
    leftPtr = 0
    rightPtr = 0

    while leftPtr < len(left) and rightPtr < len(right):
        leftWord = left[leftPtr].lower()
        rightWord = right[rightPtr].lower()

        if leftWord == rightWord:
            rightPtr += 1
        elif leftWord < rightWord:
            mergedArray.append(left[leftPtr])
            leftPtr += 1
        else:
            mergedArray.append(right[rightPtr])
            rightPtr += 1

    mergedArray += left[leftPtr:]
    mergedArray += right[rightPtr:]

    # Remove special characters and duplicates
    finalArray = []
    for word in mergedArray:
        word = ''.join(e for e in word if e.isalnum())
        if word.lower() not in [w.lower() for w in finalArray]:
            finalArray.append(word)

    return finalArray