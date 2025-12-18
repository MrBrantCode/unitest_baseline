"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

After IOI Ilya decided to make a business.  He found a social network called "TheScorpyBook.com". It currently has N registered users. As in any social network two users can be friends. Ilya wants the world to be as connected as possible, so he wants to suggest friendship to some pairs of users. He will suggest user u to have a friendship with user v if they are not friends yet and there is a user w who is friends of both of them. Note that u, v and w are different users. Ilya is too busy with IPO these days, so he asks you to count how many friendship suggestions he has to send over his social network.
 
------ Input ------ 

The first line contains an integer number N — the number of users in the network. Next N lines contain N characters each denoting friendship relations. j^{th} character if the i^{th} lines equals one, if users i and j are friends and equals to zero otherwise. This relation is symmetric, i.e. if user a is friend of b then b is also a friend of a.
 
------ Output ------ 

Output a single integer — number of friendship suggestions Ilya has to send.
 
------ Constraints ------ 

$1 ≤ N ≤ 2000$

------ Example ------ 

Input:
4
0111
1000
1000
1000

Output:
6

------ Explanation ------ 

Each of users [2, 3, 4] should receive two friendship suggestions, while user 1 does not need any, since he already has all other users in his friend-list.
"""

def count_friendship_suggestions(n, friendship_matrix):
    # Convert the friendship matrix to a list of integers for bitwise operations
    friendship_bits = [int(row, 2) for row in friendship_matrix]
    
    count = 0
    limit = 0
    
    for i in range(n):
        for j in range(limit):
            if friendship_matrix[i][j] == '0' and i != j and (friendship_bits[i] & friendship_bits[j]):
                count += 2
        limit += 1
    
    return count