"""
QUESTION:
Implement the `ItemToTest` class with the following requirements:

- Create an `ItemToTest` class with a method `add_to_TestingQueue(self, PrivateTest=False)` that adds the item to a `TestingQueue` if `PrivateTest` is False or to a `PrivateTestingQueue` if `PrivateTest` is True.
- Implement a `remove_from_testing_list(self)` method that removes the item from either `TestingQueue` or `PrivateTestingQueue` depending on where it is located.
- Include an `update_state(self, new_state)` method that updates the item's state.
- The class should also maintain a `state` attribute with an initial value of `'Not_tested'`.
- The class should assume that `TestingQueue` and `PrivateTestingQueue` are lists and are accessible as attributes of an object named `City`.
"""

def item_to_test(City):
    class ItemToTest:
        def __init__(self):
            self.state = 'Not_tested'
        
        def add_to_testing_queue(self, PrivateTest=False):
            if PrivateTest:
                City.PrivateTestingQueue.append(self)
            else:
                City.TestingQueue.append(self)
        
        def remove_from_testing_list(self):
            if self in City.TestingQueue:
                City.TestingQueue.remove(self)
            elif self in City.PrivateTestingQueue:
                City.PrivateTestingQueue.remove(self)
        
        def update_state(self, new_state):
            self.state = new_state

    return ItemToTest