"""
QUESTION:
Given a random bingo card and an array of called numbers, determine if you have a bingo!

*Parameters*: `card` and `numbers` arrays.

*Example input*:
```
card = [
  ['B', 'I', 'N', 'G', 'O'],
  [1, 16, 31, 46, 61],
  [3, 18, 33, 48, 63],
  [5, 20, 'FREE SPACE', 50, 65],
  [7, 22, 37, 52, 67],
  [9, 24, 39, 54, 69]
]

numbers = ['B1', 'I16', 'N31', 'G46', 'O61']
```

*Output*: ```true``` if you have a bingo, ```false``` if you do not.

You have a bingo if you have a complete row, column, or diagonal - each consisting of 5 numbers, or 4 numbers and the FREE SPACE.

### Constraints:
Each column includes 5 random numbers within a range (inclusive):  
`'B':  1 - 15`  
`'I': 16 - 30`  
`'N': 31 - 45`  
`'G': 46 - 60`  
`'O': 61 - 75`  

### Notes:
* All numbers will be within the above ranges.
* `FREE SPACE` will not be included in the numbers array but always counts towards a bingo.
* The first array of the card is the column headers.
* `numbers` array will include only tiles present in the card, without duplicates.

___

## Examples:
```
card:
------------------------------
| B  | I  |   N    | G  | O  |
==============================
| 2  | 17 |   32   | 47 | 74 |
------------------------------
| 14 | 25 |   44   | 48 | 62 |
------------------------------
| 5  | 22 | 'FREE' | 49 | 67 |
------------------------------
| 10 | 23 |   45   | 59 | 73 |
------------------------------
| 1  | 30 |   33   | 58 | 70 |
------------------------------

numbers: ['N32', 'N45', 'B7', 'O75', 'N33', 'N41, 'I18', 'N44']

// return true - you have bingo at ['N32', 'N44', 'FREE', 'N45', 'N33']
```

The inspiration for this kata originates from completing the [Bingo Card](http://www.codewars.com/kata/566d5e2e57d8fae53c00000c) by FrankK.
"""

def check_bingo(card, numbers):
    # Initialize row, column, and diagonal counters
    row_counts = [0] * 5
    col_counts = [0] * 5
    diag_counts = [1] * 2  # Diagonals start with 1 because of the FREE SPACE
    
    # The FREE SPACE is always considered marked
    row_counts[2] = 1
    col_counts[2] = 1
    
    # Convert numbers list to a set for O(1) lookups
    called_numbers = set(numbers)
    
    # Iterate over the card to check for marked numbers
    for x, line in enumerate(card[1:]):
        for y, (col_header, number) in enumerate(zip(card[0], line)):
            tile = f'{col_header}{number}'
            if tile in called_numbers:
                row_counts[x] += 1
                col_counts[y] += 1
                if x == y:
                    diag_counts[0] += 1
                if x + y == 4:
                    diag_counts[1] += 1
    
    # Check if any row, column, or diagonal has 5 marked numbers
    return 5 in row_counts + col_counts + diag_counts