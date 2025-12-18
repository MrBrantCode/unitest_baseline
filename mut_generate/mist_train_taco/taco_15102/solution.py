"""
QUESTION:
Milly and her classmates are standing in a queue to attend the morning assembly of her school. According to the rule any student should stand in his/her proper place in order to make the queue completely visible till the end. Milly being the class monitor is required to make this queue such that students should be standing in an increasing order of their heights. Student with smaller height should stand at front and the student with higher height should stand at the end. She can reverse one particular group of the students. But she can perform this action only once. Here group of students means one particular continuous segment. Height of the students are distinct. Your task is to help her in solving this problem. You have to output starting and ending position of that group. In case, if queue is already in required condition or it is not possible to solve then consider starting and ending positions as -1.

Input

First line of the input will contain T (No. of test cases).
For each test case, first line will contain a integer N (No. of students). Second line will contain N space separated integers (denoting distinct height of students in initial queue) 

Output
For every test case, print the two space separated integers denoting the starting and ending positions of group in a new line.
Constraints

1 ≤ T ≤ 10
1 ≤ N ≤ 10^4
1 ≤ Height ≤ 10^9 

SAMPLE INPUT
3
4
2 4 3 5
3
1 2 3
3
2 3 1

SAMPLE OUTPUT
2 3
-1 -1
-1 -1

Explanation

Test case #1: Reverse the segment [2, 3]
Test case #2: Already a asked queue.
Test case #3: Not possible.
"""

def find_group_to_reverse(heights, n):
    def is_sorted(arr):
        """Helper function to check if the array is sorted in non-decreasing order."""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    if is_sorted(heights):
        return -1, -1

    start = end = 0
    for i in range(n - 1):
        if heights[i] > heights[i + 1]:
            end += 1
        else:
            if start == end:
                start = end = i + 1
            else:
                if is_sorted(heights[0:start] + list(reversed(heights[start:end + 1])) + heights[end + 1:n]):
                    return start + 1, end + 1
                else:
                    return -1, -1
    if is_sorted(heights[0:start] + list(reversed(heights[start:end + 1])) + heights[end + 1:n]):
        return start + 1, end + 1
    else:
        return -1, -1