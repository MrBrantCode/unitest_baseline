"""
QUESTION:
Implement the function `filter_businesses` that takes in the following parameters:
- `businesses_data`: A list of dictionaries, where each dictionary represents information about a specific business.
- `sector`: A string representing the sector of activity to filter by.
- `legal_status`: A string representing the legal status to filter by.
- `open_since`: An integer representing the number of years a business has been open since its establishment.
- `has_partial_activity`: A boolean indicating whether the business has requested partial activity in the last 12 months.

The function should return a list of dictionaries, where each dictionary represents information about a business that meets all the specified criteria. The function should assume the current year is 2022 for calculating the number of years a business has been open since its establishment.
"""

def filter_businesses(businesses_data, sector, legal_status, open_since, has_partial_activity):
    current_year = 2022  # Assuming the current year is 2022
    return [
        business for business in businesses_data 
        if (business['secteur_activite'] == sector 
            and business['statut_juridique'] == legal_status 
            and current_year - business['date_ouverture_etablissement'] >= open_since 
            and business['activite_partielle'] == has_partial_activity)
    ]