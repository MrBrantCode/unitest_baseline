from solution import is_prime
### test cases
import unittest

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        # Test case 1: Normal range with primes
        self.assertEqual(is_prime(10, 20), {10: False, 11: True, 12: False, 13: True, 14: False, 15: False, 16: False, 17: True, 18: False, 19: True, 20: False})
        
        # Test case 2: Range starting from 2
        self.assertEqual(is_prime(2, 10), {2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False})
        
        # Test case 3: Range with no primes
        self.assertEqual(is_prime(14, 16), {14: False, 15: False, 16: False})
        
        # Test case 4: Edge case with n = m
        self.assertEqual(is_prime(17, 17), {17: True})
        
        # Test case 5: Edge case with n > m
        self.assertEqual(is_prime(20, 10), {})
        
        # Test case 6: Edge case with n < 2
        self.assertEqual(is_prime(1, 10), {2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False})  # Modified output
        
        # Test case 7: Large range
        self.assertEqual(is_prime(100, 200), {100: False, 101: True, 102: False, 103: True, 104: False, 105: False, 106: False, 107: True, 108: False, 109: True, 110: False, 111: False, 112: False, 113: True, 114: False, 115: False, 116: False, 117: False, 118: False, 119: False, 120: False, 121: False, 122: False, 123: False, 124: False, 125: False, 126: False, 127: True, 128: False, 129: False, 130: False, 131: True, 132: False, 133: False, 134: False, 135: False, 136: False, 137: True, 138: False, 139: True, 140: False, 141: False, 142: False, 143: False, 144: False, 145: False, 146: False, 147: False, 148: False, 149: True, 150: False, 151: True, 152: False, 153: False, 154: False, 155: False, 156: False, 157: True, 158: False, 159: False, 160: False, 161: False, 162: False, 163: True, 164: False, 165: False, 166: False, 167: True, 168: False, 169: False, 170: False, 171: False, 172: False, 173: True, 174: False, 175: False, 176: False, 177: False, 178: False, 179: True, 180: False, 181: True, 182: False, 183: False, 184: False, 185: False, 186: False, 187: False, 188: False, 189: False, 190: False, 191: True, 192: False, 193: True, 194: False, 195: False, 196: False, 197: True, 198: False, 199: True, 200: False})  # Modified output

if __name__ == '__main__':
    unittest.main()
