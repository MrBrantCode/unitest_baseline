"""
QUESTION:
Implement the `addClient` function to add a client to a database. The function takes a JSON object as input through a `request` object and must validate the presence of "name" and "email" fields. If both fields are present, add the client to the database and return a success message. If either field is missing, return an error message specifying the missing field. Assume the existence of a database and necessary functions to interact with it.
"""

def addClient(request):
    if "name" in request.json and "email" in request.json:
        name = request.json['name']
        email = request.json['email']
        # Assuming the existence of a database and a function to add a client
        # Add client to the database
        # return success message
        return "Client added successfully"
    else:
        # Return error message for missing fields
        if "name" not in request.json:
            return "Error: Missing 'name' field"
        else:
            return "Error: Missing 'email' field"