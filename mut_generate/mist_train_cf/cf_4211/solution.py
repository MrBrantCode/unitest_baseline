"""
QUESTION:
Write a function `calculate_average_grade` that takes a list of dictionaries representing students, where each dictionary contains the student's name and a list of grades. The function should return a list of dictionaries containing the student's name, their average grade rounded to the nearest integer, and a comment based on their grade. The comment should be "Excellent" for grades 90 and above, "Good" for grades 80-89, "Average" for grades 70-79, "Below Average" for grades 60-69, and "Poor" for grades below 60. The function should have a time complexity of O(n), where n is the total number of grades across all students, and a space complexity of O(1).
"""

def calculate_average_grade(students):
    results = []
    for student in students:
        grades = student['grades']
        average = round(sum(grades) / len(grades))
        comment = ""
        if average >= 90:
            comment = "Excellent"
        elif average >= 80:
            comment = "Good"
        elif average >= 70:
            comment = "Average"
        elif average >= 60:
            comment = "Below Average"
        else:
            comment = "Poor"
        results.append({
            'name': student['name'],
            'average_grade': average,
            'comment': comment
        })
    return results