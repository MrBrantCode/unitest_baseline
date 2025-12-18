"""
QUESTION:
- Input: Integer `n`
- Output: String

Example:

`a(4)` prints as
```
   A   
  A A  
 A A A 
A     A
```

`a(8)` prints as
```
       A       
      A A      
     A   A     
    A     A    
   A A A A A   
  A         A  
 A           A 
A             A
```

`a(12)` prints as
```
           A           
          A A          
         A   A         
        A     A        
       A       A       
      A         A      
     A A A A A A A     
    A             A    
   A               A   
  A                 A  
 A                   A 
A                     A
```
Note:

- Each line's length is `2n - 1`
- Each line should be concatenate by line break `"\n"`
- If `n` is less than `4`, it should return `""`
- If `n` is odd, `a(n) = a(n - 1)`, eg `a(5) == a(4); a(9) == a(8)`
"""

def generate_pattern(n: int) -> str:
    # Adjust n if it is odd
    if n % 2 != 0:
        n = n - 1
    
    # Return empty string if n is less than 4
    if n < 4:
        return ''
    
    # Initialize the side spaces
    side = ' ' * (n - 1)
    
    # List to hold each line of the pattern
    lines = [side + 'A' + side]
    
    # Generate each line of the pattern
    for i in range(1, n):
        side = side[1:]  # Reduce side spaces by one
        middle = 'A ' * (i - 1) if i == n // 2 else '  ' * (i - 1)
        lines.append(side + 'A ' + middle + 'A' + side)
    
    # Join all lines with newline character
    return '\n'.join(lines)