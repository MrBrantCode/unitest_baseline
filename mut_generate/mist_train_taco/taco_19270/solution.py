"""
QUESTION:
We take a line segment of length $\textbf{C}$ on a one-dimensional plane and bend it to create a circle with circumference $\textbf{C}$ that's indexed from $0$ to $\boldsymbol{c-1}$. For example, if $c=4$:

We denote a pair of points, $a$ and $\boldsymbol{b}$, as $\rho(a,b)$. We then plot $n$ pairs of points (meaning a total of $2\cdot n$ individual points) at various indices along the circle's circumference. We define the distance $d(a,b)$ between points $a$ and $\boldsymbol{b}$ in pair $\rho(a,b)$ as $min(|a-b|,c-|a-b|)$.

Next, let's consider two pairs: $\rho(a_i,b_i)$ and $\rho(a_j,b_j)$. We define distance $d(\rho(a_i,b_i),\rho(a_j,b_j))$ as the minimum of the six distances between any two points among points $a_i$, $b_i$, $a_j$, and $b_j$. In other words: 
$d(\rho_i,\rho_j)=min(d(a_i,a_j),d(a_i,b_i),d(a_i,b_j),d(b_i,b_j),d(a_j,b_i),d(a_j,b_j))$

For example, consider the following diagram in which the relationship between points in pairs at non-overlapping indices is shown by a connecting line:

Given $n$ pairs of points and the value of $\textbf{C}$, find and print the maximum value of $d(\rho_i,\rho_j)$, where $i\neq j$, among all pairs of points.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of pairs of points) and $\textbf{C}$ (the circumference of the circle). 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains two space-separated integers describing the values of $a_i$ and $b_i$ (i.e., the locations of the points in pair $\boldsymbol{i}$).

Constraints

$1\leq c\leq10^6$
$2\leq n\leq10^5$
$0\leq a,b<c$

Output Format

Print a single integer denoting the maximum $d(\rho_i$, $\rho_j)$, where $i\neq j$.

Sample Input 0
5 8
0 4
2 6
1 5
3 7
4 4

Sample Output 0
2

Explanation 0

In the diagram below, the relationship between points in pairs at non-overlapping indices is shown by a connecting line:

As you can see, the maximum distance between any two pairs of points is $2$, so we print $2$ as our answer.

Sample Input 1
2 1000
0 10
10 20

Sample Output 1
0

Explanation 1

In the diagram below, we have four individual points located at three indices:

Because two of the points overlap, the minimum distance between the two pairs of points is $0$. Thus, we print $0$ as our answer.
"""

def find_max_pair_distance(n, c, pairs):
    def primary_distance(a, b, c):
        return min(abs(a - b), c - abs(a - b))

    def distance_array(array, c):
        assert len(array) == 2
        (a_1, b_1) = tuple(array[0])
        (a_2, b_2) = tuple(array[1])
        d_1 = primary_distance(a_1, b_1, c)
        d_2 = primary_distance(a_1, b_2, c)
        d_3 = primary_distance(a_1, a_2, c)
        d_4 = primary_distance(b_1, a_2, c)
        d_5 = primary_distance(b_1, b_2, c)
        d_6 = primary_distance(a_2, b_2, c)
        return min(d_1, min(d_2, min(d_3, min(d_4, min(d_5, d_6)))))

    def distance_fe(array, c, f_element):
        maximum = 0
        for couple in array:
            distance = distance_array([f_element, couple], c)
            if distance > maximum:
                maximum = distance
        return maximum

    def point_dist(array, c):
        global_min = 0
        common_info = {}
        array2 = copy.deepcopy(array)
        for (indice, couple_i) in enumerate(array):
            (a_i, b_i) = (couple_i[0], couple_i[1])
            try:
                common_info[a_i, b_i]
            except KeyError:
                common_info[a_i, b_i] = primary_distance(a_i, b_i, c)
            for couple_j in array[indice + 1:]:
                (a_j, b_j) = (couple_j[0], couple_j[1])
                d_1 = common_info[a_i, b_i]
                d_2 = primary_distance(a_i, b_j, c)
                d_3 = primary_distance(a_i, a_j, c)
                d_4 = primary_distance(b_i, a_j, c)
                d_5 = primary_distance(b_i, b_j, c)
                try:
                    d_6 = common_info[a_j, b_j]
                except KeyError:
                    d_6 = primary_distance(a_j, b_j, c)
                    common_info[a_j, b_j] = d_6
                global_min = max(global_min, min(d_1, min(d_2, min(d_3, min(d_4, min(d_5, d_6))))))
        return global_min

    return point_dist(pairs, c)