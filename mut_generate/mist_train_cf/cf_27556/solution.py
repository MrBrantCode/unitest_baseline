"""
QUESTION:
Create a function `process_wallet_objects(wallet_objects)` that takes a list of JSON strings representing wallet objects, performs specific assertions on the objects' attributes, and raises an AssertionError if any of the assertions fail. 

The function should iterate through each object in the `wallet_objects` list and perform the following assertions:
- If the object's "addr" attribute is "something:5", the "name" attribute should be "myuser_5".
- If the object's "addr" attribute is "something:4", the "name" attribute should be "myuser_4".
- If the object's "addr" attribute is "something:3", the "name" attribute should be "myuser_3", and the "id" attribute should be stored in a variable.
- If the object's "addr" attribute is "something:2", no specific assertion is required.

The input `wallet_objects` is a list of JSON strings, where each string represents an object obtained from the wallet. The function should return the "id" attribute of the object with "addr" attribute "something:3" if needed.
"""

import json

def process_wallet_objects(wallet_objects):
    obj_id_3 = None  
    for obj_str in wallet_objects:
        obj = json.loads(obj_str)
        if obj["addr"] == "something:5":
            assert obj["name"] == "myuser_5", f"Assertion failed for object with addr 'something:5'"
        if obj["addr"] == "something:4":
            assert obj["name"] == "myuser_4", f"Assertion failed for object with addr 'something:4'"
        if obj["addr"] == "something:3":
            assert obj["name"] == "myuser_3", f"Assertion failed for object with addr 'something:3'"
            obj_id_3 = obj["id"]  
        if obj["addr"] == "something:2":
            pass  
    return obj_id_3 