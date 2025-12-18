"""
QUESTION:
Create a function named 'loop_control_statements' that demonstrates the use of 'break', 'continue', and 'return' statements within loop constructs. Implement these control flow statements in Python, considering their applicability in various programming scenarios such as data validation, algorithm optimization, and error handling. Also, analyze the impact of these statements on time and space complexity, and discuss potential pitfalls and commonalities between how different programming languages handle these control flow modifications.
"""

def loop_control_statements(num_list):
  even_nums = []
  for num in num_list:
    if num % 2 == 0:
      even_nums.append(num)
    if len(even_nums) == 5:
      return even_nums  # returns when it finds 5 even numbers
    if num == 300:  # demonstrate break statement
      break
  return even_nums  # returns if there are less than 5 even numbers

def loop_control_statements_alt(num_list):
  even_nums = []
  for num in num_list:
    if num % 2 != 0:  # demonstrate continue statement
      continue
    even_nums.append(num)
    if len(even_nums) == 5:
      return even_nums  # returns when it finds 5 even numbers
    if num == 300:  # demonstrate break statement
      break
  return even_nums  # returns if there are less than 5 even numbers