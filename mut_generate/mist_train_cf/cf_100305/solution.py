"""
QUESTION:
Create a function named 'food_allergy_prediction' that takes two parameters: 'months_breastfed' (the number of months a baby has been breastfed) and 'maternal_diet' (the mother's diet). The function should predict the probability of the baby developing food allergies in the future based on the exclusive breastfeeding duration and the frequency of allergenic foods in the mother's diet.
"""

def food_allergy_prediction(months_breastfed, maternal_diet):
    # Check if exclusive breastfeeding duration is at least 4 to 6 months
    if months_breastfed < 4:
        return "Breastfeed exclusively for at least 4 to 6 months to lower the risk of food allergies."
    
    # Check if allergenic foods have been introduced between 4 to 6 months and 12 months
    if months_breastfed < 12:
        return "Introduce allergenic foods between 4 to 6 months and 12 months of age to prevent food allergies."
    
    # Check maternal consumption of allergenic foods during pregnancy and lactation
    if "peanuts" in maternal_diet.lower() or "tree nuts" in maternal_diet.lower():
        return "Maternal consumption of peanuts or tree nuts during pregnancy and lactation may increase the risk of food allergies. Consider avoiding these foods or limiting their intake."
    
    # Calculate the probability of developing food allergies based on exclusive breastfeeding duration and allergenic food introduction
    if months_breastfed >= 12:
        # If the baby has been breastfed exclusively for at least 6 months and allergenic foods have been introduced between 4 to 6 months and 12 months, the probability of developing food allergies is low.
        return "The probability of developing food allergies is low. Continue to introduce a variety of foods into the baby's diet."
    else:
        # If the baby has not been breastfed exclusively for at least 6 months or allergenic foods have not been introduced between 4 to 6 months and 12 months, the probability of developing food allergies may be higher.
        return "The probability of developing food allergies may be higher. Consider extending the breastfeeding period or introducing allergenic foods earlier."