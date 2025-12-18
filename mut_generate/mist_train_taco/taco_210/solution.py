"""
QUESTION:
You need to handle two extraordinarily large integers. The good news is that you don't need to perform any arithmetic operation on them. You just need to compare them and see whether they are equal or one is greater than the other.

Given two strings x and y, print either "x< y"(ignore space, editor issues), "x>y" or "x=y" depending on the values represented by x and y. x and y each consist of a decimal integer followed zero or more '!' characters. Each '!' represents the factorial operation. For example, "3!!" represents 3!! = 6! = 720.

Input - First line of input contains no. of testcases and each test consist of 2 lines x and y.

Ouptut - Print the required output.

SAMPLE INPUT
3
0!
1
9!!
999999999
456!!!
123!!!!!!

SAMPLE OUTPUT
x=y
x>y
x<y
"""

def compare_large_integers(x: str, y: str) -> str:
    xcount, ycount = 0, 0
    
    # Count '!' in x
    i = len(x) - 1
    while i >= 0 and x[i] == '!':
        xcount += 1
        i -= 1
    
    # Count '!' in y
    i = len(y) - 1
    while i >= 0 and y[i] == '!':
        ycount += 1
        i -= 1
    
    # Extract the numeric part of x and y
    new_x = int(x[:len(x) - xcount]) if xcount < len(x) else 0
    new_y = int(y[:len(y) - ycount]) if ycount < len(y) else 0
    
    # Handle special case where 0! = 1
    if new_x == 0 and xcount > 0:
        new_x = 1
    if new_y == 0 and ycount > 0:
        new_y = 1
    
    # Normalize the counts and values if necessary
    sflag = False
    if xcount > ycount:
        new_x, new_y = new_y, new_x
        xcount, ycount = ycount, xcount
        sflag = True
    
    ycount -= xcount
    dflag = False
    
    # Compute factorials for y if necessary
    while ycount > 0:
        ycount -= 1
        val = new_y - 1
        while val > 0:
            new_y *= val
            val -= 1
            if new_y > new_x:
                dflag = True
                break
        if dflag:
            break
    
    # Swap back if necessary
    if sflag:
        new_x, new_y = new_y, new_x
    
    # Compare the final values
    if new_x > new_y:
        return "x>y"
    elif new_x == new_y:
        return "x=y"
    else:
        return "x<y"