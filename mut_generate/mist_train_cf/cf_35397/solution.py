"""
QUESTION:
Implement a function `popularNFeatures` that takes in five parameters: 
- `numFeatures`: the number of features in the company's database.
- `topFeatures`: the number of most popular features to return.
- `possibleFeatures`: a list of strings representing the features available in the company's database.
- `numFeatureRequests`: the number of feature requests received.
- `featureRequests`: a list of strings representing the feature requests received from customers.

Return a list of the top `topFeatures` most popular features mentioned in the feature requests, with popularity determined by the number of times a feature is mentioned. In the event of a tie, list features in lexicographical order.
"""

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests):
    featureCount = {feature: 0 for feature in possibleFeatures}

    for request in featureRequests:
        words = request.lower().split()
        for feature in possibleFeatures:
            if feature in words:
                featureCount[feature] += 1

    sortedFeatures = sorted(featureCount.keys(), key=lambda x: (-featureCount[x], x))
    return sortedFeatures[:topFeatures]