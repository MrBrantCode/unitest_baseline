"""
QUESTION:
Write a function called `calculate_students` that takes two integers `band` and `choir` as input representing the number of students in the school band and the choir respectively. The function should assume a fixed ratio of boys to girls in the band is 7:6 and in the choir is 3:5. It should return a string containing the number of boys and girls in both the band and the choir, the total number of boys and girls, and whether the total number of boys is greater than the total number of girls or not. If the total number of students in either the band or the choir cannot be perfectly divided by the sum of their respective ratios, the function should return a meaningful error message.
"""

def calculate_students(band, choir):
    band_ratio = (7, 6)
    choir_ratio = (3, 5)
    
    band_total_ratio = sum(band_ratio)
    choir_total_ratio = sum(choir_ratio)
    
    if band % band_total_ratio != 0 or choir % choir_total_ratio != 0:
        return "Ratios do not evenly divide total number of students"
    
    band_boys = (band / band_total_ratio) * band_ratio[0]
    band_girls = band - band_boys
    
    choir_boys = (choir / choir_total_ratio) * choir_ratio[0]
    choir_girls = choir - choir_boys
    
    total_boys = band_boys + choir_boys
    total_girls = band_girls + choir_girls
    
    band_output = f"Band = Boys: {band_boys}, Girls: {band_girls}"
    choir_output = f"Choir = Boys: {choir_boys}, Girls: {choir_girls}"
    
    total_output = f"Total Boys = {total_boys}, Total Girls = {total_girls}"
    
    boys_greater_output = "Total number of Boys is greater than Girls" if total_boys > total_girls else "Total number of Boys is less than Girls"

    return f"{band_output}. {choir_output}. {total_output}. {boys_greater_output}"