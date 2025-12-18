"""
QUESTION:
Calculate the average age of users from the 'users' table where the age is 18 or older and the first name starts with 'A'. The results should be ordered in descending order by age. The function should be named 'average_age_of_adults_starting_with_a'.
"""

def average_age_of_adults_starting_with_a(users):
    adults_starting_with_a = [user for user in users if user['age'] >= 18 and user['first_name'].startswith('A')]
    adults_starting_with_a.sort(key=lambda x: x['age'], reverse=True)
    return sum(user['age'] for user in adults_starting_with_a) / len(adults_starting_with_a)