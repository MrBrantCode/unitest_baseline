"""
QUESTION:
# Task

**Your task** is to implement function `printNumber` (`print_number` in C/C++ and Python `Kata.printNumber` in Java) that returns string that represents given number in text format (see examples below).

Arguments:
 - `number` — Number that we need to print (`num` in C/C++/Java)
 - `char` — Character for building number (`ch` in C/C++/Java)

# Examples
```c,python
print_number(99, '$')
//Should return
//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n
//$                                      $\n
//$   $$$$   $$$$   $$$$   $$$$   $$$$   $\n
//$  $$  $$ $$  $$ $$  $$ $$  $$ $$  $$  $\n
//$  $$  $$ $$  $$ $$  $$ $$  $$ $$  $$  $\n
//$  $$  $$ $$  $$ $$  $$  $$$$   $$$$   $\n
//$  $$  $$ $$  $$ $$  $$   $$     $$    $\n
//$   $$$$   $$$$   $$$$   $$     $$     $\n
//$                                      $\n
//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

print_number(12345, '*')
//Should return
//****************************************\n
//*                                      *\n
//*    **    ****   ****  **  ** ******  *\n
//*   ***   **  ** **  ** **  ** **      *\n
//*  * **      **     **  **  ** *****   *\n
//*    **     **      **   *****     **  *\n
//*    **    **    **  **     **     **  *\n
//*  ****** ******  ****      ** *****   *\n
//*                                      *\n
//****************************************

print_number(67890, '@')
//Should return
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n
//@                                      @\n
//@     @@  @@@@@@  @@@@   @@@@   @@@@   @\n
//@    @@   @@  @@ @@  @@ @@  @@ @@  @@  @\n
//@   @@@@     @@   @@@@  @@  @@ @@  @@  @\n
//@  @@  @@   @@    @@@@   @@@@  @@  @@  @\n
//@  @@  @@  @@    @@  @@   @@   @@  @@  @\n
//@   @@@@   @@     @@@@   @@     @@@@   @\n
//@                                      @\n
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
>***Note, that***:
 - Number should be `0 <= number <= 99999` and have `5 digits` (should have zeros at the start if needed)
 - Test cases contains only valid values (integers that are 0 <= number <= 99999) and characters
 - Numbers should have the same shape as in the examples (6x6 by the way)
 - Returned string should be joined by `\n` character (except of the end)
 - Returned string should have 1 character *(height)* border (use the same character as for number) + padding (1 character in height vertical and 2 horizontal with ` `) around borders and 1 character margin between "digits"
 
 *Suggestions and translations are welcome.*
"""

def generate_number_string(number: int, char: str) -> str:
    # Define the patterns for each digit (0-9) for each of the 6 lines
    L = (
        (' #### ', '  ##  ', ' #### ', ' #### ', '##  ##', '######', '   ## ', '######', ' #### ', ' #### ').__getitem__,
        ('##  ##', ' ###  ', '##  ##', '##  ##', '##  ##', '##    ', '  ##  ', '##  ##', '##  ##', '##  ##').__getitem__,
        ('##  ##', '# ##  ', '   ## ', '   ## ', '##  ##', '##### ', ' #### ', '   ## ', ' #### ', '##  ##').__getitem__,
        ('##  ##', '  ##  ', '  ##  ', '   ## ', ' #####', '    ##', '##  ##', '  ##  ', ' #### ', ' #### ').__getitem__,
        ('##  ##', '  ##  ', ' ##   ', '##  ##', '    ##', '    ##', '##  ##', ' ##   ', '##  ##', '  ##  ').__getitem__,
        (' #### ', '######', '######', ' #### ', '    ##', '##### ', ' #### ', ' ##   ', ' #### ', ' ##   ').__getitem__
    )
    
    # Convert the number to a 5-digit string, padding with zeros if necessary
    number_str = f'{number:05}'
    
    # Create the top and bottom borders
    border = char * 40
    middle_line = f"{char}{' ' * 38}{char}"
    
    # Generate the lines for the number representation
    number_lines = [f"{char}  {' '.join(map(L[i], map(int, number_str)))}  {char}" for i in range(6)]
    
    # Combine all parts into the final output string
    output_string = '\n'.join([border, middle_line] + number_lines + [middle_line, border])
    
    return output_string