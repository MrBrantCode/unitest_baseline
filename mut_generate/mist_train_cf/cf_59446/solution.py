"""
QUESTION:
Create a function called `classify_countries` that takes a list of tuples containing the names of countries and their capitals as input. The function should return a list of tuples where each tuple contains the country-capital pair, their continent (Asia, Europe, America, Africa, or Oceania), and the official language(s) spoken in the country.
"""

def classify_countries(country_capitals):
    """
    This function takes a list of tuples containing country names and their capitals, 
    and returns a list of tuples containing country-capital pairs, their continent, 
    and the official language(s) spoken in the country.
    
    Parameters:
    country_capitals (list): A list of tuples containing country names and their capitals.
    
    Returns:
    list: A list of tuples containing country-capital pairs, their continent, and the official language(s) spoken in the country.
    """
    
    # Dictionary to store country information
    country_info = {
        "China": ("Asia", "Mandarin"),
        "Finland": ("Europe", "Finnish and Swedish"),
        "United States": ("America", "English"),
        "Vietnam": ("Asia", "Vietnamese"),
        "India": ("Asia", "Hindi and English"),
        "Italy": ("Europe", "Italian"),
        "Mexico": ("America", "Spanish"),
        "Russia": ("Europe/Asia", "Russian"),
        "France": ("Europe", "French"),
        "Brazil": ("America", "Portuguese"),
        "Australia": ("Oceania", "English"),
        "Egypt": ("Africa", "Arabic"),
        "South Africa": ("Africa", "English, Afrikaans, Zulu, Xhosa, Swazi, Ndebele, Northern Sotho, Southern Sotho, Tswana, Tsonga, Venda"),
        "Japan": ("Asia", "Japanese"),
        "Canada": ("America", "English and French"),
        "Argentina": ("America", "Spanish"),
        "Nigeria": ("Africa", "English"),
        "New Zealand": ("Oceania", "English and Maori"),
        "Germany": ("Europe", "German"),
        "Saudi Arabia": ("Asia", "Arabic")
    }
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each country-capital pair
    for country, capital in country_capitals:
        # Get the continent and official language(s) for the country
        continent, language = country_info[country]
        
        # Append the country-capital pair, continent, and official language(s) to the results list
        results.append((country, capital, continent, language))
    
    # Return the results list
    return results