"""
QUESTION:
Lesha plays the recently published new version of the legendary game hacknet. In this version character skill mechanism was introduced. Now, each player character has exactly n skills. Each skill is represented by a non-negative integer ai — the current skill level. All skills have the same maximum level A.

Along with the skills, global ranking of all players was added. Players are ranked according to the so-called Force. The Force of a player is the sum of the following values:

  * The number of skills that a character has perfected (i.e., such that ai = A), multiplied by coefficient cf.
  * The minimum skill level among all skills (min ai), multiplied by coefficient cm. 



Now Lesha has m hacknetian currency units, which he is willing to spend. Each currency unit can increase the current level of any skill by 1 (if it's not equal to A yet). Help him spend his money in order to achieve the maximum possible value of the Force.

Input

The first line of the input contains five space-separated integers n, A, cf, cm and m (1 ≤ n ≤ 100 000, 1 ≤ A ≤ 109, 0 ≤ cf, cm ≤ 1000, 0 ≤ m ≤ 1015).

The second line contains exactly n integers ai (0 ≤ ai ≤ A), separated by spaces, — the current levels of skills.

Output

On the first line print the maximum value of the Force that the character can achieve using no more than m currency units.

On the second line print n integers a'i (ai ≤ a'i ≤ A), skill levels which one must achieve in order to reach the specified value of the Force, while using no more than m currency units. Numbers should be separated by spaces.

Examples

Input

3 5 10 1 5
1 3 1


Output

12
2 5 2 


Input

3 5 10 1 339
1 3 1


Output

35
5 5 5 

Note

In the first test the optimal strategy is to increase the second skill to its maximum, and increase the two others by 1.

In the second test one should increase all skills to maximum.
"""

def calculate_max_force(n, A, cf, cm, m, skills):
    def force(cf, cm, f, m):
        return f * cf + m * cm

    def mtable(sa):
        mt = [0] * len(sa)
        for i in range(1, len(sa)):
            mt[i] = mt[i - 1] + i * (sa[i] - sa[i - 1])
        return mt

    def maxm(sa, mt, f, k):
        i = bs.bisect_right(mt, k, hi=len(sa) - f)
        return sa[i - 1] + (k - mt[i - 1]) // i

    def optimize(a, amax, cf, cm, k):
        if sum(a) + k >= len(a) * amax:
            return (len(a) * cf + amax * cm, len(a), amax)
        sa = sorted(a)
        f = 0
        while sa[-f - 1] == amax:
            f += 1
        mt = mtable(sa)
        of = f
        om = maxm(sa, mt, f, k)
        o = force(cf, cm, of, om)
        while k >= amax - sa[-f - 1]:
            k -= amax - sa[-f - 1]
            f += 1
            m = maxm(sa, mt, f, k)
            t = force(cf, cm, f, m)
            if t > o:
                (of, om, o) = (f, m, t)
        return (o, of, om)

    def apply(a, amax, of, om):
        a_ = [max(om, ai) for ai in a]
        h = [(-a[i], i) for i in range(len(a))]
        hq.heapify(h)
        for _ in range(of):
            (_, i) = hq.heappop(h)
            a_[i] = amax
        return a_

    (t, of, om) = optimize(skills, A, cf, cm, m)
    if of == len(skills):
        return (t, [A] * len(skills))
    else:
        return (t, apply(skills, A, of, om))