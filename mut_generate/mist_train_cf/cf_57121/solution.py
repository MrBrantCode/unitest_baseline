"""
QUESTION:
Design a function named `update_project_status` that takes in a DynamoDB event as input and returns a JSON response. The function should be able to handle DynamoDB events triggered by project initiation, alteration, or deletion, and update the project status accordingly. The function should not have any latency and should be able to manage the instability of project coordination.
"""

import json

def update_project_status(event):
    """
    This function updates the project status based on the DynamoDB event.

    Args:
        event (dict): The DynamoDB event.

    Returns:
        dict: A JSON response.
    """
    
    # Get the project status from the DynamoDB event
    project_status = event['Records'][0]['eventName']

    # Update the project status based on the event
    if project_status == 'INSERT':
        # Project initiation
        updated_status = 'initiated'
    elif project_status == 'MODIFY':
        # Project alteration
        updated_status = 'altered'
    elif project_status == 'REMOVE':
        # Project deletion
        updated_status = 'deleted'

    # Return a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'project_status': updated_status})
    }