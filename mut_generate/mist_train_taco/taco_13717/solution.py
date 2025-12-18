"""
QUESTION:
Every Friday Chef and his N - 1 friends go for a party. At these parties, they play board games. This Friday, they are playing a game named "Boats! Boats! Boats!". In this game players have to transport cookies between Venice and Constantinople. Each player has a personal storage. The players are numbered from 1 to N, Chef is numbered 1. Rules for determining a winner are very difficult, therefore Chef asks you to write a program, which will determine who is a winner. 

There are 6 types of cookies. For each cookie in the storage player gets 1 point. Also player gets additional points if he packs his cookies in some boxes as follows: 

- A box containing 4 different types of cookies fetches 1 additional point.
- A box containing 5 different types of cookies fetches 2 additional points.
- A box containing 6 different types of cookies fetches 4 additional points.

Obviously a cookie can be put into a single box.

For each player, you know the number of cookies in his storage (denoted by c[i]), also the types of cookies in the storage given denoted by type[i][j].

Your task is to determine the winner of this game. Output "tie" if there are two or more players with same maximum score, "chef" if only Chef has a maximum score, winner's index in all other cases.

-----Input-----

The first line of input contains a single integer T denoting the number of test cases. This will be followed by T test cases.
The first line of each test case contains an integer N denoting the number of players.
The second line of each test case contains an integer c[i] denoting the number of cookies in the i-th storage, followed by c[i] space-separated integers type[i][j] which denote the type if j-th cookie in the storage i-th.

-----Output-----
For each test case, output a single line containing the answer as specified in the statement.

-----Constraints and Subtasks-----Subtask #1 : (20 points)  

- 1 ≤ T ≤ 10 
- 1 ≤  N  ≤ 100  
- 1 ≤  c[i]  ≤  100  
- 1 ≤  type[i][j]  ≤  3   
Subtask #2 : (80 points)  

- 1 ≤ T ≤ 10 
- 1 ≤  N  ≤ 100  
- 1 ≤  c[i]  ≤  100  
- 1 ≤  type[i][j]  ≤  6  

-----Example-----
Input:
3
2
6 1 2 3 4 5 6
9 3 3 3 4 4 4 5 5 5
2
5 2 3 4 5 6
7 1 1 2 2 3 3 4
3
4 1 1 2 3
4 1 2 2 3
4 1 2 3 3
Output:
chef
2
tie

-----Explanation-----
Example case 1.
Chef has total 6 cookie, so he gets 6 points for that. Also, he can put all his cookies (as they are all distinct) in a bag of size 6. It will fetch him additional 4 points. So, Chef's total points will be 10.
The second player has 9 cookies, he gets 9 points for that. Other than this, he can't create a bag with either 4, 5 or 6 distinct cookies. So, his final score is 9.
10 > 9 - Chef wins.
Example case 2.
Chef has 5 + 2 (a bag with 5 different cookies) = 7.
The second player has 7 + 1(a bag with 4 different cookies) = 8.
7 < 8 - the second player wins.
Example case 3.
Every player has 4 cookies and can't create any bag of sweets. So, it's a tie.
"""

def determine_winner(T, test_cases):
    results = []
    
    for test_case in test_cases:
        N = test_case[0]
        players = test_case[1:]
        
        max_score = -1
        winner_index = -2
        
        for i in range(N):
            storage = players[i]
            c = storage[0]
            types = storage[1:]
            
            # Calculate base score (number of cookies)
            score = c
            
            # Calculate additional points for boxes
            type_counts = [0] * 7  # Since types are 1 to 6, we use 7 slots
            for t in types:
                type_counts[t] += 1
            
            # Check for boxes with 4, 5, and 6 different types
            for box_size in range(4, 7):
                while True:
                    distinct_types = sum(1 for x in type_counts if x > 0)
                    if distinct_types >= box_size:
                        score += 1 if box_size == 4 else (2 if box_size == 5 else 4)
                        for t in range(1, 7):
                            if type_counts[t] > 0:
                                type_counts[t] -= 1
                    else:
                        break
            
            # Determine the winner
            if score > max_score:
                max_score = score
                winner_index = i + 1
            elif score == max_score:
                winner_index = -2
        
        if winner_index == -2:
            results.append('tie')
        elif winner_index == 1:
            results.append('chef')
        else:
            results.append(str(winner_index))
    
    return results