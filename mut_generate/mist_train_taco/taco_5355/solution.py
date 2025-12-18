"""
QUESTION:
Drazil likes heap very much. So he created a problem with heap:

There is a max heap with a height h implemented on the array. The details of this heap are the following:

This heap contains exactly 2^h - 1 distinct positive non-zero integers. All integers are distinct. These numbers are stored in the array a indexed from 1 to 2^h-1. For any 1 < i < 2^h, a[i] < a[\left ⌊{i/2}\right ⌋].

Now we want to reduce the height of this heap such that the height becomes g with exactly 2^g-1 numbers in heap. To reduce the height, we should perform the following action 2^h-2^g times:

Choose an index i, which contains an element and call the following function f in index i:

<image>

Note that we suppose that if a[i]=0, then index i don't contain an element.

After all operations, the remaining 2^g-1 element must be located in indices from 1 to 2^g-1. Now Drazil wonders what's the minimum possible sum of the remaining 2^g-1 elements. Please find this sum and find a sequence of the function calls to achieve this value.

Input

The first line of the input contains an integer t (1 ≤ t ≤ 70 000): the number of test cases.

Each test case contain two lines. The first line contains two integers h and g (1 ≤ g < h ≤ 20). The second line contains n = 2^h-1 distinct positive integers a[1], a[2], …, a[n] (1 ≤ a[i] < 2^{20}). For all i from 2 to 2^h - 1, a[i] < a[\left ⌊{i/2}\right ⌋].

The total sum of n is less than 2^{20}.

Output

For each test case, print two lines.

The first line should contain one integer denoting the minimum sum after reducing the height of heap to g. The second line should contain 2^h - 2^g integers v_1, v_2, …, v_{2^h-2^g}. In i-th operation f(v_i) should be called.

Example

Input


2
3 2
7 6 3 5 4 2 1
3 2
7 6 5 4 3 2 1


Output


10
3 2 3 1
8
2 1 3 1
"""

def minimize_heap_sum(A, h, g):
    N = len(A)
    ans = []
    initial_root = 0
    items_to_leave = pow(2, g) - 1
    expected_ans_size = pow(2, h) - pow(2, g)
    
    while len(ans) < expected_ans_size:
        root = initial_root
        operations = []
        ok = False
        while True:
            lchi = root * 2 + 1
            rchi = lchi + 1
            lchv = A[lchi] if lchi < N else 0
            rchv = A[rchi] if rchi < N else 0
            if lchv == 0 and rchv == 0:
                if root >= items_to_leave:
                    ok = True
                    A[root] = 0
                break
            if lchv > rchv:
                operations.append((root, lchv))
                root = lchi
            else:
                operations.append((root, rchv))
                root = rchi
        if ok:
            for (index, value) in operations:
                A[index] = value
            ans.append(initial_root + 1)
        else:
            initial_root += 1
    
    min_sum = sum(A[:items_to_leave])
    return min_sum, ans