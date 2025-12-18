from solution import entrance
### Test Cases
import unittest

class TestQuantityRegistry(unittest.TestCase):
    def setUp(self):
        # Clear the registry before each test case
        entrance.registry.clear()

    def test_register_quantity(self):
        # Test registering a new quantity
        entrance("length", "meters")
        self.assertEqual(entrance.registry["length"], "meters")

    def test_get_units(self):
        # Test retrieving units of a registered quantity
        entrance("length", "meters")
        self.assertEqual(entrance("length", quantity_name="length"), "meters")

        # Test retrieving units of an unregistered quantity
        self.assertEqual(entrance("speed", quantity_name="speed"), "Quantity not found")

    def test_get_all_quantities(self):
        # Test retrieving all registered quantities
        entrance("length", "meters")
        entrance("speed", "m/s")
        self.assertEqual(set(entrance("all", get_all=True)), set(["length", "speed"]))

    def test_invalid_usage(self):
        # Test invalid usage: trying to register without units
        self.assertIsNone(entrance("length"))

        # Test invalid usage: trying to retrieve units without a quantity name
        self.assertIsNone(entrance("length", units="meters"))

if __name__ == '__main__':
    unittest.main()
