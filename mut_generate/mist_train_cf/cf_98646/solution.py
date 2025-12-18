"""
QUESTION:
Write a function named `add_character` that adds a new character to the "Guri and Gura" book series and integrates them into the plot. The new character should have a unique personality, skills, and traits that contribute to the adventures of Guri and Gura. The function should also determine how many themes in the book series align with the new character's interests or strengths and suggest potential plot developments that could arise from their presence.

The input should be a dictionary representing the book series, containing the title, author, illustrator, themes, characters, and books. The output should be the modified dictionary with the new character added and the number of aligned themes.
"""

def add_character(book_series, new_character):
    # Add a new character to the characters list
    book_series["characters"].append(new_character["name"])
    
    # Add the new character to the plot of each book
    for book in book_series["books"]:
        if "plot" not in book:
            book["plot"] = ""
        book["plot"] += f" {new_character['name']} joins Guri and Gura and showcases her {new_character['skills']} skills."
    
    # Count the number of themes that align with the new character's interests
    aligned_themes = sum(1 for theme in book_series["themes"] if theme in new_character["interests"])
    
    return book_series, aligned_themes