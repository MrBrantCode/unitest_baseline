"""
QUESTION:
Create a function called `create_sunburst_chart` to visualize hierarchical team information and performance metrics in a dynamic sunburst chart. The chart should be partitioned by team and sorted by team and performance score. 

The input should be a list of team members with their name, team, and performance score. The function should be able to update the chart dynamically as new team members are added, existing members are removed, or their performance changes. The function should also be efficient and scalable for larger data sets.
"""

def create_sunburst_chart(team_members):
    # Assuming team_members is a list of dictionaries containing team member information
    # For example, team_members = [
    #     {'name': 'John', 'team': 'A', 'performance': 90},
    #     {'name': 'Jane', 'team': 'A', 'performance': 80},
    #     {'name': 'Alice', 'team': 'B', 'performance': 95},
    #     {'name': 'Bob', 'team': 'B', 'performance': 85}
    # ]

    # Processing data into a hierarchical structure
    hierarchical_data = {}
    for member in team_members:
        team = member['team']
        if team not in hierarchical_data:
            hierarchical_data[team] = []
        hierarchical_data[team].append(member)

    # Sorting team members within each team by performance scores
    for team in hierarchical_data:
        hierarchical_data[team] = sorted(hierarchical_data[team], key=lambda x: x['performance'], reverse=True)

    # Creating the sunburst chart (note: this part is not implemented here as it requires JavaScript and D3.js)
    # You can use a library like plotly or bokeh to create a sunburst chart in Python
    # However, these libraries may not be as powerful as D3.js for dynamic visualizations
    return hierarchical_data