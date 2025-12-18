"""
QUESTION:
#Sort the columns of a csv-file

You get a string with the content of a csv-file. The columns are separated by semicolons.
The first line contains the names of the columns.
Write a method that sorts the columns by the names of the columns alphabetically and incasesensitive. 

An example:
```
Before sorting:
As table (only visualization):
|myjinxin2015|raulbc777|smile67|Dentzil|SteffenVogel_79|
|17945       |10091    |10088  |3907   |10132          |
|2           |12       |13     |48     |11             |

The csv-file:
myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n
17945;10091;10088;3907;10132\n
2;12;13;48;11

----------------------------------

After sorting:
As table (only visualization):
|Dentzil|myjinxin2015|raulbc777|smile67|SteffenVogel_79|
|3907   |17945       |10091    |10088  |10132          |
|48     |2           |12       |13     |11             |

The csv-file:
Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n
3907;17945;10091;10088;10132\n
48;2;12;13;11
```

There is no need for prechecks. You will always get a correct string with more than 1 line und more than 1 row. All columns will have different names.

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
"""

def sort_csv_columns(csv_file_content, sep=';', end='\n'):
    # Split the CSV content into rows
    rows = csv_file_content.split(end)
    
    # Split each row into columns and zip them together
    csv_columns = zip(*(row.split(sep) for row in rows))
    
    # Sort the columns by the first element (column name) in a case-insensitive manner
    sorted_columns = sorted(csv_columns, key=lambda col: col[0].lower())
    
    # Unzip the sorted columns back into rows
    sorted_rows = zip(*sorted_columns)
    
    # Join the rows back into a single string with the specified separator and line ending
    sorted_csv_content = end.join((sep.join(row) for row in sorted_rows))
    
    return sorted_csv_content