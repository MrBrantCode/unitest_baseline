"""
QUESTION:
Implement a function `isDuplicatedOffer` that checks if an offer with a given name and category ID already exists in the active offers for that category. The function takes three parameters: `self`, `name`, and `categoryId`. The function should use the existing `filterMyOffers` method, which filters offers based on name, status, limit, and category ID. The `filterMyOffers` method returns a list of dictionaries, each representing an offer with keys 'name', 'status', 'category', etc., where 'category' is another dictionary with keys 'id', 'name', etc. The function should return `True` if a duplicated offer is found and `False` otherwise.
"""

def isDuplicatedOffer(self, name, categoryId):
    filteredOffers = self.filterMyOffers(name, 'ACTIVE', 1, categoryId)
    for offer in filteredOffers:
        if offer['name'] == name and offer['category']['id'] == categoryId:
            return True
    return False