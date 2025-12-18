"""
QUESTION:
Design a data structure with the following methods: 
- `add(string)`: Adds a new string to the data structure at the end, ensuring uniqueness. If the string already exists, do not add it again and return false. Otherwise, add it and return true.
- `get_by_index(index)`: Retrieves the string at the specified index position. If the index is out of range, return null.
- `get_by_value(string)`: Retrieves the index position of the specified string. If the string does not exist, return -1.

Restrictions: 
- The data structure should allow for fast lookup by both index position and value.
- The data structure should not rely on any built-in data structures or libraries for string indexing or lookup.
- The implementation should be efficient in terms of time and space complexity.
"""

def entrance(string, index=None):
    class DataStructure:
        def __init__(self):
            self.string_map = {}  # hash table
            self.string_list = []  # array

        def add(self, string):
            if string in self.string_map:  # check if string already exists
                return False
            
            index = len(self.string_list)  # get the index position
            self.string_map[string] = index  # store the index in the hash table
            self.string_list.append(string)  # add the string to the array
            return True

        def get_by_index(self, index):
            if index < 0 or index >= len(self.string_list):  # check if index is out of range
                return None
            return self.string_list[index]

        def get_by_value(self, string):
            if string not in self.string_map:  # check if string exists
                return -1
            return self.string_map[string]
    
    data_structure = DataStructure()
    
    if index is None:
        return data_structure.add(string)
    elif string == 'index':
        return data_structure.get_by_index(index)
    else:
        return data_structure.get_by_value(string)