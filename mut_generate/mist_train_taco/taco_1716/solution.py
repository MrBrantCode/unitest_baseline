"""
QUESTION:
Heidi found out that the Daleks have created a network of bidirectional Time Corridors connecting different destinations (at different times!). She suspects that they are planning another invasion on the entire Space and Time. In order to counter the invasion, she plans to deploy a trap in the Time Vortex, along a carefully chosen Time Corridor. She knows that tinkering with the Time Vortex is dangerous, so she consulted the Doctor on how to proceed. She has learned the following:

  * Different Time Corridors require different amounts of energy to keep stable. 
  * Daleks are unlikely to use all corridors in their invasion. They will pick a set of Corridors that requires the smallest total energy to maintain, yet still makes (time) travel possible between any two destinations (for those in the know: they will use a minimum spanning tree). 
  * Setting the trap may modify the energy required to keep the Corridor stable. 



Heidi decided to carry out a field test and deploy one trap, placing it along the first Corridor. But she needs to know whether the Daleks are going to use this corridor after the deployment of the trap. 

She gives you a map of Time Corridors (an undirected graph) with energy requirements for each Corridor.

For a Corridor c, E_{max}(c) is the largest e ≤ 10^9 such that if we changed the required amount of energy of c to e, then the Daleks may still be using c in their invasion (that is, it belongs to some minimum spanning tree). Your task is to calculate E_{max}(c_1) for the Corridor c_1 that Heidi plans to arm with a trap, which is the first edge in the graph.

Input

The first line contains integers n and m (2 ≤ n ≤ 10^5, n - 1 ≤ m ≤ 10^6), number of destinations to be invaded and the number of Time Corridors.

Each of the next m lines describes a Corridor: destinations a, b and energy e (1 ≤ a, b ≤ n, a ≠ b, 0 ≤ e ≤ 10^9).

It's guaranteed, that no pair \\{a, b\} will repeat and that the graph is connected — that is, it is possible to travel between any two destinations using zero or more Time Corridors.

Output

Output a single integer: E_{max}(c_1) for the first Corridor c_1 from the input.

Example

Input

3 3
1 2 8
2 3 3
3 1 4


Output

4

Note

After the trap is set, the new energy requirement for the first Corridor may be either smaller, larger, or equal to the old energy requiremenet.

In the example, if the energy of the first Corridor is set to 4 or less, then the Daleks may use the set of Corridors \{ \{ 1,2 \}, \{ 2,3 \} \} (in particular, if it were set to less than 4, then this would be the only set of Corridors that they would use). However, if it is larger than 4, then they will instead use the set \{ \{2,3\}, \{3,1\} \}.
"""

def calculate_max_energy_for_first_corridor(n, m, corridors):
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, a):
            acopy = a
            while a != self.parent[a]:
                a = self.parent[a]
            while acopy != a:
                (self.parent[acopy], acopy) = (a, self.parent[acopy])
            return a

        def union(self, a, b):
            self.parent[self.find(b)] = self.find(a)

    # Extract the first corridor
    a1, b1, e1 = corridors[0]
    
    # If there are only two destinations or the number of corridors is exactly one less than the number of destinations
    if n == 2 or m + 1 == n:
        return 1000000000

    # Prepare the list of corridors excluding the first one
    remaining_corridors = corridors[1:]
    
    # Sort the remaining corridors by energy
    remaining_corridors.sort(key=lambda x: x[2])
    
    # Initialize UnionFind
    uf = UnionFind(n + 1)
    
    # Initialize the answer with a large value
    ans = 1000000000
    
    # Process each corridor in sorted order
    for aa, bb, cc in remaining_corridors:
        if uf.find(aa) != uf.find(bb):
            uf.union(aa, bb)
        if uf.find(a1) == uf.find(b1):
            ans = cc
            break
    
    return ans