"""
QUESTION:
# # Task:
  * #### Complete the pattern, using the special character ```■   □```
  * #### In this kata, we draw some histogram of the sound performance of ups and downs.

# # Rules:
  -  parameter ```waves```  The value of sound waves, an array of number, all number in array >=0.
  -  return a string, ```■``` represents the sound waves, and ```□``` represents the blank part, draw the histogram from bottom to top.

# # Example:

```
draw([1,2,3,4])

□□□■
□□■■
□■■■
■■■■

draw([1,2,3,3,2,1])

□□■■□□
□■■■■□
■■■■■■

draw([1,2,3,3,2,1,1,2,3,4,5,6,7])

□□□□□□□□□□□□■
□□□□□□□□□□□■■
□□□□□□□□□□■■■
□□□□□□□□□■■■■
□□■■□□□□■■■■■
□■■■■□□■■■■■■
■■■■■■■■■■■■■


draw([5,3,1,2,4,6,5,4,2,3,5,2,1])

□□□□□■□□□□□□□
■□□□□■■□□□■□□
■□□□■■■■□□■□□
■■□□■■■■□■■□□
■■□■■■■■■■■■□
■■■■■■■■■■■■■

draw([1,0,1,0,1,0,1,0])

■□■□■□■□
```
"""

def draw_histogram(waves):
    # Find the maximum value in the waves list to determine the height of the histogram
    max_height = max(waves)
    
    # Create a list of strings where each string represents a row in the histogram
    histogram_rows = []
    for level in range(max_height, 0, -1):
        row = ''.join('■' if wave >= level else '□' for wave in waves)
        histogram_rows.append(row)
    
    # Join the rows with newline characters to form the final histogram string
    return '\n'.join(histogram_rows)