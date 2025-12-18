"""
QUESTION:
Create a program that reads the sales unit price and sales quantity and outputs the total sales amount and the average sales quantity.



Input

The input is given in the following format:


Sales unit price, sales quantity
Sales unit price, sales quantity
::
::


A comma-separated pair of unit price and quantity is given across multiple lines. All values ​​entered are greater than or equal to 0 and less than or equal to 1,000, and the number of unit price and quantity pairs does not exceed 100.

Output

Please output the total sales amount (integer) on the first line and the average sales quantity (integer) on the second line. If the average sales volume has a fraction (number after the decimal point), round off to the first decimal place.

Example

Input

100,20
50,10
70,35


Output

4950
22
"""

def calculate_sales_summary(sales_data):
    total_sales_amount = 0
    total_sales_quantity = 0
    
    for price, quantity in sales_data:
        total_sales_amount += price * quantity
        total_sales_quantity += quantity
    
    average_sales_quantity = int(total_sales_quantity / len(sales_data) + 0.5)
    
    return total_sales_amount, average_sales_quantity