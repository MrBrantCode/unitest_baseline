"""
QUESTION:
Display Table of Food Orders in a Restaurant with Time of Order
The function `displayTable` should take a list of orders as input where each order is a list containing the customer name, table number, food item, and time of order. It should return a table where each row represents a table's order, with the table number in the first column and the remaining columns representing the count and average time of each food item in alphabetical order. The table should be sorted in numerically increasing order by table number.

Constraints: 
- The length of the orders list is between 1 and 5 * 10^4.
- Each order is a list of four elements.
- The customer name and food item consist of lowercase and uppercase English letters and spaces, and their length is between 1 and 20.
- The table number is an integer between 1 and 500.
- The time of order is an integer between 1 and 60.
"""

def displayTable(orders):
    tables = set()
    foods = set()
    
    time_dict = dict()
    count_dict = dict()
    
    for order in orders:
        name, table, food, time = order
        table = int(table)
        time = int(time)
        
        tables.add(table)
        foods.add(food)
        
        if (table,food) in count_dict:
            count_dict[(table,food)] += 1
            time_dict[(table,food)] += time
        else:
            count_dict[(table,food)] = 1
            time_dict[(table,food)] = time
     
    res = []
    foods = sorted(list(foods))
    res.append(["Table"] + foods)
    
    for table in sorted(list(tables)):
        row = [str(table)]
        for food in foods:
            if (table,food) in count_dict:
                ave_time = round(time_dict[(table,food)]/count_dict[(table,food)])
                row.append(str(count_dict[(table,food)]) + " ("+str(ave_time)+")")
            else:
                row.append("0 (0)")
        res.append(row)
        
    return res