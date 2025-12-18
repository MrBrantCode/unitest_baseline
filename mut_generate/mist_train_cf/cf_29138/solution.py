"""
QUESTION:
Implement the `calculate_accrued_interest` method within the FloatingRateBond class, which takes four parameters: `nominal_interest_rate`, `face_value`, `accrual_period`, and `base_value`. The method should calculate the accrued interest using the formula: `(nominal_interest_rate * face_value * accrual_period) / base_value` and return the result.
"""

def calculate_accrued_interest(nominal_interest_rate, face_value, accrual_period, base_value):
    accrued_interest = (nominal_interest_rate * face_value * accrual_period) / base_value
    return accrued_interest