"""
QUESTION:
Two neighbours, Alan and Bob, live in the city, where there are three buildings only: a cinema, a shop and the house, where they live. The rest is a big asphalt square. 

Once they went to the cinema, and the film impressed them so deeply, that when they left the cinema, they did not want to stop discussing it.

Bob wants to get home, but Alan has to go to the shop first, and only then go home. So, they agreed to cover some distance together discussing the film (their common path might pass through the shop, or they might walk circles around the cinema together), and then to part each other's company and go each his own way. After they part, they will start thinking about their daily pursuits; and even if they meet again, they won't be able to go on with the discussion. Thus, Bob's path will be a continuous curve, having the cinema and the house as its ends. Alan's path — a continuous curve, going through the shop, and having the cinema and the house as its ends.

The film ended late, that's why the whole distance covered by Alan should not differ from the shortest one by more than t1, and the distance covered by Bob should not differ from the shortest one by more than t2.

Find the maximum distance that Alan and Bob will cover together, discussing the film.

Input

The first line contains two integers: t1, t2 (0 ≤ t1, t2 ≤ 100). The second line contains the cinema's coordinates, the third one — the house's, and the last line — the shop's. 

All the coordinates are given in meters, are integer, and do not exceed 100 in absolute magnitude. No two given places are in the same building.

Output

In the only line output one number — the maximum distance that Alan and Bob will cover together, discussing the film. Output the answer accurate to not less than 4 decimal places.

Examples

Input

0 2
0 0
4 0
-3 0


Output

1.0000000000


Input

0 0
0 0
2 0
1 0


Output

2.0000000000
"""

import math

def calculate_max_common_distance(t1, t2, cinema_coords, house_coords, shop_coords):
    # Convert coordinates to complex numbers
    cinema = complex(*cinema_coords)
    house = complex(*house_coords)
    shop = complex(*shop_coords)
    
    # Calculate distances
    cinema_to_house = abs(house - cinema)
    cinema_to_shop = abs(shop - cinema)
    shop_to_house = abs(house - shop)
    
    # Calculate maximum possible distances for Alan and Bob
    alice_max = cinema_to_shop + shop_to_house + t1
    bob_max = cinema_to_house + t2
    
    def check(d):
        c1, c2, c3 = ((cinema, d), (house, bob_max - d), (shop, alice_max - d - shop_to_house))
        for i in range(3):
            status = intersect(c1, c2)
            if status == 0:
                return False
            if status == 1:
                return intersect(c1 if c1[1] < c2[1] else c2, c3)
            for intersection in status:
                if abs(intersection - c3[0]) - 1e-10 <= c3[1]:
                    return True
            c1, c2, c3 = c2, c3, c1
        return False
    
    def intersect(a, b):
        dif = b[0] - a[0]
        dist = abs(dif)
        if dist > a[1] + b[1] + 1e-10:
            return 0
        if dist <= abs(a[1] - b[1]) - 1e-10:
            return 1
        k = (dist * dist + a[1] * a[1] - b[1] * b[1]) / (2 * dist)
        u = dif * k / dist
        v = dif * 1j / dist * (a[1] * a[1] - k * k) ** 0.5
        return [a[0] + u + v, a[0] + u - v]
    
    # Determine the maximum common distance
    if cinema_to_shop + shop_to_house <= bob_max:
        return min(alice_max, bob_max)
    else:
        lower, upper = 0, min(alice_max, bob_max)
        while upper - lower > 1e-10:
            mid = (lower + upper) * 0.5
            if check(mid):
                lower = mid
            else:
                upper = mid
        return lower