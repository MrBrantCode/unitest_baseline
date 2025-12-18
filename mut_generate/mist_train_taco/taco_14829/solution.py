"""
QUESTION:
"Search" is an operation to obtain the desired information from a large amount of information. Familiar examples include "finding your own exam number from a large number of exam numbers" when announcing your success, or "finding Taro Aizu's phone number" from your phone book. This search operation is also widely used in the computer field.

<image>


There are many ways to search. Consider a search method that can be used when the data to be searched is arranged in ascending (or largest) order.

Using the magnitude relationship between the value located in the center of the data string arranged in ascending order (or in descending order) and the target value, the first half is set as the search range or the second half is searched from the value located in the center. There is a way to narrow down the search range by deciding whether to make it a range. The procedure is as follows.

1. The entire column of data is the scope of the search.
2. Examine the value located in the center of the search range.
3. If the desired value matches the centered value, the search ends.
4. If it is smaller than the target value and the value located in the center, the first half is the search range, and if it is larger, the second half is the search range and returns to 2.



The following is an example of the search method described above. The desired value in this example is 51. Each piece of data is numbered (index), which starts at 0.






Step 1: Initially, the search range is the entire number 0-6.

Step 2: Find the value in the center of the search range. However, the "centered value" is the value at the position of the number obtained by dividing (the number on the left side + the number on the right side) by 2. In other words, in this case, (0 + 6) ÷ 2 is calculated, and the value (36) at number 3 is the value located in the center.

Step 3: Compare the desired value (51) with the centrally located value (36).

Step 4: From the result of step 3, the target value is larger than the value located in the center, so the search range is from number 4 (next to the value located in the center) in the latter half. Use the same procedure to check the value located in the center of the search range, and if the target value is smaller than the value located in the center, the first half is the search range, and if it is larger, the second half is the search range. I will make it smaller. (Repeat of steps 2 to 4) The search ends when the target value matches the value located in the center or the search range is reached.

| <image>
--- | ---



Create a program that takes an array of n numbers as input and outputs the number of times the target value is compared with the value located in the center. However, if the number of the value located in the center is not divisible, the value rounded down to the nearest whole number will be used as the number. It is assumed that the given data columns are sorted in ascending order.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


n
a1
a2
::
an
k


The number of numbers n (1 ≤ n ≤ 100) is given on the first line, and the i-th number ai (1 ≤ ai ≤ 100000, integer) is given on the following n lines.

The following line is given the value k (1 ≤ k ≤ 100000) to search for.

Output

The number of comparisons until the search is completed for each data set is output on one line.

Example

Input

7
11
15
23
36
51
61
86
51
4
1
2
3
5
4
0


Output

3
3
"""

def binary_search_comparisons(a: list[int], k: int) -> int:
    """
    Perform a binary search on the sorted array `a` to find the target value `k`
    and return the number of comparisons made during the search.

    Parameters:
    - a (list[int]): A sorted list of integers.
    - k (int): The target value to search for.

    Returns:
    - int: The number of comparisons made during the binary search.
    """
    l, r, c = 0, len(a) - 1, 0
    while l <= r:
        c += 1
        m = (l + r) // 2
        if k == a[m]:
            break
        elif k < a[m]:
            r = m - 1
        else:
            l = m + 1
    return c