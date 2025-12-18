"""
QUESTION:
Create a function called `proposal_status` that takes in two parameters: `status` and `recipient`, where `status` is either "accepted" or "rejected". The function should return a message in the format "Dear [recipient's name], [message]". The message should be "unfortunately your proposal has been rejected" if the status is "rejected", and "congratulations on your successful proposal" if the status is "accepted". The function must use only one if statement and one return statement.
"""

def proposal_status(status, recipient):
    return "Dear " + recipient + ", " + ("unfortunately your proposal has been rejected." if status == "rejected" else "congratulations on your successful proposal.")