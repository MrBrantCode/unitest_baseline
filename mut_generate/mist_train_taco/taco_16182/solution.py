"""
QUESTION:
This is a story in a depopulated area. In this area, houses are sparsely built along a straight road called Country Road. Until now, there was no electricity in this area, but this time the government will give us some generators. You can install the generators wherever you like, but in order for electricity to be supplied to your home, you must be connected to one of the generators via an electric wire, which incurs a cost proportional to its length. As the only technical civil servant in the area, your job is to seek generator and wire placement that minimizes the total length of wires, provided that electricity is supplied to all homes. Is. Since the capacity of the generator is large enough, it is assumed that electricity can be supplied to as many houses as possible.

Figure 2 shows the first data set of the sample input. To give the optimum placement for this problem, place the generators at the positions x = 20 and x = 80 as shown in the figure, and draw the wires at the positions shown in gray in the figure, respectively.

Example of generator and wire placement (first dataset in input example).
---
Figure 2: Example of generator and wire placement (first dataset in input example).



Input

The number of datasets t (0 <t ≤ 50) is given on the first line of the input.

Subsequently, t datasets are given. Each dataset is given in two lines in the following format.


n k
x1 x2 ... xn


n is the number of houses and k is the number of generators. x1, x2, ..., xn are one-dimensional coordinates that represent the position of the house, respectively. All of these values ​​are integers and satisfy 0 <n ≤ 100000, 0 <k ≤ 100000, 0 ≤ x1 <x2 <... <xn ≤ 1000000.

In addition, 90% of the dataset satisfies 0 <n ≤ 100, 0 <k ≤ 100.

Output

For each dataset, output the minimum total required wire length in one line.

Example

Input

6
5 2
10 30 40 70 100
7 3
3 6 10 17 21 26 28
1 1
100
2 1
0 1000000
3 5
30 70 150
6 4
0 10 20 30 40 50


Output

60
13
0
1000000
0
20
"""

def calculate_minimum_wire_length(t, datasets):
    results = []
    for dataset in datasets:
        n, k, x = dataset
        x.sort()
        diff = []
        for i in range(1, len(x)):
            diff.append(x[i] - x[i - 1])
        diff.sort(reverse=True)
        s = sum(diff[:k - 1])
        min_wire_length = max(x) - min(x) - s
        results.append(min_wire_length)
    return results