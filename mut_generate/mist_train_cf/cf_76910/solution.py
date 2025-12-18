"""
QUESTION:
Create a Python function named `clean_data` that takes a Pandas DataFrame as input. The function should remove rows where the 'Age' column is null or the 'Salary' is below 0. It should replace null values in the 'Profession' column with the string 'Unspecified'. Finally, it should sort the cleaned DataFrame in decreasing order of 'Salary'. The function should handle any exceptions that may occur during the cleaning process and return the cleaned DataFrame.
"""

# Function to Clean Data
def clean_data(df):
    try:
        # Remove rows with null 'Age'
        df = df[df['Age'].notna()]
        
        # Remove rows where 'Salary' is below 0 
        df = df[df['Salary'] >= 0] 
        
        # Replace null values in the 'Profession' column with 'Unspecified'
        df['Profession'] = df['Profession'].fillna('Unspecified')
        
        # Sort the dataframe in descending order of 'Salary'
        df = df.sort_values(by='Salary', ascending=False)
    
    except Exception as e:
        print(str(e))
        return None
    
    return df