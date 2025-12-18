"""
QUESTION:
Implement a NodeService class with two methods, `get_node` and `update_node`, that handle the retrieval and update of node information. The `get_node` method should return the JSON representation of the node, while the `update_node` method should update the node's name and return the keys of the updated node's data, excluding certain frozen keys ('id', 'name', 'original_name', 'created_at', 'updated_at').
"""

def entrance(request, *args):
    model = request.model
    if request.method == 'GET':
        return {"node": model.json}
    elif request.method == 'POST' or request.method == 'PUT':
        frozen_keys = ['id', 'name', 'original_name', 'created_at', 'updated_at']

        new_name = request.params.get("name")
        if new_name:
            model.node_name = new_name

        model_keys = model.__data__.keys() - set(frozen_keys)
        return list(model_keys)