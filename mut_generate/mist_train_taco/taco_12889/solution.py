"""
QUESTION:
# Definition

**_Disarium number_** is the number that *The sum of its digits powered with their respective positions is equal to the number itself*.

____

# Task

**_Given_** a number, **_Find if it is Disarium or not_** . 
____

# Warm-up (Highly recommended)

# [Playing With Numbers Series](https://www.codewars.com/collections/playing-with-numbers)
___

# Notes 

* **_Number_** *passed is always*  **_Positive_** .
* **_Return_** *the result as* **_String_**
___

# Input >> Output Examples

```
disariumNumber(89) ==> return "Disarium !!"
```
## **_Explanation_**:

* Since , **_8^(1) + 9^(2) = 89_** , thus *output* is `"Disarium !!"`
___

```
disariumNumber(564) ==> return "Not !!"
```
## **_Explanation_**:

Since , **_5^(1) + 6^(2) + 4^(3) = 105 != 564_** ,  thus *output* is `"Not !!"`

___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou
"""

def is_disarium(number):
    # Convert the number to a string to easily access each digit
    str_num = str(number)
    
    # Calculate the sum of each digit raised to the power of its position (1-based index)
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(str_num))
    
    # Check if the calculated sum is equal to the original number
    if disarium_sum == number:
        return "Disarium !!"
    else:
        return "Not !!"