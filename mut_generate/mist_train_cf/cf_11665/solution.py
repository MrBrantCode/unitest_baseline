"""
QUESTION:
Write a function `get_average_salary` to calculate the average salary for all employees who have been with the company for at least 5 years and have a job title of "Senior Software Engineer" using MongoDB aggregation.
"""

def get_average_salary(employees):
   return employees.aggregate([
      {
         "$match": {
            "yearsWithCompany": { "$gte": 5 },
            "jobTitle": "Senior Software Engineer"
         }
      },
      {
         "$group": {
            "_id": None,
            "averageSalary": { "$avg": "$salary" }
         }
      }
   ])