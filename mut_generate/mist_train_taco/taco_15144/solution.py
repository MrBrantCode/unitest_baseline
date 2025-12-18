"""
QUESTION:
Aarav has just graduated from the university. Now he is going to travel along his country. More precisely: there are N cities with integer coordinates. His plan is to travel between each pair of the cities. 

The distance between city A with coordinates (x1, y1) and city B with coordinates (x2, y2) is equal to |x1 - x2| + |y1 - y2|.

Now he is interested in the total distance between all the pairs of the cities.

Input
The first line contains one integer N.
The following N lines contain two separated integers (xi, yi) each - coordinates of the corresponding city.

Output
Output one integer - the answer to the question. 
As this number can be very big - output it modulo 10^9 + 7.

Constraints
1 ≤ N ≤ 200 000
|xi|, |yi| ≤ 10^9

SAMPLE INPUT
4
-1 5
1 6
3 5
2 3

SAMPLE OUTPUT
22
"""

def calculate_total_distance(N, coordinates):
    def comp(a):
        t = 0
        res = 0
        for i in range(1, len(a)):
            t += i * (a[i] - a[i-1])
            res += t
        return res

    X = [coord[0] for coord in coordinates]
    Y = [coord[1] for coord in coordinates]
    
    X.sort()
    Y.sort()
    
    total_distance = (comp(X) + comp(Y)) % 1000000007
    return total_distance