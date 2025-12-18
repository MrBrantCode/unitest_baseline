"""
QUESTION:
Create a function called `classify_age` that takes an integer `age` as input and returns a string representing the age classification group. The age classification groups are as follows: toddler (0-2 years), child (3-12 years), teenager (13-19 years), adult (20-59 years), and senior citizen (60 years and above). The function should return "Invalid age" if the input age is negative.
"""

def classify_age(age):
  if age < 0:
    return "Invalid age"
  elif age <= 2:
    return "Toddler"
  elif age <= 12:
    return "Child"
  elif age <= 19:
    return "Teenager"
  elif age <= 59:
    return "Adult"
  else:
    return "Senior Citizen"