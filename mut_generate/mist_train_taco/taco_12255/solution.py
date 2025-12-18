"""
QUESTION:
In this kata you will be given a random string of letters and tasked with returning them as a string of comma-separated sequences sorted alphabetically, with each sequence starting with an uppercase character followed by `n-1` lowercase characters, where `n` is the letter's alphabet position `1-26`.

## Example

```python
alpha_seq("ZpglnRxqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"
```

## Technical Details

- The string will include only letters.
- The first letter of each sequence is uppercase followed by `n-1` lowercase.
- Each sequence is separated with a comma.
- Return value needs to be a string.
"""

def generate_alpha_sequences(input_string: str) -> str:
    """
    Generates a string of comma-separated sequences sorted alphabetically, 
    where each sequence starts with an uppercase character followed by 
    `n-1` lowercase characters, and `n` is the letter's alphabet position (1-26).

    Parameters:
    - input_string (str): The input string containing random letters.

    Returns:
    - str: A string of comma-separated sequences.
    """
    return ','.join(((c * (ord(c) - 96)).capitalize() for c in sorted(input_string.lower())))