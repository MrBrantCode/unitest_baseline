"""
QUESTION:
Write a GraphQL query for the `instructors` function to retrieve the name, age, address, email, and total number of students taught by each instructor. The instructors must have at least 5 years of teaching experience and be certified in at least 3 different programming languages. The results should be sorted by the total number of students taught in descending order.
"""

def instructors(teaching_experience: int, certified_languages: int):
    query = """
        query($teachingExperience: String!, $certifiedLanguages: String!) {
            instructors(teachingExperience: $teachingExperience, certifiedLanguages: $certifiedLanguages) {
                name
                age
                address
                email
                studentsCount
            }
        }
    """
    return query