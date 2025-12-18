"""
QUESTION:
You are given two images img1 and img2 both of size n x n, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?
 
Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We slide img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3. (Shown in red)


Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0

 
Constraints:

n == img1.length
n == img1[i].length
n == img2.length 
n == img2[i].length
1 <= n <= 30
img1[i][j] is 0 or 1.
img2[i][j] is 0 or 1.
"""

def largest_overlap(img1, img2):
    leng = len(img1[0])
    a = 0
    b = 0
    
    # Convert matrices to binary numbers
    for i in range(0, leng * leng):
        row = int(i % leng)
        col = int(i / leng)
        a = (a << 1) + img1[col][row]
        b = (b << 1) + img2[col][row]
    
    maxsum = 0
    
    # Calculate the maximum overlap
    for i in range(-leng + 1, leng):
        if i < 0:
            mask = ('0' * abs(i) + '1' * (leng - abs(i))) * leng
            bp = (b & int(mask, 2)) << abs(i)
        elif i > 0:
            mask = ('1' * (leng - abs(i)) + '0' * abs(i)) * leng
            bp = (b & int(mask, 2)) >> abs(i)
        else:
            bp = b
        
        for j in range(-leng + 1, leng):
            if j < 0:
                bpp = bp >> leng * abs(j)
            elif j > 0:
                bpp = bp << leng * abs(j) & 2 ** (leng * leng) - 1
            else:
                bpp = bp
            
            maxsum = max(maxsum, bin(a & bpp).count('1'))
    
    return maxsum