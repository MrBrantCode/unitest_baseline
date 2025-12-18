"""
QUESTION:
Implement a hybrid sorting algorithm, HybridSort, that efficiently sorts a large, unordered array of integer data types with frequent repetitions. The algorithm should utilize a combination of Quicksort and Insertion Sort, switching to Insertion Sort when the partition size is below a certain threshold. The algorithm should take an array A and an optional threshold value (default is 10) as input, and return the sorted array.
"""

def HybridSort(A, thresh=10):
  def InsertionSort(start, end):
    for i in range(start + 1, end + 1):
      key = A[i]
      j = i - 1
      while j >= start and key < A[j]:
        A[j + 1] = A[j]
        j -= 1
      A[j + 1] = key

  def Partition(start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
      if A[j] <= pivot:
        i += 1
        A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1

  def QuickSort(start, end):
    if start < end:
      if end - start + 1 < thresh:
        InsertionSort(start, end)
      else:
        pivot = Partition(start, end)
        QuickSort(start, pivot - 1)
        QuickSort(pivot + 1, end)

  QuickSort(0, len(A) - 1)
  return A