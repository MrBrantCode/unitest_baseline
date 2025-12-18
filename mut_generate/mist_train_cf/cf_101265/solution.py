"""
QUESTION:
Write a function named `remove_low_grades` that takes a list of dictionaries as input, where each dictionary represents a student's grades with their name, class section, and scores in three exams. The function should return a tuple containing the updated list of students whose exam grades are not lower than the class average on that exam, and a dictionary with the updated average scores of each class section in each exam.
"""

def remove_low_grades(grades):
    exams = ["exam1", "exam2", "exam3"]
    sections = set([student["section"] for student in grades])
    averages = {}
    for section in sections:
        section_grades = [student for student in grades if student["section"] == section]
        exam_averages = []
        for exam in exams:
            scores = [student[exam] for student in section_grades]
            avg = sum(scores) / len(scores)
            exam_averages.append(avg)
        averages[section] = exam_averages

    new_grades = []
    for student in grades:
        section = student["section"]
        above_avg = all([student[exam] >= averages[section][i] for i, exam in enumerate(exams)])
        if above_avg:
            new_grades.append(student)

    new_averages = {}
    new_sections = set([student["section"] for student in new_grades])
    for section in new_sections:
        new_section_grades = [student for student in new_grades if student["section"] == section]
        new_exam_averages = []
        for exam in exams:
            new_scores = [student[exam] for student in new_section_grades]
            new_avg = sum(new_scores) / len(new_scores)
            new_exam_averages.append(new_avg)
        new_averages[section] = new_exam_averages

    return new_grades, new_averages