"""
QUESTION:
Write a function `tip_difference` that takes the pre-tax dinner bill as input and returns the difference in cents between the tip amount calculated by doubling the state's sales tax of 8.25% and the traditional standard tip of 15%.
"""

def tip_difference(pre_tax_bill):
    #Calculate sales tax of 8.25% on the bill
    sales_tax = pre_tax_bill * 0.0825

    #Restaurant tip by doubling the sales tax
    californian_tip = sales_tax * 2

    #Traditional tip of 15% on pre-tax bill
    traditional_tip = pre_tax_bill * 0.15

    #Difference in the two methods, converted to cents
    difference_in_cents = (californian_tip - traditional_tip) * 100

    return difference_in_cents