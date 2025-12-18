"""
QUESTION:
A team of students from the city S is sent to the All-Berland Olympiad in Informatics. Traditionally, they go on the train. All students have bought tickets in one carriage, consisting of n compartments (each compartment has exactly four people). We know that if one compartment contain one or two students, then they get bored, and if one compartment contain three or four students, then the compartment has fun throughout the entire trip.

The students want to swap with other people, so that no compartment with students had bored students. To swap places with another person, you need to convince him that it is really necessary. The students can not independently find the necessary arguments, so they asked a sympathetic conductor for help. The conductor can use her life experience to persuade any passenger to switch places with some student.

However, the conductor does not want to waste time persuading the wrong people, so she wants to know what is the minimum number of people necessary to persuade her to change places with the students. Your task is to find the number. 

After all the swaps each compartment should either have no student left, or have a company of three or four students. 


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^6) — the number of compartments in the carriage. The second line contains n integers a_1, a_2, ..., a_{n} showing how many students ride in each compartment (0 ≤ a_{i} ≤ 4). It is guaranteed that at least one student is riding in the train.


-----Output-----

If no sequence of swapping seats with other people leads to the desired result, print number "-1" (without the quotes). In another case, print the smallest number of people you need to persuade to swap places.


-----Examples-----
Input
5
1 2 2 4 3

Output
2

Input
3
4 1 1

Output
2

Input
4
0 3 0 4

Output
0
"""

def minimum_persuasions(n, students_per_compartment):
    counts = [0] * 5
    s = 0
    
    for x in students_per_compartment:
        counts[x] += 1
        s += x
    
    if s > 2 and s != 5:
        ans = 0
        
        if counts[1] >= counts[2]:
            ans += counts[2]
            counts[3] += counts[2]
            counts[1] -= counts[2]
            ans += 2 * (counts[1] // 3)
            counts[3] += counts[1] // 3
            counts[1] %= 3
            if counts[3] > 0:
                ans += counts[1]
            elif counts[1] != 0:
                ans += 2
        else:
            ans += counts[1]
            counts[2] -= counts[1]
            ans += 2 * (counts[2] // 3)
            counts[2] %= 3
            if counts[4] > 0:
                ans += counts[2]
            elif counts[2] != 0:
                ans += 2
        
        return ans
    else:
        return -1