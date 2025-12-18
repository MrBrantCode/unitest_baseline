"""
QUESTION:
This is the story of 20XX. The number of air passengers increased as a result of the stable energy supply by the renewable power network and the invention of liquefied synthetic fuel. However, the threat of terrorism by aircraft still exists, and the importance of fast and highly reliable automatic baggage inspection systems is increasing. Since it is actually difficult for an inspector to inspect all the baggage, we would like to establish a mechanism for the inspector to inspect only the baggage judged to be suspicious by the automatic inspection.

At the request of the aviation industry, the International Cabin Protection Company investigated recent passenger baggage in order to develop a new automated inspection system. As a result of the investigation, it was found that the baggage of recent passengers has the following tendency.

* Baggage is shaped like a rectangular parallelepiped with only one side short.
* Items that ordinary passengers pack in their baggage and bring into the aircraft include laptop computers, music players, handheld game consoles, and playing cards, all of which are rectangular.
* Individual items are packed so that their rectangular sides are parallel to the sides of the baggage.
* On the other hand, weapons such as those used for terrorism have a shape very different from a rectangle.



Based on the above survey results, we devised the following model for baggage inspection. Each piece of baggage is considered to be a rectangular parallelepiped container that is transparent to X-rays. It contains multiple items that are opaque to X-rays. Here, consider a coordinate system with the three sides of the rectangular parallelepiped as the x-axis, y-axis, and z-axis, irradiate X-rays in the direction parallel to the x-axis, and take an image projected on the y-z plane. The captured image is divided into grids of appropriate size, and the material of the item reflected in each grid area is estimated by image analysis. Since this company has a very high level of analysis technology and can analyze even the detailed differences in materials, it can be considered that the materials of the products are different from each other. When multiple items overlap in the x-axis direction, the material of the item that is in the foreground for each lattice region, that is, the item with the smallest x-coordinate is obtained. We also assume that the x-coordinates of two or more items are never equal.

Your job can be asserted that it contains non-rectangular (possibly a weapon) item when given the results of the image analysis, or that the baggage contains anything other than a rectangular item. It is to create a program that determines whether it is presumed that it is not included.

Input

The first line of input contains a single positive integer, which represents the number of datasets. Each dataset is given in the following format.

> H W
> Analysis result 1
> Analysis result 2
> ...
> Analysis result H
>

H is the vertical size of the image, and W is an integer representing the horizontal size (1 <= h, w <= 50). Each line of the analysis result is composed of W characters, and the i-th character represents the analysis result in the grid region i-th from the left of the line. For the lattice region where the substance is detected, the material is represented by uppercase letters (A to Z). At this time, the same characters are used if they are made of the same material, and different characters are used if they are made of different materials. The lattice region where no substance was detected is represented by a dot (.).

For all datasets, it is guaranteed that there are no more than seven material types.

Output

For each data set, output "SUSPICIOUS" if it contains items other than rectangles, and "SAFE" if not, on one line.

Sample Input


6
1 1
..
3 3
...
.W.
...
10 10
..........
.DDDDCC ..
.DDDDCC ..
.DDDDCC ..
ADDDDCCC ..
AAA .. CCC ..
AAABB BBC ..
AAABBBB ...
..BBBBB ...
..........
10 10
..........
.DDDDDD ...
.DDDDCC ..
.DDDDCC ..
ADDDDCCC ..
AAA .. CCC ..
AAABB BBC ..
AAABBBB ...
..BBBBB ...
..........
10 10
R..E..C.T.
R.EEE.C.T.
.EEEEE ....
EEEEEEE ...
.EEEEEEE ..
..EEEEEEE.
... EEEEEEE
.... EEEEE.
..... EEE ..
...... E ...
16 50
.................................................................
......... AAAAAAAAAAAAAAAAA ............................
.... PPP ... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA .....
.... PPP ... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA .....
.... PPP ... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ....
.... PPP .............. AAAAA.AAAAAAAAAAAAAAAA .......
.... PPP ................ A .... AAA.AAAAAAAAAA ........
.... PPP ........... IIIIIAAIIAIII.AAAAAAAAAA ........
..CCCCCCCCCCCCCC ... IIIIIIAAAAAAAAAAAAAAAAAA ........
..CCCCCCCCCCCCCC ... IIIIIIIIIIIII ... AAAAAAAAAAA ......
.... PPP .................. AAAAAAAAAAA .....
MMMMPPPMMMMMMMMMMMMMMM ............. AAAAAAAAAAA ....
MMMMPPPMMMMMMMMMMMMMMM .............. AAAAAAAAAAA ...
MMMMMMMMMMMMMMMMMMMMMM ............... AAAAAAAAAAA ...
MMMMMMMMMMMMMMMMMMMMMM ............... AAAAAAAAAAA ...
MMMMMMMMMMMMMMMMMMMMMM ............................


Output for the Sample Input


SAFE
SAFE
SAFE
SUSPICIOUS
SUSPICIOUS
SUSPICIOUS






Example

Input

6
1 1
.
3 3
...
.W.
...
10 10
..........
.DDDDCCC..
.DDDDCCC..
.DDDDCCC..
ADDDDCCC..
AAA..CCC..
AAABBBBC..
AAABBBB...
..BBBBB...
..........
10 10
..........
.DDDDDD...
.DDDDCCC..
.DDDDCCC..
ADDDDCCC..
AAA..CCC..
AAABBBBC..
AAABBBB...
..BBBBB...
..........
10 10
R..E..C.T.
R.EEE.C.T.
.EEEEE....
EEEEEEE...
.EEEEEEE..
..EEEEEEE.
...EEEEEEE
....EEEEE.
.....EEE..
......E...
16 50
..................................................
.........AAAAAAAAAAAAAAAA.........................
....PPP...AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.....
....PPP...AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.....
....PPP...AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA....
....PPP..............AAAAA.AAAAAAAAAAAAAAAA.......
....PPP................A....AAA.AAAAAAAAAA........
....PPP...........IIIIIAAIIAIII.AAAAAAAAAA........
..CCCCCCCCCCCCC...IIIIIIAAAAAAAAAAAAAAAAAA........
..CCCCCCCCCCCCC...IIIIIIIIIIIII...AAAAAAAAAA......
....PPP............................AAAAAAAAAA.....
MMMMPPPMMMMMMMMMMMMMMM.............AAAAAAAAAAA....
MMMMPPPMMMMMMMMMMMMMMM..............AAAAAAAAAAA...
MMMMMMMMMMMMMMMMMMMMMM...............AAAAAAAAAA...
MMMMMMMMMMMMMMMMMMMMMM...............AAAAAAAAAA...
MMMMMMMMMMMMMMMMMMMMMM............................


Output

SAFE
SAFE
SAFE
SUSPICIOUS
SUSPICIOUS
SUSPICIOUS
"""

def check_baggage_safety(datasets):
    results = []
    
    for dataset in datasets:
        H, W, analysis_results = dataset
        mp = [list(row) for row in analysis_results]
        range_dic = {}
        keys = []
        
        for y in range(H):
            for x in range(W):
                c = mp[y][x]
                if c in range_dic:
                    x1, x2, y1, y2 = range_dic[c]
                    range_dic[c] = (min(x, x1), max(x, x2), min(y, y1), max(y, y2))
                else:
                    range_dic[c] = (x, x, y, y)
                    keys.append(c)
        
        while keys:
            tmp = keys[:]
            for key in keys:
                break_flag = False
                x1, x2, y1, y2 = range_dic[key]
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if not mp[y][x] in (key, '#'):
                            break_flag = True
                            break
                    if break_flag:
                        break
                else:
                    for y in range(y1, y2 + 1):
                        mp[y][x1:x2 + 1] = ['#'] * (x2 - x1 + 1)
                    keys.remove(key)
            if tmp == keys:
                results.append("SUSPICIOUS")
                break
        else:
            results.append("SAFE")
    
    return results