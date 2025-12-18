"""
QUESTION:
There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, presented as binary strings, determine the maximum number of topics a 2-person team can know. Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not.  Also determine the number of teams that know the maximum number of topics.  Return an integer array with two elements.  The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.  

Example  

$n=3$ 

$to pics=[\text{'}10101\text{'},\text{'}11110\text{'},\text{'}00010\text{'}]$  

The attendee data is aligned for clarity below:

10101
11110
00010

These are all possible teams that can be formed:

Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]

In this case, the first team will know all 5 subjects.  They are the only team that can be created that knows that many subjects, so $[5,1]$ is returned.

Function Description  

Complete the acmTeam function in the editor below. 

acmTeam has the following parameter(s):  

string topic: a string of binary digits  

Returns  

int[2]:  the maximum topics and the number of teams that know that many topics   

Input Format

The first line contains two space-separated integers $n$ and $m$, where $n$ is the number of attendees and $m$ is the number of topics.  

Each of the next $n$ lines contains a binary string of length $m$.  

Constraints

$2\leq n\leq500$ 

$1\leq m\leq500$ 

Sample Input
4 5
10101
11100
11010
00101

Sample Output
5
2

Explanation

Calculating topics known for all permutations of 2 attendees we get:  

$(1,2)\rightarrow4$ 

$(1,3)\rightarrow5$ 

$(1,4)\rightarrow3$ 

$(2,3)\rightarrow4$ 

$(2,4)\rightarrow4$ 

$(3,4)\rightarrow5$  

The 2 teams (1, 3) and (3, 4) know all 5 topics which is maximal.
"""

def acm_team_max_topics(topics):
    def merge(p1, p2):
        count = 0
        for i in range(len(p1)):
            if p1[i] == '1' or p2[i] == '1':
                count += 1
        return count
    
    n = len(topics)
    mxcount = 0
    mxteams = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            count = merge(topics[i], topics[j])
            if count > mxcount:
                mxcount = count
                mxteams = 1
            elif count == mxcount:
                mxteams += 1
    
    return [mxcount, mxteams]