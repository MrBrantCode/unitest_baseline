"""
QUESTION:
B-Mansion and courier

Problem Statement

Taro lives alone in a mansion. Taro, who loves studying, intends to study in his study in the house today. Taro can't concentrate outside the study, so he always studies in the study.

However, on this day, $ N $ of courier service to Taro arrived. $ i $ ($ 1 \ leq i \ leq N $) The arrival time of the third courier is $ a_i $. It is painful to have the delivery person wait at the front door, so Taro decided to be at the front door by the time the courier arrives. Due to the large size of the mansion, it takes $ M $ one way to move between the study and the entrance.

On the other hand, Taro wants to study for as long as possible. Find the maximum amount of time Taro can study in the study from time $ 0 $ to time $ T $.

Taro is in the study at time $ 0 $, and the courier does not arrive earlier than the time $ M $, and the courier does not arrive later than the time $ T $. Also, the time it takes for Taro to receive the courier can be ignored.

Input

Each dataset consists of two lines. The first line consists of three integers $ N, M, T $ separated by blanks. These integers satisfy $ 1 \ leq N \ leq 100 $, $ 1 \ leq M \ leq 10 {,} 000 $, $ 1 \ leq T \ leq 10 {,} 000 $. The second line consists of $ N $ integers $ a_1, a_2, \ dots, a_N $ separated by blanks. Each $ a_i $ fills $ M \ leq a_i \ leq T $ and is also $ a_i <a_ {i + 1} $ ($ 1 \ leq i <N $).

Output

Output an integer representing the maximum amount of time Taro can study on one line.

Sample Input 1


1 1 5
3

Output for the Sample Input 1


3

Sample Input 2


2 1 10
2 7

Output for the Sample Input 2


6

Sample Input 3


2 4 10
6 8

Output for the Sample Input 3


2





Example

Input

1 1 5
3


Output

3
"""

def calculate_max_study_time(N, M, T, arrival_times):
    study = 0
    state = 0
    now = 0
    
    for a in arrival_times:
        if state == 0:
            if M < a - now:
                study += a - now - M
            now = a
            state = 1
        elif state == 1:
            if 2 * M < a - now:
                study += a - now - 2 * M
            now = a
    
    if T - M - arrival_times[-1] > 0:
        study += T - M - arrival_times[-1]
    
    return study