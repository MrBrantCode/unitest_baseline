"""
QUESTION:
Write a program of a Merge Sort algorithm implemented by the following pseudocode. You should also report the number of comparisons in the Merge function.


Merge(A, left, mid, right)
n1 = mid - left;
n2 = right - mid;
create array L[0...n1], R[0...n2]
for i = 0 to n1-1
do L[i] = A[left + i]
for i = 0 to n2-1
do R[i] = A[mid + i]
L[n1] = SENTINEL
R[n2] = SENTINEL
i = 0;
j = 0;
for k = left to right-1
if L[i] <= R[j]
then A[k] = L[i]
i = i + 1
else A[k] = R[j]
j = j + 1

Merge-Sort(A, left, right){
if left+1 < right
then mid = (left + right)/2;
call Merge-Sort(A, left, mid)
call Merge-Sort(A, mid, right)
call Merge(A, left, mid, right)


Notes

Constraints

* n ≤ 500000
* 0 ≤ an element in S ≤ 109

Input

In the first line n is given. In the second line, n integers are given.

Output

In the first line, print the sequence S. Two consequtive elements should be separated by a space character.

In the second line, print the number of comparisons.

Example

Input

10
8 5 9 2 6 3 7 1 10 4


Output

1 2 3 4 5 6 7 8 9 10
34
"""

def merge_sort_with_comparisons(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    
    count = 0
    
    def merge(a, left, mid, right):
        nonlocal count
        l = a[left:mid]
        r = a[mid:right]
        l.append(10 ** 9 + 1)
        r.append(10 ** 9 + 1)
        i = 0
        j = 0
        for k in range(left, right):
            count += 1
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
    
    def merge_sort(a, left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            merge_sort(a, left, mid)
            merge_sort(a, mid, right)
            merge(a, left, mid, right)
    
    merge_sort(arr, left, right)
    return arr, count