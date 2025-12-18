"""
QUESTION:
problem

There are the following games.

N characters are lined up in a vertical row. The color of these characters is red, blue, or yellow, and in the initial state, four or more characters of the same color are not lined up in a row. The player can select a character at a certain position and change it to another color. By this operation, if four or more characters of the same color are lined up in a row, those characters will disappear. When four or more characters of the same color are lined up in a row due to the disappearance of the characters, those characters also disappear, and this chain continues until there are no more places where four or more characters of the same color are lined up in a row. .. The purpose of this game is to reduce the number of characters remaining without disappearing.

For example, if the color of the sixth character from the top is changed from yellow to blue in the state at the left end of the figure below, five blue characters will disappear in a row, and finally three characters will remain without disappearing.

<image>


Given the color sequence of N characters in the initial state, create a program that finds the minimum value M of the number of characters that remain without disappearing when the color of the character is changed in only one place.



input

The input consists of multiple datasets. Each dataset is given in the following format.

The first line consists of only the number of characters N (1 ≤ N ≤ 10000). The following N lines contain one of 1, 2, and 3 integers, and the i + 1st line (1 ≤ i ≤ N) represents the color of the i-th character from the top in the initial state (1). Is red, 2 is blue, and 3 is yellow).

When N is 0, it indicates the end of input. The number of datasets does not exceed 5.

output

For each dataset, output the minimum value M of the number of characters remaining without disappearing on one line.

Examples

Input

12
3
2
1
1
2
3
2
2
2
1
1
3
12
3
2
1
1
2
3
2
1
3
2
1
3
0


Output

3
12


Input

None


Output

None
"""

def find_min_remaining_characters(N, colors):
    def erase(array, i, N):
        if array[i - 1] == array[i]:
            up = i - 1
            down = i
        elif array[i] == array[i + 1]:
            up = i
            down = i + 1
        else:
            return N - 2
        while True:
            if array[up] == -1 or array[down] == -1 or (not array[up] == array[down]):
                return up + N - down - 1
            save_up = up
            save_down = down
            c = array[up]
            while array[up] == c:
                up -= 1
            while array[down] == c:
                down += 1
            if save_up - up + down - save_down < 4:
                return save_up + N - save_down - 1

    # Add boundary markers to the colors array
    a = [-1] + colors + [-1]
    min_erased = N

    for i in range(1, N + 1):
        save = a[i]
        a[i] = save % 3 + 1
        min_erased = min(min_erased, erase(a, i, N + 2))
        a[i] = (save + 1) % 3 + 1
        min_erased = min(min_erased, erase(a, i, N + 2))
        a[i] = save

    return min_erased