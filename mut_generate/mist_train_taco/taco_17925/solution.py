"""
QUESTION:
You are a real estate broker in ancient Knossos. You have $m$ unsold houses, and each house $j$ has an area, $x_j$, and a minimum price, $y_j$. You also have $n$ clients, and each client $\boldsymbol{i}$ wants a house with an area greater than $a_i$ and a price less than or equal to $p_i$.

Each client can buy at most one house, and each house can have at most one owner. What is the maximum number of houses you can sell?

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of clients) and $m$ (the number of houses). 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $a_i$ and $p_i$ for client $\boldsymbol{i}$. 

Each line $j$ of the $m$ subsequent lines contains two space-separated integers describing the respective values of $x_j$ and $y_j$ for house $j$.

Constraints

$1\leq n,m\leq1000$
$1\leq a_i,p_i\leq10^9$, where $0\leq i<n$.
$1\leq x_j,y_j\leq10^9$, where $0\leq j\lt m$.

Output Format

Print a single integer denoting the maximum number of houses you can sell.

Sample Input 0
3 3
5 110
9 500
20 400
10 100
2 200
30 300

Sample Output 0
2

Explanation 0

Recall that each client $\boldsymbol{i}$ is only interested in some house $j$ where $x_j>a_i$ and $y_j\leq p_i$. The diagram below depicts which clients will be interested in which houses:

Client $\mbox{o}$ will be interested in house $\mbox{o}$ because it has more than $a_{0}=5$ units of space and costs less than $p_{0}=110$. Both of the other houses are outside of this client's price range.
Client $\mbox{I}$ will be interested in houses $\mbox{o}$ and $2$, as both these houses have more than $a_1=9$ units of space and cost less than $p_1=500$. They will not be interested in the remaining house because it's too small.
Client $2$ will be interested in house $2$ because it has more than $a_{2}=20$ units of space and costs less than $p_2=400$. They will not be interested in the other two houses because they are too small.

All three clients are interested in the same two houses, so you can sell at most two houses in the following scenarios:   

Client $\mbox{o}$ buys house $\mbox{o}$ and client $\mbox{I}$ buys house $2$.
Client $\mbox{I}$ buys house $\mbox{o}$ and client $2$ buys house $2$.
Client $\mbox{o}$ buys house $\mbox{o}$ and client $2$ buys house $2$.

Thus, we print the maximum number of houses you can sell, $2$, on a new line.
"""

def max_houses_sold(clients, houses):
    # Sort clients by their area requirement in descending order
    clients.sort(reverse=True, key=lambda x: x[0])
    # Sort houses by their area in ascending order
    houses.sort(key=lambda x: x[0])
    
    count = 0
    for client in clients:
        # Find the best house for the current client
        best_house_index = -1
        for j in range(len(houses)):
            if houses[j][0] > client[0] and houses[j][1] <= client[1]:
                if best_house_index == -1 or houses[j][1] < houses[best_house_index][1]:
                    best_house_index = j
        
        if best_house_index != -1:
            count += 1
            # Remove the house from the list as it has been sold
            houses.pop(best_house_index)
    
    return count