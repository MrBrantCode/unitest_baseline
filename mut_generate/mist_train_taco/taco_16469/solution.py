"""
QUESTION:
Nandu is stuck in a maze consisting of N rooms. Each room with room number x has a door leading into room number 2x (if 2x ≤ N) and another door leading into room number 2x+1 (if 2x+1 ≤ N). All these doors are 2-way doors ie. they can be opened from both the sides.

Some of these N rooms have monsters living in them. 

Nandu is currently in room number i . Nandu's only escape from this maze is to somehow reach room number j which contains the magical Wish-Granting Well. The Well will only grant a wish to Nandu if he offers it a single golden coin. Nandu presently has only a single golden coin in his possession. However, if while going from room number i to j he meets a monster, the monster will take away the only golden coin Nandu has and Nandu will never be able to escape from the maze. 

You will be given information about every room telling you whether a monster resides in it or not. You will then be given Q scenarios, each scenario describing the locations i (the room currently Nandu is present in)  and j (the room where the wishing well is present), i and j will vary over different scenarios but the locations of the monsters will remain fixed for all these scenarios. For each of these scenarios, you have to find out whether Nandu can escape from the maze or not.

Input :

The first line consists on N and Q denoting the number of rooms in the maze and the number of different scenarios that will be given to you. The next line consists of N non-space separated integers such that if the kth integer is '0' , there is no monster present in room number k and if the kth integer is '1' , there is a monster present in room number k. The next Q lines are such that each line consists of two space separated integers i and j denoting Nandu's current location and the location of the Wishing Well for  this particular scenario respectively.

Output :

For every scenario print on a new line 'Yes' if Nandu can escape from the maze and 'No' if he cannot escape from the maze. (Quotes for clarity).

Constraints :

1 ≤ N ≤ 100000

1 ≤ Q ≤ 100000

1 ≤ i,j ≤ N

Author : Shreyans

Tester : Sayan

(By IIT Kgp HackerEarth Programming Club)

SAMPLE INPUT
3 9
001
1 2
1 3
3 2
2 1
2 3
3 1
1 1
2 2
3 3

SAMPLE OUTPUT
Yes
No
No
Yes
No
No
Yes
Yes
No

Explanation

A monster is present only in room number 3. 

Scenario 1 : Nandu is initially present in room number 1 and the Wish-Granting Well is present in room number 2 . Since there is no monster in either of the rooms Nandu goes from 1 -> 2 without losing his golden coin. Hence Nandu can escape the maze by making a wish to the Wish-Granting Well

Scenario 2 : Nandu goes from 1 -> 3. However, there is a monster present in room number 3, which takes away his only golden coin before he can make a wish to the Wish-Granting Well. Hence Nandu cannot escape the maze.
"""

import math

def can_nandu_escape(N, Q, monster_info, scenarios):
    # Precompute the parent room for each room
    array = []
    for j in range(N):
        i = j + 1
        if i == 1:
            array.append(-1)
        elif i % 2 == 0:
            array.append(i // 2)
        else:
            array.append((i - 1) // 2)
    
    results = []
    
    for start, final in scenarios:
        level_start = int(math.log(start, 2)) + 1
        level_final = int(math.log(final, 2)) + 1
        done = 0
        
        if level_final < level_start:
            while level_start != level_final:
                if monster_info[start - 1] == '1':
                    results.append("No")
                    done = 1
                    break
                else:
                    start = array[start - 1]
                    level_start -= 1
        elif level_final > level_start:
            while level_start != level_final:
                if monster_info[final - 1] == '1':
                    results.append("No")
                    done = 1
                    break
                else:
                    final = array[final - 1]
                    level_final -= 1
        
        if done == 0:
            while final != start:
                if monster_info[final - 1] == '1' or monster_info[start - 1] == '1':
                    results.append("No")
                    done = 1
                    break
                else:
                    final = array[final - 1]
                    start = array[start - 1]
            
            if done == 0 and monster_info[start - 1] == '1':
                results.append("No")
            elif done == 0:
                results.append("Yes")
    
    return results