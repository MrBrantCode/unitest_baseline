"""
QUESTION:
Mr. Matsudaira is always careful about eco-friendliness in his life. Last month's water charge was 4280 yen, which exceeded the usual target of 4000 yen, so we have been trying to save water this month. How much have you saved on your water bill compared to last month?

Enter this month's water usage w [m3] and create a program that outputs how much water charges you have saved compared to last month's water charges of 4280 yen.

The water charge is calculated as follows.

(Water charge) = (Basic charge) + (Charge based on water volume)

The charge based on the amount of water is calculated according to the amount used as shown in the table below.

Stage | Water volume | Price
--- | --- | ---
1st stage charge | Up to 10 [m3] | Basic charge 1150 yen
Second stage fee | 10 [m3] Excess up to 20 [m3] | 125 yen per [m3]
Third stage charge | 20 [m3] Excess up to 30 [m3] | 140 yen per [m3]
4th stage charge | 30 [m3] excess | 160 yen per [m3]



For example, if the amount of water used is 40 [m3], the basic charge is 1150 yen (1st stage) + 10 [m3] x 125 yen (2nd stage) + 10 [m3] x 140 yen (3rd stage) + 10 [ m3] x 160 yen (4th stage) = 5400 yen.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of -1.

For each dataset, an integer w (0 ≤ w ≤ 100) representing the amount of water used this month is given on one line.

The number of datasets does not exceed 200.

Output

For each input dataset, the difference from last month's water charges is output on one line.

Example

Input

29
40
0
-1


Output

620
-1120
3130
"""

def calculate_water_charge_savings(w: int) -> int:
    # Last month's water charge
    last_month_charge = 4280
    
    # Calculate this month's water charge
    if w <= 10:
        this_month_charge = 1150
    elif w <= 20:
        this_month_charge = 1150 + 125 * (w - 10)
    elif w <= 30:
        this_month_charge = 1150 + 125 * 10 + 140 * (w - 20)
    else:
        this_month_charge = 1150 + 125 * 10 + 140 * 10 + 160 * (w - 30)
    
    # Calculate the savings
    savings = last_month_charge - this_month_charge
    
    return savings