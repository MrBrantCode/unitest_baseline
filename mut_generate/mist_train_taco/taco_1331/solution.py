"""
QUESTION:
You have an image file of size $2 \times 2$, consisting of $4$ pixels. Each pixel can have one of $26$ different colors, denoted by lowercase Latin letters.

You want to recolor some of the pixels of the image so that all $4$ pixels have the same color. In one move, you can choose no more than two pixels of the same color and paint them into some other color (if you choose two pixels, both should be painted into the same color).

What is the minimum number of moves you have to make in order to fulfill your goal?


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases.

Each test case consists of two lines. Each of these lines contains two lowercase letters of Latin alphabet without any separators, denoting a row of pixels in the image.


-----Output-----

For each test case, print one integer — the minimum number of moves you have to make so that all $4$ pixels of the image have the same color.


-----Examples-----

Input
5
rb
br
cc
wb
aa
aa
ab
cd
yy
xx
Output
1
2
0
3
1


-----Note-----

Let's analyze the test cases of the example.

In the first test case, you can paint the bottom left pixel and the top right pixel (which share the same color) into the color r, so all pixels have this color.

In the second test case, two moves are enough:

paint both top pixels, which have the same color c, into the color b;

paint the bottom left pixel into the color b.

In the third test case, all pixels already have the same color.

In the fourth test case, you may leave any of the pixels unchanged, and paint all three other pixels into the color of that pixel in three moves.

In the fifth test case, you can paint both top pixels into the color x.
"""

def min_moves_to_uniform_color(image):
    """
    Calculate the minimum number of moves required to make all pixels in a 2x2 image the same color.

    Parameters:
    image (list of str): A list containing two strings, each representing a row of pixels in the 2x2 image.

    Returns:
    int: The minimum number of moves required.
    """
    # Flatten the image into a single string
    s = image[0] + image[1]
    
    # Count the occurrences of each color
    color_counts = [s.count(s[i]) for i in range(4)]
    
    # Find the maximum count of any single color
    max_count = max(color_counts)
    
    # Determine the minimum number of moves based on the maximum count
    if max_count == 4:
        return 0
    elif max_count == 3:
        return 1
    elif max_count == 2:
        if min(color_counts) == 1:
            return 2
        else:
            return 1
    elif max_count == 1:
        return 3