"""
QUESTION:
Create a function called `employee_performance` that takes four parameters: `age`, `income`, `car_ownership`, and `years_of_experience`, where `car_ownership` is either "Yes" or "No" and `years_of_experience` is a range of 0-2 or 3-5. The function should return a string representing the employee's performance level ("Poor", "Average", "Good", "Excellent") based on the given decision tree rules. The decision tree rules are as follows:

- If age is less than 26, check income range:
  - If income is less than or equal to 25k, check car ownership:
    - If car ownership is no, check years of experience:
      - If years of experience is 0-2, performance is poor.
      - If years of experience is 3-5, performance is average.
    - If car ownership is yes, check years of experience:
      - If years of experience is 3-5, performance is good.
  - If income is greater than 25k, check car ownership:
    - If car ownership is no, check years of experience:
      - If years of experience is 0-2, performance is average.
      - If years of experience is 3-5, performance is good.
    - If car ownership is yes, check years of experience:
      - If years of experience is 3-5, performance is excellent.
- If age is greater than or equal to 26, check income range:
  - If income is less than or equal to 25k, check car ownership:
    - If car ownership is no, check years of experience:
      - If years of experience is 0-2, performance is poor.
      - If years of experience is 3-5, performance is good.
    - If car ownership is yes, check years of experience:
      - If years of experience is 3-5, performance is excellent.
  - If income is greater than 25k, check car ownership:
    - If car ownership is no, check years of experience:
      - If years of experience is 0-2, performance is average.
      - If years of experience is 3-5, performance is excellent.
    - If car ownership is yes, check years of experience:
      - If years of experience is 3-5, performance is excellent.

The function should not take any other parameters and should not use any external libraries or files.
"""

def employee_performance(age, income, car_ownership, years_of_experience):
    if age < 26:
        if income <= 25000:
            if car_ownership == "No":
                if years_of_experience <= 2:
                    return "Poor"
                else:
                    return "Average"
            else:
                if years_of_experience >= 3:
                    return "Good"
        else:
            if car_ownership == "No":
                if years_of_experience <= 2:
                    return "Average"
                else:
                    return "Good"
            else:
                if years_of_experience >= 3:
                    return "Excellent"
    else:
        if income <= 25000:
            if car_ownership == "No":
                if years_of_experience <= 2:
                    return "Poor"
                else:
                    return "Good"
            else:
                if years_of_experience >= 3:
                    return "Excellent"
        else:
            if car_ownership == "No":
                if years_of_experience <= 2:
                    return "Average"
                else:
                    return "Excellent"
            else:
                if years_of_experience >= 3:
                    return "Excellent"