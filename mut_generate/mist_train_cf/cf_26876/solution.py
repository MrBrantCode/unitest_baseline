"""
QUESTION:
Given a list of rules describing which bags can contain other bags, write a function `count_bags_containing_shiny_gold` that takes in the list of rules and returns the total number of bags that can contain at least one shiny gold bag. Each rule is a string in the format "color bags contain count color bags, count color bags." where "color" is the color of the bag, "count" is the number of bags of that color, and the list of contained bags is comma-separated. The function should return the number of individual bags that can eventually contain a shiny gold bag.
"""

import re

def count_bags_containing_shiny_gold(rules):
    bag_map = {}
    for rule in rules:
        color, contents = re.match(r'^([a-z ]+) bags contain (.*)\.$', rule).groups()
        if contents == "no other bags":
            continue
        for count, inner_color in re.findall(r'(\d+) ([a-z ]+) bags?', contents):
            if inner_color not in bag_map:
                bag_map[inner_color] = set()
            bag_map[inner_color].add(color)

    containing_bags = set()
    queue = ["shiny gold"]
    while queue:
        current_bag = queue.pop(0)
        for bag in bag_map.get(current_bag, []):
            if bag not in containing_bags:
                containing_bags.add(bag)
                queue.append(bag)

    return len(containing_bags)