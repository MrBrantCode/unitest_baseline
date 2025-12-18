"""
QUESTION:
Create a parameterized query in Python to find the details of a person, ensuring that the query retrieves data from at least three related tables and includes multiple join conditions. The function, `get_person_details`, should take three parameters: `age_threshold`, `city`, and `order_amount_threshold`. The query should filter the results to include only records where the person's age is greater than `age_threshold`, their city matches `city`, and the total amount of their orders is greater than `order_amount_threshold`.
"""

import sqlite3

def get_person_details(age_threshold, city, order_amount_threshold):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = """
    SELECT person.name, person.address, person.phone, person.email, orders.order_date, orders.total_amount, products.product_name
    FROM person
    JOIN orders ON person.id = orders.person_id
    JOIN order_items ON orders.order_id = order_items.order_id
    JOIN products ON order_items.product_id = products.product_id
    WHERE person.age > ?
    AND person.city = ?
    AND orders.total_amount > ?
    """
    
    cursor.execute(query, (age_threshold, city, order_amount_threshold))
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return result