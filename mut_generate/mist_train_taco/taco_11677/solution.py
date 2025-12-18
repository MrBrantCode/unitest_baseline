"""
QUESTION:
Vasya learns to type. He has an unusual keyboard at his disposal: it is rectangular and it has n rows of keys containing m keys in each row. Besides, the keys are of two types. Some of the keys have lowercase Latin letters on them and some of the keys work like the "Shift" key on standard keyboards, that is, they make lowercase letters uppercase.

Vasya can press one or two keys with one hand. However, he can only press two keys if the Euclidean distance between the centers of the keys does not exceed x. The keys are considered as squares with a side equal to 1. There are no empty spaces between neighbouring keys.

Vasya is a very lazy boy, that's why he tries to type with one hand as he eats chips with his other one. However, it is possible that some symbol can't be typed with one hand only, because the distance between it and the closest "Shift" key is strictly larger than x. In this case he will have to use his other hand. Having typed the symbol, Vasya returns other hand back to the chips.

You are given Vasya's keyboard and the text. Count the minimum number of times Vasya will have to use the other hand.

Input

The first line contains three integers n, m, x (1 ≤ n, m ≤ 30, 1 ≤ x ≤ 50).

Next n lines contain descriptions of all the keyboard keys. Each line contains the descriptions of exactly m keys, without spaces. The letter keys are marked with the corresponding lowercase letters. The "Shift" keys are marked with the "S" symbol. 

Then follow the length of the text q (1 ≤ q ≤ 5·105). The last line contains the text T, which consists of q symbols, which are uppercase and lowercase Latin letters.

Output

If Vasya can type the text, then print the minimum number of times he will have to use his other hand. Otherwise, print "-1" (without the quotes).

Examples

Input

2 2 1
ab
cd
1
A


Output

-1


Input

2 2 1
ab
cd
1
e


Output

-1


Input

2 2 1
ab
cS
5
abcBA


Output

1


Input

3 9 4
qwertyuio
asdfghjkl
SzxcvbnmS
35
TheQuIcKbRoWnFOXjummsovertHeLazYDOG


Output

2

Note

In the first sample the symbol "A" is impossible to print as there's no "Shift" key on the keyboard.

In the second sample the symbol "e" is impossible to print as there's no such key on the keyboard.

In the fourth sample the symbols "T", "G" are impossible to print with one hand. The other letters that are on the keyboard can be printed. Those symbols come up in the text twice, thus, the answer is 2.
"""

import math

def min_hand_usage(n, m, x, keyboard, text):
    def shift_key_test(arr, dictionary, distance, row, column):
        arr_dict = {}
        if dictionary.get('S') is not None:
            for (a, b) in dictionary.get('S'):
                upper_limit = b - distance
                lower_limit = b + distance
                if upper_limit < 0:
                    upper_limit = 0
                if lower_limit >= row:
                    lower_limit = row - 1
                (left, right) = (a - 1, a)
                (access_right, access_left) = (1, 1)
                while True:
                    if math.sqrt((right - a) ** 2 + (upper_limit - b) ** 2) <= distance and right < column and access_right:
                        if arr_dict.get(arr[upper_limit][right]) is None:
                            arr_dict[arr[upper_limit][right]] = upper_limit
                    else:
                        access_right = 0
                    if math.sqrt((left - a) ** 2 + (upper_limit - b) ** 2) <= distance and left >= 0 and access_left:
                        if arr_dict.get(arr[upper_limit][left]) is None:
                            arr_dict[arr[upper_limit][left]] = upper_limit
                    else:
                        access_left = 0
                    right += 1
                    left -= 1
                    if not access_left and (not access_right):
                        (access_left, access_right) = (1, 1)
                        (left, right) = (a - 1, a)
                        upper_limit += 1
                    if upper_limit > lower_limit:
                        break
        return arr_dict

    keyboard_dict = dict()
    for i in range(n):
        for j in range(m):
            if keyboard_dict.get(keyboard[i][j]) is not None:
                keyboard_dict[keyboard[i][j]].append((j, i))
            else:
                keyboard_dict[keyboard[i][j]] = [(j, i)]

    hand = 0
    shift_dict = shift_key_test(keyboard, keyboard_dict, x, n, m)

    for char in text:
        if keyboard_dict.get(char.lower()) is not None:
            if 'A' <= char <= 'Z':
                if shift_dict.get('S') is not None:
                    if shift_dict.get(char.lower()) is None:
                        hand += 1
                else:
                    return -1
        else:
            return -1

    return hand