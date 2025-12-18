"""
QUESTION:
Implement a function `createAndroidApp` that displays a list of items from a local database. The function should include the following features: 
- Add, edit, and delete items from the database.
- Search for specific items in the list.
- Sort the list based on a specific attribute.
- Filter the list based on multiple criteria.
The function should also ensure that the list is updated in real-time when changes are made to the database, and handle large amounts of data efficiently with caching mechanisms.
"""

def createAndroidApp(db_name, table_name):
    class AndroidApp:
        def __init__(self, db_name, table_name):
            self.db_name = db_name
            self.table_name = table_name
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)")
            self.conn.commit()

        def add_item(self, name, description):
            self.cursor.execute(f"INSERT INTO {self.table_name} (name, description) VALUES (?, ?)", (name, description))
            self.conn.commit()

        def edit_item(self, id, name, description):
            self.cursor.execute(f"UPDATE {self.table_name} SET name = ?, description = ? WHERE id = ?", (name, description, id))
            self.conn.commit()

        def delete_item(self, id):
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (id,))
            self.conn.commit()

        def search_item(self, query):
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE name LIKE ?", ('%' + query + '%',))
            return self.cursor.fetchall()

        def sort_items(self, attribute):
            self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY {attribute}")
            return self.cursor.fetchall()

        def filter_items(self, criteria):
            query = "SELECT * FROM {} WHERE ".format(self.table_name)
            values = []
            for key, value in criteria.items():
                query += "{} = ? AND ".format(key)
                values.append(value)
            query = query[:-5]  # Remove the extra " AND "
            self.cursor.execute(query, values)
            return self.cursor.fetchall()

    return AndroidApp(db_name, table_name)