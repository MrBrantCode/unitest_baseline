"""
QUESTION:
Write a function `min_travel_cost` that calculates the minimum cost of a travel itinerary given a list of lists `days` representing the cost of staying in each city on each week, and a matrix `flights` representing the availability of flights between cities, assuming the trip starts and ends in city 0 and includes the cost of flights. The function should return the minimum cost of the travel itinerary.
"""

def min_travel_cost(days, flights):
    num_cities = len(days)
    num_weeks = len(days[0])
    
    dp = [[0] * num_cities for _ in range(2)]
    
    for week in range(num_weeks - 1, -1, -1):
        for cur_city in range(num_cities):
            dp[week % 2][cur_city] = days[cur_city][week] + dp[(week + 1) % 2][cur_city]
            for dest_city in range(num_cities):
                if flights[cur_city][dest_city] == 1:
                    dp[week % 2][cur_city] = max(dp[week % 2][cur_city], 
                                                 days[dest_city][week] + dp[(week + 1) % 2][dest_city])
    
    return dp[0][0]