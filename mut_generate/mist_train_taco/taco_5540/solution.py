"""
QUESTION:
In 1862, the lord of Aizu was ordered to serve as a guardian of Kyoto. The Kyoto Shugoshoku is an important role to protect Kyoto at the end of the Edo period when security has deteriorated. You have to patrol the city by sharing it with the shogunate and other clan. However, when it came time to decide the sharing route, the following order was received from a stubborn old man who is famous among his vassals.

<image>


It was a big deal. Even the lord cannot ignore the statement of this vassal. Depending on the selection of the sharing route, it will be "the samurai's face is not noticeable".

So, please make a program to judge whether the above three conditions are met by inputting the information of the start point, the goal point, and the intersection, and give it to the lord.

The start point is represented by 1, the goal point is represented by 2, and other intersections are represented by integers of 3 or more. A road is represented by a set of intersection numbers that the roads connect to. The number of intersections shall be 100 or less, and there shall be one or more routes from all intersections to the start point and goal point.



input

Given multiple datasets. Each dataset is given in the following format:


a1 b1
a2 b2
:
:
0 0


The two integers in each row indicate that there is a road connecting intersection ai and intersection bi. When both ai and bi are 0, it indicates the end of inputting intersection information.

The number of datasets does not exceed 50.

output

For each data set, if the samurai's face stands out (if the three conditions are met), OK, otherwise (if the three conditions are not met), output NG on one line.

Example

Input

1 3
3 4
3 5
3 6
4 6
4 7
4 7
5 6
6 7
5 8
5 8
6 8
6 9
7 9
8 9
9 2
0 0
1 3
3 4
3 4
4 2
0 0


Output

OK
NG
"""

from collections import defaultdict

def check_patrol_route(data_list):
    def is_half_euler_graph(node_list):
        results = []
        for node in node_list:
            isBool = True
            for (dic_key, dic_value) in node.items():
                if dic_key != 1 and dic_key != 2:
                    if dic_value % 2 != 0:
                        isBool = False
                        break
                elif dic_value % 2 == 0:
                    isBool = False
                    break
            if isBool:
                results.append('OK')
            else:
                results.append('NG')
        return results

    node_data_lists = []
    tmp_list = []
    count_lists = []
    tmp_dic = defaultdict(int)

    for i in range(len(data_list)):
        if data_list[i][0] == 0 and data_list[i][1] == 0:
            node_data_lists.append(tmp_list[:])
            tmp_list.clear()
        else:
            tmp_list.append(data_list[i])

    for node_data_list in node_data_lists:
        tmp_dic.clear()
        for i in range(len(node_data_list)):
            tmp_dic[node_data_list[i][0]] += 1
            tmp_dic[node_data_list[i][1]] += 1
        count_lists.append(tmp_dic.copy())

    return is_half_euler_graph(count_lists)