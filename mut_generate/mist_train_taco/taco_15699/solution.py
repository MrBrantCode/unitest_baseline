"""
QUESTION:
# Task
 Smartphones software security has become a growing concern related to mobile telephony. It is particularly important as it relates to the security of available personal information.
 
 For this reason, Ahmed decided to encrypt phone numbers of contacts in such a way that nobody can decrypt them. At first he tried encryption algorithms very complex, but the decryption process is tedious, especially when he needed to dial a speed dial.

 He eventually found the algorithm following: instead of writing the number itself, Ahmed multiplied by 10, then adds the result to the original number.
 
 For example, if the phone number is `123`, after the transformation, it becomes `1353`. Ahmed truncates the result (from the left), so it has as many digits as the original phone number. In this example Ahmed wrote `353` instead of `123` in his smart phone.

 Ahmed needs a program to recover the original phone number from number stored on his phone. The program return "impossible" if the initial number can not be calculated.
 
 Note: There is no left leading zero in either the input or the output; Input `s` is given by string format, because it may be very huge ;-)

# Example

 For `s="353"`, the result should be `"123"`
 
 ```
    1230
  +  123
  .......
  = 1353  
  
  truncates the result to 3 digit -->"353"
  
  So the initial number is "123"
 ```
 For `s="123456"`, the result should be `"738496"`
 
 ```
    7384960
  +  738496
  .........
  = 8123456
  
  truncates the result to 6 digit -->"123456"
  
  So the initial number is "738496"
 ```
 For `s="4334"`, the result should be `"impossible"`
 
 Because no such a number can be encrypted to `"4334"`.

# Input/Output


 - `[input]` string `s`

  string presentation of n with `1 <= n <= 10^100`


 - `[output]` a string

  The original phone number before encryption, or `"impossible"` if the initial number can not be calculated.
"""

def decrypt_phone_number(s: str) -> str:
    """
    Decrypts the original phone number from the encrypted string.

    The encryption process involves multiplying the original number by 10, adding the original number to the result,
    and then truncating the result to the same number of digits as the original number.

    Args:
        s (str): The encrypted phone number as a string.

    Returns:
        str: The original phone number before encryption, or "impossible" if the initial number cannot be calculated.
    """
    for a in range(1, 11):
        b = int(str(a) + s)
        if b % 11 == 0:
            return str(b // 11)
    return "impossible"