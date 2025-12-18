"""
QUESTION:
Create a function called `add_character` that adds a new character to the "Guri and Gura" book series. The function should take in a dictionary representing the book series and a dictionary representing the new character, and modify the book series dictionary to include the new character. The new character's skills or expertise should align with at least one of the book series' themes, and their presence should impact the dynamic between the existing characters.

The book series dictionary should have the following structure: 
- "title": title of the book series
- "author": author of the book series
- "illustrator": illustrator of the book series
- "themes": list of themes in the book series
- "characters": list of characters in the book series
- "books": list of dictionaries, each representing a book in the series with "title" and "year" keys

The new character dictionary should have the following structure: 
- "name": name of the new character
- "skills": list of skills or expertise of the new character
- "personality": personality traits of the new character
"""

def add_character(book_series, new_character):
    """
    Adds a new character to the book series and modifies the plot to include the new character.
    
    Args:
    book_series (dict): A dictionary representing the book series.
    new_character (dict): A dictionary representing the new character.
    
    Returns:
    dict: The modified book series with the new character.
    """
    
    # Check if the new character's skills align with at least one of the book series' themes
    if any(skill in book_series["themes"] for skill in new_character["skills"]):
        # Add the new character to the characters list
        book_series["characters"].append(new_character["name"])
        
        # Add the new character to the plot of each book
        for book in book_series["books"]:
            if "plot" not in book:
                book["plot"] = ""
            book["plot"] += f" {new_character['name']} joins Guri and Gura and teaches them new recipes and cooking techniques."
        
        # Print the number of themes that align with the new character's interests or strengths
        aligned_themes = sum(1 for skill in new_character["skills"] if skill in book_series["themes"])
        print(f"The number of themes in the book series that align with {new_character['name']}'s interests or strengths is {aligned_themes}.")
        
        # Print potential plot developments that could arise from the new character's presence
        print("Potential plot developments that could arise from", new_character["name"], "presence are:")
        print(f"- {new_character['name']} teaches Guri and Gura new recipes and cooking techniques.")
        print(f"- {new_character['name']} introduces Guri and Gura to new ingredients.")
        print(f"- {new_character['name']} challenges Guri and Gura to cook against her in a cooking competition.")
        print(f"- {new_character['name']} helps Guri and Gura cater a party for their friends.")
        
        return book_series
    else:
        print("The new character's skills do not align with any of the book series' themes.")
        return book_series