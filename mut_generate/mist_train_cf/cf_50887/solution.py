"""
QUESTION:
Create a function `makeWebhookResult(req)` that takes a JSON object `req` as input and returns a JSON object containing a 'speech' field with the text to be spoken by the voice assistant. The returned JSON object should also include 'displayText' and 'source' fields. The function should be part of a Flask app that listens for POST requests on the '/webhook' route and runs on port 5000 in debug mode.
"""

def makeWebhookResult(req):
    # Put your logic here...
    speech = "Put your speech response here... e.g. Hello User!"
    return {"speech": speech,
            "displayText": speech,
            "source": "webhookdata"}