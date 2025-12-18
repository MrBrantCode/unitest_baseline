"""
QUESTION:
You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, but things have gotten a little boring. You've each decided to add some amazing new features to your robot and automate them to battle to the death.

Each robot will be represented by an object. You will be given two robot objects, and an object of battle tactics and how much damage they produce. Each robot will have a name, hit points, speed, and then a list of battle tacitcs they are to perform in order. Whichever robot has the best speed, will attack first with one battle tactic. 

Your job is to decide who wins.

Example:
```python
 robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
 fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."
```

robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35. Now robot1 uses a punch, and so on. 

**Rules**

- A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
- Robots alternate turns attacking. Tactics are used in order.
- A fight is over when a robot has 0 or less health or both robots have run out of tactics.
- A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
- If both robots run out of tactics, whoever has the most health wins. Return the message "{Name} has won the fight."
- If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw."

**To Java warriors**

`Robot` class is immutable.


Check out my other 80's Kids Katas:


80's Kids #1: How Many Licks Does It Take
80's Kids #2: Help Alf Find His Spaceship
80's Kids #3: Punky Brewster's Socks
80's Kids #4: Legends of the Hidden Temple
80's Kids #5: You Can't Do That on Television
80's Kids #6: Rock 'Em, Sock 'Em Robots
80's Kids #7: She's a Small Wonder
80's Kids #8: The Secret World of Alex Mack
80's Kids #9: Down in Fraggle Rock 
80's Kids #10: Captain Planet
"""

def determine_robot_battle_winner(robot_1, robot_2, tactics):
    # Determine the order of attack based on speed
    if robot_1['speed'] >= robot_2['speed']:
        first_robot, second_robot = robot_1, robot_2
    else:
        first_robot, second_robot = robot_2, robot_1
    
    # Initialize indices for tactics
    first_tactic_index = 0
    second_tactic_index = 0
    
    # Battle loop
    while first_tactic_index < len(first_robot['tactics']) or second_tactic_index < len(second_robot['tactics']):
        # First robot attacks
        if first_tactic_index < len(first_robot['tactics']):
            tactic = first_robot['tactics'][first_tactic_index]
            second_robot['health'] -= tactics[tactic]
            first_tactic_index += 1
            if second_robot['health'] <= 0:
                return f"{first_robot['name']} has won the fight."
        
        # Second robot attacks
        if second_tactic_index < len(second_robot['tactics']):
            tactic = second_robot['tactics'][second_tactic_index]
            first_robot['health'] -= tactics[tactic]
            second_tactic_index += 1
            if first_robot['health'] <= 0:
                return f"{second_robot['name']} has won the fight."
    
    # Determine the winner based on remaining health
    if first_robot['health'] > second_robot['health']:
        return f"{first_robot['name']} has won the fight."
    elif second_robot['health'] > first_robot['health']:
        return f"{second_robot['name']} has won the fight."
    else:
        return "The fight was a draw."