"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

The apocalyptic demon Kali is on a rampage. The ground shudders under his feet, trees shrivel and animals and birds scurry away from his path. In order to save the universe from devastation, all the devtas led by devraj Indra decide to meditate to please Lord Vishnu so that he appears in the form of Kalki, his last avatar, and kill the demon.

Each devta can sit in meditation at a particular place on Swarglok (the heaven). Considering Swarglok as a 2-dimensional plane, the position of each devta is a fixed point with integer coordinates. The positions of all the devtas are distinct from each other.

While meditating the devtas connect to each other by means of astral projections - metaphysical threads that connect one devta to another. They must do so in such a way to satisfy two criteria:

Each devta must be able to connect to every other devta by following a path of astral projections.
No subgroup of devtas may be connected by a cycle of astral projections.

In simple terms, the astral projections must form a tree connecting all devtas.

What needs to be optimized ?

Once the devtas have taken their positions and are connected as a single group to start meditation, a ring of influence is formed around each devta. This ring is centered at the position of the devta, and has a radius equal to the Euclidean distance from this devta to the furthest devta directly connected via an astral projection.

Since different devtas have their own supernatural powers (Indra is the rain god, Agni is the fire god,Varuna is the water god, Vayu is the air god , etc), the influence ring of each devta has an adverse effect on all other devtas which lie within or on this ring. In other words, the efficiency of a devta to perform meditation decreases as the number of influence rings that include him increases.

For each devta D_{i}, define C_{i} as the number of influence rings that include or touch D_{i} (including their own). Now devraj Indra wants the devtas to connect in such a manner so as to minimize the maximum value of C_{i} over all devtas. So he has sent a message to Bhulok (the earth) and he needs help from the best programmers on the planet.

------ Input ------ 

The first line contains the number of test cases T.
Each test case starts with an integer N, where N denotes the number of devtas.
Then N lines follow - the i-th such line consists of two integers x_{i} and y_{i}, specifying the coordinates of the i-th devta.
 
------ Output ------ 

For each test case output exactly N-1 lines. Each line should consist of two integers, specifying a pair of devtas between whom an astral projection should be formed.
 
------ Constraints ------ 

$1 ≤ T ≤ 100$
$3 ≤ N ≤ 400$
$-2000 ≤ x _{i} ≤ 2000$
$-2000 ≤ y _{i} ≤ 2000$

Scoring and test data generation 
The score is C, where C = max(C_{i}) for 1 ≤ i ≤ N. The sequence of positions for devtas is generated randomly and the positions are distributed uniformly.

------ Example ------ 

Input:
1
5
-3 0
-1 0
0 1
1 0
2 0

Example of a valid output:
1 2
2 3
3 4
4 5

------ Explanation ------ 

The second devta is connected to two other devtas: the first devta (a distance of 2 away), and the third devta (a distance of sqrt(2) away). The larger of these distances is 2, so the radius of the second devta's ring of influence is 2. We can calculate the other rings similarly.

Here is a diagram with the astral projections represented in red, and all of the influence rings represented in blue.

The second devta lies within three rings of influence - the first devta's, the second devta's himself, and the third devta's. We can calculate the other values similarly:

C_{1} = 2; C_{2} = 3; C_{3} = 3; C_{4} = 4; C_{5} = 2.

The maximum of these values is 4, so you would get a score of 4.

Other possible outputs may result in higher or lower scores. Your objective is to minimize your score.
"""

def minimize_influence_rings(test_cases):
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    results = []
    
    for points in test_cases:
        n = len(points)
        connections = []
        
        for j in range(n - 1):
            min_dist = float('inf')
            closest_devta = None
            
            for k in range(j + 1, n):
                dist = distance(points[j][0], points[j][1], points[k][0], points[k][1])
                if dist < min_dist:
                    min_dist = dist
                    closest_devta = k
            
            connections.append([j + 1, closest_devta + 1])
        
        results.append(connections)
    
    return results