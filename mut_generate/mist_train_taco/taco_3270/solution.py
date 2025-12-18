"""
QUESTION:
Cat Noku recently picked up construction working as a hobby. He's currently working with a row of buildings and would like to make it beautiful.

There are n buildings in a row. The height of the i-th building is xi.

Cat Noku can modify the buildings by adding or removing floors to change the heights.
It costs him P dollars to increase the height of one building by 1, and M dollars to lower the height of one building by 1. Note that the heights of all the buildlings must remain integers (i.e. Cat Noku cannot choose to raise the height of a building by 0.5).

At the end of the day Cat Noku will get a bonus for the number of buildings which are adjacent and have the same height. For each section i, if section i+1 has the same height, Cat Noku will gain a profit of S (of course, it is not possible to get this bonus for the last building in the row).
Thus, his net profit can be described by his total profit minus the cost it took him to change the building heights.

Help Cat Noku determine the maximum possible net profit he can gain.

 Input format: 
The first line will contain four space separated integers n, S, M, P.
The second line will contain n space separated integers. The i-th integer in this line will be equal to xi.

 Output format: 
Print a single integer on its own line, the maximum net profit that Cat Noku can earn.

 Constraints: 
For all subtasks:
2 ≤ n 
1 ≤ xi
1 ≤ S, M, P

Subtask 1 (56 pts):  
n ≤ 5 
xi ≤ 10 
S, M, P ≤ 100 

 Subtask 2 (32 pts):  
n ≤ 50 
xi ≤ 100 
S, M, P ≤ 1,000

 Subtask 3 (12 pts):  
n ≤ 2,500 
xi ≤ 1,000,000 
S, M, P ≤ 1,000,000,000 

SAMPLE INPUT
5 4 2 1
1 2 1 5 4

SAMPLE OUTPUT
9

Explanation

In this case, we have 5 buildings with heights 1,2,1,5,4. Cat Noku will get a bonus of 4 for adjacent buildings with the same height. It costs 2 dollars to lower the height of a building by 1, and 1 dollar to raise the height by 1.

One optimal solution is to modify the buildings heights to be 1,1,1,5,5. This costs 2+1=3 dollars. Cat Noku gets the bonus 3 times (i.e. the first, second and fourth buildings qualify for the bonus). Thus, his gross profit is 3*4=12. His net profit is 12-3=9 in this case.
"""

def calculate_max_net_profit(n, S, M, P, heights):
    def convert(cand_val, target_val, S, M, P):
        if cand_val < target_val:
            return S - P * (target_val - cand_val)
        elif cand_val > target_val:
            return S - M * (cand_val - target_val)
        else:
            return S

    def findMax(max_arr, heights, ind, S, M, P):
        max_ind = len(max_arr) - 1
        cur_max = max_arr[max_ind]
        temp_ind = ind + 1
        max_ind -= 1
        cur_val = 0
        while max_ind > -1:
            cur_val += convert(heights[temp_ind], heights[ind], S, M, P) 
            temp_val = cur_val + max_arr[max_ind]
            max_ind -= 1
            temp_ind += 1
            if temp_val > cur_max:
                cur_max = temp_val
        return cur_max

    val_map = dict()
    max_arr = [0]
    for ind in range(len(heights)-1, -1, -1):
        if len(val_map) == 0:
            val_map[heights[ind]] = 0
            max_arr.append(0)
        else:
            max_val = 0
            for key in val_map:
                val_map[key] += convert(heights[ind], key, S, M, P)
                if val_map[key] > max_val:
                    max_val = val_map[key]
            val_map[heights[ind]] = findMax(max_arr, heights, ind, S, M, P)
            if val_map[heights[ind]] > max_val:
                max_val = val_map[heights[ind]]
            max_arr.append(max_val)
    return max_arr[len(max_arr) - 1]