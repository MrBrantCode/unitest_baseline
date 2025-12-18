"""
QUESTION:
Design a data structure to store the academic information of students in an educational institution. The structure should be able to store information such as student ID, name, age, gender, class, grades, and subjects, and allow for efficient lookup, addition, and deletion of student records.
"""

def entance(studentID, name, age, gender, class_, grades, subjects):
    studentdict = {}
    studentdict['Name'] = name
    studentdict['Age'] = age
    studentdict['Gender'] = gender
    studentdict['Class'] = class_
    studentdict['Grades'] = grades   #This will be a list
    studentdict['Subjects'] = subjects   #This will be a list
    return studentdict

maindict = {}

def add_student(studentID, name, age, gender, class_, grades, subjects):
    maindict[studentID] = entance(studentID, name, age, gender, class_, grades, subjects)