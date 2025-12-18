"""
QUESTION:
Write a function `is_prime_check` that takes a 2D array of mixed data types as input. The function should iterate over each element in the array. If the element is an integer or a string that can be converted to an integer, it should check if the number is prime. If the number is prime, print the number along with the message " is a prime number." If the number is not prime, print the number along with the message " is not a prime number." If the number is zero or negative, print the number along with the message " is a negative number." If the element cannot be converted to an integer, print the element along with the message " is not a number."
"""

def is_prime_check(array):
  def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
      return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

  for sublist in array:
    for item in sublist:
      try:
        num = int(item)
        if num >= 0:
          if is_prime(num):
            print(str(num) + " is a prime number.")
          else:
            print(str(num) + " is not a prime number.")
        else:
          print(str(num) + " is a negative number.")
      except ValueError:
        print(item + " is not a number.")