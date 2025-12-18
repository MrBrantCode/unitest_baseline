"""
QUESTION:
A group of tourists is going to kayak and catamaran tour. A rented lorry has arrived to the boat depot to take kayaks and catamarans to the point of departure. It's known that all kayaks are of the same size (and each of them occupies the space of 1 cubic metre), and all catamarans are of the same size, but two times bigger than kayaks (and occupy the space of 2 cubic metres).

Each waterborne vehicle has a particular carrying capacity, and it should be noted that waterborne vehicles that look the same can have different carrying capacities. Knowing the truck body volume and the list of waterborne vehicles in the boat depot (for each one its type and carrying capacity are known), find out such set of vehicles that can be taken in the lorry, and that has the maximum total carrying capacity. The truck body volume of the lorry can be used effectively, that is to say you can always put into the lorry a waterborne vehicle that occupies the space not exceeding the free space left in the truck body.

Input

The first line contains a pair of integer numbers n and v (1 ≤ n ≤ 105; 1 ≤ v ≤ 109), where n is the number of waterborne vehicles in the boat depot, and v is the truck body volume of the lorry in cubic metres. The following n lines contain the information about the waterborne vehicles, that is a pair of numbers ti, pi (1 ≤ ti ≤ 2; 1 ≤ pi ≤ 104), where ti is the vehicle type (1 – a kayak, 2 – a catamaran), and pi is its carrying capacity. The waterborne vehicles are enumerated in order of their appearance in the input file.

Output

In the first line print the maximum possible carrying capacity of the set. In the second line print a string consisting of the numbers of the vehicles that make the optimal set. If the answer is not unique, print any of them.

Examples

Input

3 2
1 2
2 7
1 3


Output

7
2
"""

def maximize_carrying_capacity(n, v, vehicles):
    a = []
    b = []
    
    for i, (typ, carry) in enumerate(vehicles):
        if typ == 1:
            a.append([carry, i + 1])
        else:
            b.append([carry, i + 1])
    
    a.sort(reverse=True, key=lambda x: x[0])
    b.sort(reverse=True, key=lambda x: x[0])
    
    for i in range(1, len(a)):
        a[i][0] += a[i - 1][0]
    
    for i in range(1, min(len(b), v // 2)):
        b[i][0] += b[i - 1][0]
    
    res = [0, 0, 0]
    r = range(0, min(v, len(a)) + 1)
    
    for i in r:
        j = min((v - i) // 2, len(b))
        v1 = a[i - 1][0] if i else 0
        v2 = b[j - 1][0] if j else 0
        
        if res[0] < v1 + v2:
            res = [v1 + v2, i, j]
    
    max_capacity = res[0]
    vehicle_indices = []
    
    if res[1]:
        vehicle_indices.extend([a[i][1] for i in range(res[1])])
    
    if res[2]:
        vehicle_indices.extend([b[i][1] for i in range(res[2])])
    
    return max_capacity, vehicle_indices