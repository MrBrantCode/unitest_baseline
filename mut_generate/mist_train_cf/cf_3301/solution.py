"""
QUESTION:
Write a function to print a dictionary of companies in alphabetical order by company name. For each company, print the company name, the length of the company name, the programming languages used in reverse order (both alphabetically and in the list), and the founding year. The function should have a time complexity of O(n^2) and a space complexity of O(1). You are not allowed to use built-in sorting functions or libraries. 

The input dictionary has the following structure: 
{
  company_name: {
    "name": company_name,
    "languages": [language1, language2, ...],
    "year": founding_year
  },
  ...
} 

The output for each company should be in the format:
Company: company_name
Name Length: name_length
Languages: language1, language2, ...
Year: founding_year
"""

def print_companies(data):
    """
    Prints a dictionary of companies in alphabetical order by company name.
    For each company, prints the company name, the length of the company name, 
    the programming languages used in reverse order (both alphabetically and in the list), 
    and the founding year.

    Args:
        data (dict): A dictionary of companies with their details.
    """

    def reverse_string(s):
        return s[::-1]

    def sort_languages(languages):
        for i in range(len(languages)-1):
            for j in range(i+1, len(languages)):
                if languages[i] < languages[j]:
                    languages[i], languages[j] = languages[j], languages[i]
        return languages

    for company in sorted(data.keys()):
        company_data = data[company]
        name = company_data["name"]
        languages = company_data["languages"]
        year = company_data["year"]

        name_length = len(name)
        reversed_languages = reverse_string(", ".join(sort_languages(languages)))
        print(f"Company: {company}")
        print(f"Name Length: {name_length}")
        print(f"Languages: {reversed_languages}")
        print(f"Year: {year}")
        print()