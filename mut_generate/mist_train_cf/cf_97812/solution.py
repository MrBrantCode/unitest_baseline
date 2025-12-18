"""
QUESTION:
Write a function `check_and_print` that calculates the average age of individuals with a 'Software Engineer' job title in a given list of dictionaries, and prints the average age if it exceeds 35.
"""

def check_and_print(lst):
    filtered_list = list(filter(lambda x: x['job_title'] == 'Software Engineer', lst))
    if not filtered_list:
        return
    avg_age = sum([x['age'] for x in filtered_list]) / len(filtered_list)
    if avg_age > 35:
        print('Average age of software engineers is greater than 35 years: %.2f' % avg_age)