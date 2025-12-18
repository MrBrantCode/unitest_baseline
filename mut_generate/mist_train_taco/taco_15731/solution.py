"""
QUESTION:
Dr. A of the Aizu Institute of Biological Research discovered a mysterious insect on a certain southern island. The shape is elongated like a hornworm, but since one segment is shaped like a ball, it looks like a beaded ball connected by a thread. What was strange was that there were many variations in body color, and some insects changed their body color over time. It seems that the color of the somites of all insects is limited to either red, green or blue, but the color of the somites changes every second, and finally all the somites become the same color and settle down. In some cases, the color seemed to keep changing no matter how long I waited.

<image>



As I investigated, I found that all the body segments usually have the same color, but after being surprised or excited by something, the color of the body segments changes without permission. It turns out that once the color of the segment changes, it will continue to change until all the segment are the same color again.

Dr. A was curiously observing how the color changed when he caught and excited many of these insects, but the way the color changed during the color change is as follows. I noticed that there is regularity.

* The color changes only in one pair of two adjacent somites of different colors, and the colors of the other somites do not change. However, when there are multiple such pairs, it is not possible to predict in advance which pair will change color.
* Such a pair will change to a color that is neither of the colors of the two segmentes at the same time (for example, if the green and red segment are adjacent, they will change to blue at the same time).

<image>



The figure above shows all the changes in the color of the insects up to 2 seconds later. Suppose you have an insect that has the color shown in the upper part of the figure. At this time, there are 3 pairs of adjacent somites of different colors, so after 1 second, it will change to one of the 3 colors drawn side by side in the middle row. After 1 second, all the segments can turn green after 2 seconds (second from the left in the lower row of the figure) when they change to the two on the left side of the middle row. On the other hand, when it changes like the one on the far right in the middle row after 1 second, all the segments do not change to the same color after 2 seconds.

He decided to predict if all the insect segments in front of him could be the same color, and if so, at the earliest, how many seconds later.

Create a program that takes the color sequence of the insect body segments in front of you as input and outputs the shortest time required for all the insect body segments to have the same color in seconds. However, if there is no possibility that the colors will be the same, output "NA (half-width uppercase letters)". In addition, the color sequence of the insect body segment is represented by a character string consisting of r (red), g (green), and b (blue) of 2 or more and 10 or less.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. For each dataset, one string is given on one line that represents information about the insect's somites.

The number of datasets does not exceed 100.

Output

For each dataset, the minimum time (integer in seconds) or NA required for all segment colors to be the same is output on one line.

Example

Input

rbgrg
rbbgbbr
bgr
bgrbrgbr
bggrgbgrr
gbrggrbggr
rrrrr
bgbr
0


Output

5
7
1
6
NA
8
0
4
"""

from collections import deque

def new_color(s, i, rgb):
    for color in rgb:
        if color != s[i] and color != s[i + 1]:
            break
    return s[:i] + color * 2 + s[i + 2:]

def find_minimum_time_to_uniform_color(s):
    length = len(s)
    monos = ['r' * length, 'g' * length, 'b' * length]
    if s in monos:
        return 0
    
    dic = {s: 0}
    rgb = 'rgb'
    que = deque()
    app = que.append
    pop = que.popleft
    que.append((s, 0))
    
    while que:
        (colors, score) = pop()
        score += 1
        temp = colors[0]
        for i in range(1, length):
            ci = colors[i]
            if ci != temp:
                new = new_color(colors, i - 1, rgb)
                if new in monos:
                    return score
                if new not in dic:
                    dic[new] = score
                    app((new, score))
            temp = ci
    
    return 'NA'