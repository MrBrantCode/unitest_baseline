"""
QUESTION:
Iahub and Sorin are the best competitive programmers in their town. However, they can't both qualify to an important contest. The selection will be made with the help of a single problem. Blatnatalag, a friend of Iahub, managed to get hold of the problem before the contest. Because he wants to make sure Iahub will be the one qualified, he tells Iahub the following task.

You're given an (1-based) array a with n elements. Let's define function f(i, j) (1 ≤ i, j ≤ n) as (i - j)^2 + g(i, j)^2. Function g is calculated by the following pseudo-code:



int g(int i, int j) {

    int sum = 0;

    for (int k = min(i, j) + 1; k <= max(i, j); k = k + 1)

        sum = sum + a[k];

    return sum;

}



Find a value min_{i} ≠ j  f(i, j).

Probably by now Iahub already figured out the solution to this problem. Can you?


-----Input-----

The first line of input contains a single integer n (2 ≤ n ≤ 100000). Next line contains n integers a[1], a[2], ..., a[n] ( - 10^4 ≤ a[i] ≤ 10^4). 


-----Output-----

Output a single integer — the value of min_{i} ≠ j  f(i, j).


-----Examples-----
Input
4
1 0 0 -1

Output
1

Input
2
1 -1

Output
2
"""

import sys

class splitFeature:
    def __init__(self, position, value):
        self.position = position
        self.value = value

def bruteForce(features, left, right):
    min_distance = sys.maxsize
    for i in range(left, right):
        for j in range(i + 1, right):
            min_distance = min(min_distance, (features[i].position - features[j].position) ** 2 + (features[i].value - features[j].value) ** 2)
    return min_distance

def enhanceData(features, left, right, mid, min_distance):
    selected_population = []
    for i in range(left, right):
        if (features[i].position - features[mid].position) ** 2 <= min_distance:
            selected_population.append(features[i])
    selected_population.sort(key=lambda x: x.value)
    l = len(selected_population)
    result = sys.maxsize
    for i in range(l):
        for j in range(i + 1, l):
            if (selected_population[i].value - selected_population[j].value) ** 2 >= min_distance:
                break
            distance = (selected_population[i].position - selected_population[j].position) ** 2 + (selected_population[i].value - selected_population[j].value) ** 2
            result = min(result, distance)
    return result

def analyzeData(features, left, right):
    if right - left <= 3:
        return bruteForce(features, left, right)
    mid = (left + right) // 2
    min_distance = min(analyzeData(features, left, mid), analyzeData(features, mid + 1, right))
    return min(min_distance, enhanceData(features, left, right, mid, min_distance))

def find_min_f_value(n, a):
    features = []
    for i in range(n):
        if i > 0:
            a[i] += a[i - 1]
        features.append(splitFeature(i, a[i]))
    return analyzeData(features, 0, n)