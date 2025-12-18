"""
QUESTION:
There is a villa which has N rooms placed one after the other , numbered from 1 to N. There are two types of rooms - normal rooms and exit rooms. 
The rooms are connected by K corridors, where ith corridor connects room Pair[i][0] and Pair[i][1]. And there are M exit rooms whose numbers are present in the array A. The rest of the rooms are normal rooms.
Rahul starts from room number 1 (only) to next room (room connected by a corridor), and so on . If it is a normal room he will keep on moving to other rooms but if he finds an exit room then he would reach out of the villa. Your task is to help Rahul in finding the last room which he can reach.
 
Example 1:
Input:
N = 5, M = 1, K = 2
A[] = {2}
Pairs = {(1 2), (2 4)}
Output:
2
Explanation:
There is only one exit room i.e. at room2.
So at beginning Rahul is at room1 as
always. As he performs 1st movement,
he would reach at room2. And now any
other movement will not affect the position
of Rahul. Hence Final position Room2.
 
Example 2:
Input:
N = 7, M = 3, K = 4
A[] = {3, 4, 6}
Pairs[] = {(1 2), (2 5), (5 7), (7 1)}
Output:
1
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function lastRoom() which takes the array A[], its size M, vector pair vp[], its size K and an integer N as inputs and returns one integer denoting the room number outside which Rahul is standing.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
2 ≤  N ≤ 1000
1  ≤  M ≤ N
1 ≤  K ≤ 1000
1  ≤  A[i]  ≤  N
1  ≤  pair[i].first , pair[i].second ≤ N
"""

def find_last_room(N, M, K, A, Pairs):
    current_room = 1
    for pair in Pairs:
        if current_room == pair[0]:
            current_room = pair[1]
            if current_room in A and current_room != 1:
                break
        elif current_room == pair[1]:
            current_room = pair[0]
            if current_room in A and current_room != 1:
                break
    return current_room