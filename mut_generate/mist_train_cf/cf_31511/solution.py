"""
QUESTION:
Implement a function called `get_suggested_books` that takes three parameters: `user_ids` (a list of user IDs), `wishlist_data` (a dictionary where the keys are user IDs and the values are DataFrames representing the wishlists of the corresponding users), and `books` (a list of available book IDs). The function should return a dictionary where the keys are user IDs and the values are lists of up to 5 suggested book IDs for each user based on the wishlists of other users.
"""

import pandas as pd

def get_suggested_books(user_ids, wishlist_data, books):
    suggested_books = {}
    
    for user_id in user_ids:
        user_wishlist = wishlist_data.get(user_id)
        if user_wishlist is None or user_wishlist.empty:
            suggested_books[user_id] = []  
        else:
            suggestion_scores = {}
            for other_user_id, other_user_wishlist in wishlist_data.items():
                if other_user_id != user_id and not other_user_wishlist.empty:
                    common_books = set(user_wishlist['book_id']).intersection(set(other_user_wishlist['book_id']))
                    for book_id in common_books:
                        suggestion_scores[book_id] = suggestion_scores.get(book_id, 0) + 1  
            
            sorted_suggestions = sorted(suggestion_scores, key=suggestion_scores.get, reverse=True)
            suggested_books[user_id] = sorted_suggestions[:5]  
    
    return suggested_books