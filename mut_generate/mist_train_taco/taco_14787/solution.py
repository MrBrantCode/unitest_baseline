"""
QUESTION:
There is a bar of chocolate with a height of H blocks and a width of W blocks.
Snuke is dividing this bar into exactly three pieces.
He can only cut the bar along borders of blocks, and the shape of each piece must be a rectangle.
Snuke is trying to divide the bar as evenly as possible.
More specifically, he is trying to minimize S_{max} - S_{min}, where S_{max} is the area (the number of blocks contained) of the largest piece, and S_{min} is the area of the smallest piece.
Find the minimum possible value of S_{max} - S_{min}.

-----Constraints-----
 - 2 ≤ H, W ≤ 10^5

-----Input-----
Input is given from Standard Input in the following format:
H W

-----Output-----
Print the minimum possible value of S_{max} - S_{min}.

-----Sample Input-----
3 5

-----Sample Output-----
0

In the division below, S_{max} - S_{min} = 5 - 5 = 0.
"""

def minimize_chocolate_division_difference(H, W):
    def score(_list):
        return max(_list) - min(_list)
    
    answer = H * W
    
    # Horizontal cuts
    for i in range(1, W // 2 + 1):
        a = score([H * i, (W - i) * (H // 2), (W - i) * (H - H // 2)])
        b = score([H * i, H * ((W - i) // 2), H * (W - i - (W - i) // 2)])
        answer = min(a, b, answer)
    
    # Vertical cuts
    for i in range(1, H // 2 + 1):
        a = score([W * i, (H - i) * (W // 2), (H - i) * (W - W // 2)])
        b = score([W * i, W * ((H - i) // 2), W * (H - i - (H - i) // 2)])
        answer = min(a, b, answer)
    
    return answer