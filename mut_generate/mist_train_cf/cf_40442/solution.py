"""
QUESTION:
Implement a function `findBestServer` that takes a dictionary `fullData` as input, where keys are server names and values are lists of CPU usage data for each user on that server. The function should return the name of the best server based on the following criteria: 
1. The server with the minimum average CPU usage across all users.
2. If there are multiple servers with the same minimum average CPU usage, then select the server with the fewest users.
"""

def findBestServer(fullData):
    def averageCPU(server, data):
        return sum(data[server]) / len(data[server])

    def numUsers(server, data):
        return len(data[server])

    def findMin(valueFunction, data):
        minValue = None
        minServers = []
        for server in data:
            if data[server]:
                value = valueFunction(server, data)
                if minValue is None or value < minValue:
                    minValue = value
                    minServers = [server]
                elif value == minValue:
                    minServers.append(server)
        return minServers

    minAvgCPU = findMin(averageCPU, fullData)
    if len(minAvgCPU) == 1:
        return minAvgCPU[0]
    else:
        minUsers = findMin(numUsers, {server: fullData[server] for server in minAvgCPU})
        return minUsers[0]