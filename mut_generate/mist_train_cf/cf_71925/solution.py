"""
QUESTION:
Create a function `drop_duplicates_conditionally` that takes a DataFrame as input and returns a new DataFrame with duplicate entries removed based on the 'url' attribute, but only if the 'drop_if_dup' attribute is 'Yes'. If 'drop_if_dup' is 'No', duplicate entries should be preserved. The function should retain the first occurrence of each 'url' attribute when 'drop_if_dup' is 'Yes'.
"""

def drop_duplicates_conditionally(df):
    # Split the DataFrame into two parts: one where 'drop_if_dup' == 'Yes', and the other where 'drop_if_dup' == 'No'
    df_yes = df[df['drop_if_dup'] == 'Yes']
    df_no = df[df['drop_if_dup'] == 'No']

    # Drop duplicates in df_yes
    df_yes = df_yes.drop_duplicates(subset='url', keep='first')

    # Concatenate the two parts
    result = pd.concat([df_yes, df_no])
    result = result.sort_index()  # sort by the original index
    return result