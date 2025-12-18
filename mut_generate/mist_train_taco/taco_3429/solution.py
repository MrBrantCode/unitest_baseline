"""
QUESTION:
One day Ms Swan bought an orange in a shop. The orange consisted of n·k segments, numbered with integers from 1 to n·k. 

There were k children waiting for Ms Swan at home. The children have recently learned about the orange and they decided to divide it between them. For that each child took a piece of paper and wrote the number of the segment that he would like to get: the i-th (1 ≤ i ≤ k) child wrote the number a_{i} (1 ≤ a_{i} ≤ n·k). All numbers a_{i} accidentally turned out to be different.

Now the children wonder, how to divide the orange so as to meet these conditions:  each child gets exactly n orange segments;  the i-th child gets the segment with number a_{i} for sure;  no segment goes to two children simultaneously. 

Help the children, divide the orange and fulfill the requirements, described above.


-----Input-----

The first line contains two integers n, k (1 ≤ n, k ≤ 30). The second line contains k space-separated integers a_1, a_2, ..., a_{k} (1 ≤ a_{i} ≤ n·k), where a_{i} is the number of the orange segment that the i-th child would like to get.

It is guaranteed that all numbers a_{i} are distinct.


-----Output-----

Print exactly n·k distinct integers. The first n integers represent the indexes of the segments the first child will get, the second n integers represent the indexes of the segments the second child will get, and so on. Separate the printed numbers with whitespaces.

You can print a child's segment indexes in any order. It is guaranteed that the answer always exists. If there are multiple correct answers, print any of them.


-----Examples-----
Input
2 2
4 1

Output
2 4 
1 3 

Input
3 1
2

Output
3 2 1
"""

def divide_orange(n, k, a):
    # Total number of segments
    total_segments = n * k
    
    # List of all segments
    all_segments = list(range(1, total_segments + 1))
    
    # Segments that are not in the list 'a'
    remaining_segments = [seg for seg in all_segments if seg not in a]
    
    # Result list to store segments for each child
    result = []
    
    # Assign segments to each child
    for i in range(k):
        # The segment that the child wants
        desired_segment = a[i]
        
        # Remaining segments to be assigned to this child
        child_segments = [desired_segment] + remaining_segments[i * (n - 1):(i + 1) * (n - 1)]
        
        # Add to the result
        result.append(child_segments)
    
    return result