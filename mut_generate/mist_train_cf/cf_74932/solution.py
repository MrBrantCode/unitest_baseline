"""
QUESTION:
Design a class called "Transport" with attributes 'type', 'speed', 'capacity', and 'cost'. Create three subclasses: "LandTransport", "SeaTransport", and "AirTransport", each with a unique attribute. Implement methods in the "Transport" class to calculate cost-effectiveness and estimate transportation time based on distance and speed. Include error handling for division by zero. The "LandTransport" subclass should have an attribute 'wheel_count', "SeaTransport" should have an attribute 'draft', and "AirTransport" should have an attribute 'altitude'.
"""

def entrance(type, speed, capacity, cost, distance, wheel_count=None, draft=None, altitude=None):
    class Transport:
        def __init__(self, type, speed, capacity, cost):
            self.type = type
            self.speed = speed
            self.capacity = capacity
            self.cost = cost

        def cost_effectiveness(self):
            try:
                return self.capacity / self.cost
            except ZeroDivisionError:
                return "Cost can't be 0."
                
        def estimate_time(self, distance):
            try:
                return distance / self.speed
            except ZeroDivisionError:
                return "Speed can't be 0."

    class LandTransport(Transport):
        def __init__(self, speed, capacity, cost, wheel_count):
            super().__init__('land', speed, capacity, cost)
            self.wheel_count = wheel_count

    class SeaTransport(Transport):
        def __init__(self, speed, capacity, cost, draft):
            super().__init__('sea', speed, capacity, cost)
            self.draft = draft

    class AirTransport(Transport):
        def __init__(self, speed, capacity, cost, altitude):
            super().__init__('air', speed, capacity, cost)
            self.altitude = altitude

    if type == 'land':
        transport = LandTransport(speed, capacity, cost, wheel_count)
    elif type == 'sea':
        transport = SeaTransport(speed, capacity, cost, draft)
    elif type == 'air':
        transport = AirTransport(speed, capacity, cost, altitude)
    else:
        return "Invalid transport type."
    
    return transport.cost_effectiveness(), transport.estimate_time(distance)