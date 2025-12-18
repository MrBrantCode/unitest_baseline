"""
QUESTION:
Implement the `slack_to_mattermost` function, which takes a JSON message in Slack format as input and returns a JSON message in Mattermost format. The Slack JSON message is a dictionary with a "blocks" key containing a list of dictionaries, each representing a block of text. The function should transform the Slack message according to the following rules: 
1. If the first block's text contains the ">>>" prefix, remove it and concatenate all block texts into a single string separated by newline characters.
2. If the first block's text does not contain the ">>>" prefix, return the original Slack message as the Mattermost message.
"""

def slack_to_mattermost(slack_json):
    if 'blocks' in slack_json and len(slack_json['blocks']) > 0:
        slack_text = slack_json['blocks'][0]['text']['text'].replace(">>>", "")
        if len(slack_json['blocks']) > 1:
            for block in slack_json['blocks'][1:]:
                slack_text += "\n" + block['text']['text']
        mattermost_json = '{"text": "' + slack_text + '"}'
        return mattermost_json
    else:
        return slack_json