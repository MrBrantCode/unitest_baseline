"""
QUESTION:
Implement a function `update_node_status(batch_size, all_or_nothing_batch, boto3_response)` that takes in a batch size, a flag indicating whether the update should be all-or-nothing, and a mock Boto3 response. It should update the nodes based on the response and return the number of failed nodes, the number of update calls made, and the list of nodes that were successfully updated.
"""

def update_node_status(batch_size, all_or_nothing_batch, boto3_response):
    failed_nodes = 0
    update_node_calls = 0
    assigned_nodes = []
    
    if all_or_nothing_batch:
        if boto3_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            assigned_nodes = boto3_response['NodeInfoList']
        else:
            failed_nodes = len(boto3_response.get('NodeInfoList', []))
    else:
        for node in boto3_response.get('NodeInfoList', []):
            try:
                # Update the node status
                update_node_calls += 1
                assigned_nodes.append(node)
            except Exception:
                failed_nodes += 1

    return failed_nodes, update_node_calls, assigned_nodes