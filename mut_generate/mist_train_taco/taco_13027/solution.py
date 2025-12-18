"""
QUESTION:
This time the Berland Team Olympiad in Informatics is held in a remote city that can only be reached by one small bus. Bus has n passenger seats, seat i can be occupied only by a participant from the city a_{i}.

Today the bus has completed m trips, each time bringing n participants. The participants were then aligned in one line in the order they arrived, with people from the same bus standing in the order of their seats (i. e. if we write down the cities where the participants came from, we get the sequence a_1, a_2, ..., a_{n} repeated m times).

After that some teams were formed, each consisting of k participants form the same city standing next to each other in the line. Once formed, teams left the line. The teams were formed until there were no k neighboring participants from the same city.

Help the organizers determine how many participants have left in the line after that process ended. We can prove that answer doesn't depend on the order in which teams were selected.


-----Input-----

The first line contains three integers n, k and m (1 ≤ n ≤ 10^5, 2 ≤ k ≤ 10^9, 1 ≤ m ≤ 10^9).

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^5), where a_{i} is the number of city, person from which must take seat i in the bus. 


-----Output-----

Output the number of remaining participants in the line.


-----Examples-----
Input
4 2 5
1 2 3 1

Output
12

Input
1 9 10
1

Output
1

Input
3 2 10
1 2 1

Output
0



-----Note-----

In the second example, the line consists of ten participants from the same city. Nine of them will form a team. At the end, only one participant will stay in the line.
"""

def calculate_remaining_participants(n, k, m, a):
    # Convert the list of participants into a list of tuples (city, count)
    a_grouped = []
    last = ('-1', 0)
    a_grouped.append(last)
    
    for ai in a:
        if last[0] == ai:
            last = (ai, last[1] + 1)
            a_grouped[-1] = last
        else:
            last = (ai, 1)
            a_grouped.append(last)
        if last[1] == k:
            a_grouped.pop()
            last = a_grouped[-1]
    
    a_grouped.pop(0)
    
    s1 = 0
    while len(a_grouped) > 0 and a_grouped[0][0] == a_grouped[-1][0]:
        if len(a_grouped) == 1:
            s = a_grouped[0][1] * m
            r1 = s % k
            if r1 == 0:
                return s1 % k
            else:
                return r1 + s1
        
        join = a_grouped[0][1] + a_grouped[-1][1]
        if join < k:
            break
        elif join % k == 0:
            s1 += join
            a_grouped.pop()
            a_grouped.pop(0)
        else:
            s1 += join // k * k
            a_grouped[0] = (a_grouped[0][0], join % k)
            a_grouped.pop()
            break
    
    s = 0
    for ai in a_grouped:
        s += ai[1]
    
    return s * m + s1