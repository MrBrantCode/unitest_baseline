"""
QUESTION:
Everyone knows that long ago on the territory of present-day Berland there lived Bindian tribes. Their capital was surrounded by n hills, forming a circle. On each hill there was a watchman, who watched the neighbourhood day and night.

In case of any danger the watchman could make a fire on the hill. One watchman could see the signal of another watchman, if on the circle arc connecting the two hills there was no hill higher than any of the two. As for any two hills there are two different circle arcs connecting them, the signal was seen if the above mentioned condition was satisfied on at least one of the arcs. For example, for any two neighbouring watchmen it is true that the signal of one will be seen by the other.

An important characteristics of this watch system was the amount of pairs of watchmen able to see each other's signals. You are to find this amount by the given heights of the hills.

Input

The first line of the input data contains an integer number n (3 ≤ n ≤ 106), n — the amount of hills around the capital. The second line contains n numbers — heights of the hills in clockwise order. All height numbers are integer and lie between 1 and 109.

Output

Print the required amount of pairs.

Examples

Input

5
1 2 4 5 3


Output

7
"""

def count_visible_pairs(n, heights):
    pairs = 0
    (highest, at) = max(((h, k) for (k, h) in enumerate(heights)))
    last = highest
    count = 0
    p = list()
    push = p.append
    pop = p.pop
    
    for at in range(at - 1, at - n, -1):
        current = heights[at]
        while current > last:
            pairs += count
            (last, count) = pop()
        if current == last:
            count += 1
            pairs += count
        else:
            pairs += 1
            push((last, count))
            last = current
            count = 1
    
    push((last, count))
    end = len(p)
    pairs += sum((p[k][1] for k in range(1 if p[0][1] else 2, end)))
    
    return pairs