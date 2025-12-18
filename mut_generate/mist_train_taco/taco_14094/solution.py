"""
QUESTION:
Artem has an array of n positive integers. Artem decided to play with it. The game consists of n moves. Each move goes like this. Artem chooses some element of the array and removes it. For that, he gets min(a, b) points, where a and b are numbers that were adjacent with the removed number. If the number doesn't have an adjacent number to the left or right, Artem doesn't get any points. 

After the element is removed, the two parts of the array glue together resulting in the new array that Artem continues playing with. Borya wondered what maximum total number of points Artem can get as he plays this game.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 5·10^5) — the number of elements in the array. The next line contains n integers a_{i} (1 ≤ a_{i} ≤ 10^6) — the values of the array elements.


-----Output-----

In a single line print a single integer — the maximum number of points Artem can get.


-----Examples-----
Input
5
3 1 5 2 6

Output
11

Input
5
1 2 3 4 5

Output
6

Input
5
1 100 101 100 1

Output
102
"""

def calculate_max_points(n, cards):
    score = 0
    preIndexes = []
    nextIndexes = []
    isChosen = [0] * n
    chosens = []
    
    # Initialize preIndexes and nextIndexes
    nextIndexes.append(1)
    preIndexes.append(-1)
    for i in range(1, n - 1):
        if cards[i] <= cards[i - 1] and cards[i] <= cards[i + 1]:
            chosens.append((-cards[i], i))
            isChosen[i] = 1
        preIndexes.append(i - 1)
        nextIndexes.append(i + 1)
    preIndexes.append(n - 2)
    nextIndexes.append(n)
    
    # Process the chosens list
    while len(chosens) != 0:
        chosen = chosens.pop()
        preChosen = preIndexes[chosen[1]]
        nextChosen = nextIndexes[chosen[1]]
        score += min(cards[preChosen], cards[nextChosen])
        nextIndexes[preChosen] = nextChosen
        preIndexes[nextChosen] = preChosen
        
        if preChosen != 0 and preIndexes[preChosen] != -1 and (nextIndexes[preChosen] != n):
            if cards[preChosen] <= cards[preIndexes[preChosen]] and cards[preChosen] <= cards[nextIndexes[preChosen]]:
                if isChosen[preChosen] == 0:
                    isChosen[preChosen] = 1
                    chosens.append((-cards[preChosen], preChosen))
        
        if nextChosen != n - 1 and preIndexes[nextChosen] != -1 and (nextIndexes[nextChosen] != n):
            if cards[nextChosen] <= cards[preIndexes[nextChosen]] and cards[nextChosen] <= cards[nextIndexes[nextChosen]]:
                if isChosen[nextChosen] == 0:
                    isChosen[nextChosen] = 1
                    chosens.append((-cards[nextChosen], nextChosen))
    
    # Final pass to calculate remaining points
    tempNode = nextIndexes[0]
    while tempNode != n and tempNode != n - 1:
        score += min(cards[preIndexes[tempNode]], cards[nextIndexes[tempNode]])
        tempNode = nextIndexes[tempNode]
    
    return score