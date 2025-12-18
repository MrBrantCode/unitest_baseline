"""
QUESTION:
Create a 'Car' class with a constructor that has parameters 'color' (default 'red'), 'speed' (default 0), and 'mileage' (default 0). Implement the following methods:

- accelerate(speed_increment): Increase the car's speed by the specified speed_increment.
- decelerate(speed_decrement): Decrease the car's speed by the specified speed_decrement without going below 0.
- drive(distance): Simulate driving the car for the given distance at a constant speed, increase the mileage, and update the speed using accelerate and decelerate.
- spray_paint(new_color): Change the car's color to the specified new_color.
"""

def car(color='red', speed=0, mileage=0):
    class Car:
        def __init__(self, color=color, speed=speed, mileage=mileage):
            self.color = color
            self.speed = speed
            self.mileage = mileage

        def accelerate(self, speed_increment):
            self.speed += speed_increment
            return self.speed

        def decelerate(self, speed_decrement):
            self.speed = max(0, self.speed - speed_decrement)
            return self.speed

        def drive(self, distance):
            avg_speed_increment = distance / 100.0 # Just for simulation
            self.accelerate(avg_speed_increment)
            self.mileage += distance
            self.decelerate(avg_speed_increment)
            return self.mileage

        def spray_paint(self, new_color):
            self.color = new_color
            return self.color

    return Car()

class Car(car()):
    def __init__(self, color, speed, mileage):
        super().__init__(color, speed, mileage)