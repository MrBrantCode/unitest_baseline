"""
QUESTION:
In Berland, there is the national holiday coming — the Flag Day. In the honor of this event the president of the country decided to make a big dance party and asked your agency to organize it. He has several conditions:  overall, there must be m dances; exactly three people must take part in each dance; each dance must have one dancer in white clothes, one dancer in red clothes and one dancer in blue clothes (these are the colors of the national flag of Berland). 

The agency has n dancers, and their number can be less than 3m. That is, some dancers will probably have to dance in more than one dance. All of your dancers must dance on the party. However, if some dance has two or more dancers from a previous dance, then the current dance stops being spectacular. Your agency cannot allow that to happen, so each dance has at most one dancer who has danced in some previous dance. 

You considered all the criteria and made the plan for the m dances: each dance had three dancers participating in it. Your task is to determine the clothes color for each of the n dancers so that the President's third condition fulfilled: each dance must have a dancer in white, a dancer in red and a dancer in blue. The dancers cannot change clothes between the dances.


-----Input-----

The first line contains two space-separated integers n (3 ≤ n ≤ 10^5) and m (1 ≤ m ≤ 10^5) — the number of dancers and the number of dances, correspondingly. Then m lines follow, describing the dances in the order of dancing them. The i-th line contains three distinct integers — the numbers of the dancers that take part in the i-th dance. The dancers are numbered from 1 to n. Each dancer takes part in at least one dance.


-----Output-----

Print n space-separated integers: the i-th number must represent the color of the i-th dancer's clothes (1 for white, 2 for red, 3 for blue). If there are multiple valid solutions, print any of them. It is guaranteed that at least one solution exists.


-----Examples-----
Input
7 3
1 2 3
1 4 5
4 6 7

Output
1 2 3 3 2 2 1 

Input
9 3
3 6 9
2 5 8
1 4 7

Output
1 1 1 2 2 2 3 3 3 

Input
5 2
4 1 5
3 1 2

Output
2 3 1 1 3
"""

def assign_dancer_colors(n, m, dances):
    colors = [0] * (n + 1)  # Initialize colors array with 0s
    available = [1, 2, 3]  # Available colors: 1 (white), 2 (red), 3 (blue)

    for dance in dances:
        a, b, c = dance
        if colors[a] != 0:
            available.remove(colors[a])
        if colors[b] != 0:
            available.remove(colors[b])
        if colors[c] != 0:
            available.remove(colors[c])

        if len(available) > 0:
            if colors[a] == 0:
                colors[a] = available[0]
                available.remove(colors[a])
            if colors[b] == 0:
                colors[b] = available[0]
                available.remove(colors[b])
            if colors[c] == 0:
                colors[c] = available[0]
                available.remove(colors[c])

        available = [1, 2, 3]  # Reset available colors

    return colors[1:]  # Return the colors for dancers 1 to n