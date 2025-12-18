"""
QUESTION:
Create a class named `RemoteControl` that includes a method named `change_battery` to set the battery level manually, a method named `display_battery_level` to display the current battery level, and a method named `display_button_press_count` to display the number of times the `press_button` method has been called. The class should also keep track of the number of times the `press_button` method has been called. The `change_battery` method should accept a parameter for the desired battery level.
"""

def entance(brand, is_bluetooth):
    class RemoteControl:
        def __init__(self, brand, is_bluetooth):
            self.brand = brand
            self.is_bluetooth = is_bluetooth
            self.__battery_level = 100
            self.__location = (0,0)
            self.__button_press_count = 0
        
        def change_battery(self, battery_level):
            self.__battery_level = battery_level
        
        def move(self, x, y):
            self.__location = (x,y)
            
        def press_button(self):
            if self.is_bluetooth:
                print("Command sent via Bluetooth")
            else:
                print("Command sent via IR signal")
            self.__battery_level -= 15  # a random value between 5 to 20
            self.__button_press_count += 1
        
        def display_battery_level(self):
            print("Current battery level:", self.__battery_level)
            
        def display_button_press_count(self):
            print("Button press count:", self.__button_press_count)

    return RemoteControl(brand, is_bluetooth)