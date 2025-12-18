"""
QUESTION:
Create a function named 'get_art_in_1' that takes two parameters: an artwork identification number and a specific currency. The function should return the price of the artwork in the requested currency. The function should use an artwork table and a currency conversion table to calculate the price, taking into account discrepancies between the currency of the artwork and the requested currency. The function should handle invalid artwork identification numbers and currency pairs.
"""

def get_art_in_1(art_id, req_currency):
    artwork_table = {"art1": {"name": "The Starry Night", "price": 1000, "currency": "USD"},
                    "art2": {"name": "The Persistence of Memory", "price": 1200, "currency": "EUR"},
                    "art3": {"name": "The Mona Lisa", "price": 1500, "currency": "GBP"}}

    currency_conversion_table = {"USD-EUR": 0.85, "USD-GBP": 0.77, "EUR-USD": 1.18,
                                "EUR-GBP": 0.91, "GBP-USD": 1.29, "GBP-EUR": 1.10}

    try:
        artwork_info = artwork_table.get(art_id)
        artwork_currency = artwork_info["currency"]
        
        if req_currency == artwork_currency:
            return artwork_info["price"]
        
        else:
            conv_factor = currency_conversion_table.get(f"{artwork_currency}-{req_currency}")
            
            if conv_factor:
                price_in_req_currency = artwork_info["price"] * conv_factor
                return price_in_req_currency
            
            else:
                return "Invalid currency pair."
                
    except KeyError:
        return "Invalid artwork identification number."