"""
QUESTION:
Task:
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:

['XOOXO',
  'XOOXO',
  'OOOXO',
  'XXOXO',
  'OXOOO'] 

or 


should return:
"Total land perimeter: 24",

while


['XOOO',
  'XOXO',
  'XOXO',
  'OOXX',
  'OOOO']



should return: "Total land perimeter: 18"
Good luck!
"""

def calculate_land_perimeter(arr):
    I, J = len(arr), len(arr[0])
    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0 or arr[i - 1][j] == 'O':
                    P += 1
                if i == I - 1 or arr[i + 1][j] == 'O':
                    P += 1
                if j == 0 or arr[i][j - 1] == 'O':
                    P += 1
                if j == J - 1 or arr[i][j + 1] == 'O':
                    P += 1
    return f'Total land perimeter: {P}'