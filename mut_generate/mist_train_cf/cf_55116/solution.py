"""
QUESTION:
Create a function `find_person_by_genre` that takes a `genre` as input and returns the name of the person who prefers that genre. The function should use the following dictionary of names to preferences:
```python
preferences = {
    "Alice": "mystery",
    "Ben": "romance",
    "Caleb": "fantasy",
    "Diana": "historical",
    "Ella": "thrillers",
    "Frank": "sci-fi"
}
```
"""

def find_person_by_genre(genre):
    preferences = {
        "Alice": "mystery",
        "Ben": "romance",
        "Caleb": "fantasy",
        "Diana": "historical",
        "Ella": "thrillers",
        "Frank": "sci-fi"
    }
    for person, preference in preferences.items():
        if preference == genre:
            return person