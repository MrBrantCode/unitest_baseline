"""
QUESTION:
Given an array of penalties fine[], an array of car numbers car[], and also the date. The task is to find the total fine which will be collected on the given date. Fine is collected from odd-numbered cars on even dates and vice versa.
 
Example 1:
Input:
N = 4, date = 12
car[] = {2375, 7682, 2325, 2352}
fine[] = {250, 500, 350, 200}
Output:
600
Explantion:
The date is 12 (even), so we collect the
fine from odd numbered cars. The odd
numbered cars and the fines associated
with them are as follows:
2375 -> 250
2325 -> 350
The sum of the fines is 250+350 = 600
 
Example 2:
Input:
N = 3, date = 8
car[] = {2222, 2223, 2224}
fine[] = {200, 300, 400}
Output:
300
Your Task:  
You don't need to read input or print anything. Your task is to complete the function totalFine() which takes the array car[] and fine[] its size N and an integer date as inputs and returns the total fine.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= Car_{i} <= 10^{5}
1 <= Date <= 10^{5}
1 <= Fine_{i} <= 10^{5}
"""

def calculate_total_fine(car, fine, date):
    # Initialize lists to store fines for even and odd numbered cars
    even_car_fines = []
    odd_car_fines = []
    
    # Iterate through the car numbers and classify fines based on car number parity
    for car_number, fine_amount in zip(car, fine):
        if car_number % 2 == 0:
            even_car_fines.append(fine_amount)
        else:
            odd_car_fines.append(fine_amount)
    
    # Determine which list of fines to sum based on the date parity
    if date % 2 == 0:
        return sum(odd_car_fines)
    else:
        return sum(even_car_fines)