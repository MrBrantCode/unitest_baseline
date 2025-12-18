"""
QUESTION:
There are n animals in the queue to Dr. Dolittle. When an animal comes into the office, the doctor examines him, gives prescriptions, appoints tests and may appoint extra examination. Doc knows all the forest animals perfectly well and therefore knows exactly that the animal number i in the queue will have to visit his office exactly ai times. We will assume that an examination takes much more time than making tests and other extra procedures, and therefore we will assume that once an animal leaves the room, it immediately gets to the end of the queue to the doctor. Of course, if the animal has visited the doctor as many times as necessary, then it doesn't have to stand at the end of the queue and it immediately goes home. 

Doctor plans to go home after receiving k animals, and therefore what the queue will look like at that moment is important for him. Since the doctor works long hours and she can't get distracted like that after all, she asked you to figure it out. 

Input

The first line of input data contains two space-separated integers n and k (1 ≤ n ≤ 105, 0 ≤ k ≤ 1014). In the second line are given space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Please do not use the %lld specificator to read or write 64-bit numbers in C++. It is recommended to use cin, cout streams (you can also use the %I64d specificator). 

Output

If the doctor will overall carry out less than k examinations, print a single number "-1" (without quotes). Otherwise, print the sequence of numbers — number of animals in the order in which they stand in the queue. 

Note that this sequence may be empty. This case is present in pretests. You can just print nothing or print one "End of line"-character. Both will be accepted.

Examples

Input

3 3
1 2 1


Output

2 

Input

4 10
3 3 2 1


Output

-1


Input

7 10
1 3 3 1 2 3 1


Output

6 2 3 

Note

In the first sample test:

  * Before examination: {1, 2, 3}
  * After the first examination: {2, 3}
  * After the second examination: {3, 2}
  * After the third examination: {2}



In the second sample test:

  * Before examination: {1, 2, 3, 4, 5, 6, 7}
  * After the first examination: {2, 3, 4, 5, 6, 7}
  * After the second examination: {3, 4, 5, 6, 7, 2}
  * After the third examination: {4, 5, 6, 7, 2, 3}
  * After the fourth examination: {5, 6, 7, 2, 3}
  * After the fifth examination: {6, 7, 2, 3, 5}
  * After the sixth examination: {7, 2, 3, 5, 6}
  * After the seventh examination: {2, 3, 5, 6}
  * After the eighth examination: {3, 5, 6, 2}
  * After the ninth examination: {5, 6, 2, 3}
  * After the tenth examination: {6, 2, 3}
"""

from collections import deque

def simulate_doctor_queue(n, k, a):
    # Check if the total number of examinations is less than k
    if sum(a) < k:
        return -1
    
    # Binary search to find the maximum number of examinations each animal can have
    (ok, ng) = (0, 10 ** 9 + 10)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if sum((mid if mid < x else x for x in a)) <= k:
            ok = mid
        else:
            ng = mid
    
    # Create a deque of indices for animals that still need more examinations
    index = deque([i + 1 for i in range(n) if a[i] > ok])
    dq = deque([x - ok for x in a if x > ok])
    
    # Adjust k by subtracting the number of examinations already performed
    k -= sum((ok if ok < x else x for x in a))
    
    # Perform the remaining examinations
    for _ in range(k):
        dq[0] -= 1
        if dq[0]:
            dq.rotate(-1)
            index.rotate(-1)
        else:
            dq.popleft()
            index.popleft()
    
    return list(index)