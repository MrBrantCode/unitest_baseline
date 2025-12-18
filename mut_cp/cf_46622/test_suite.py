from solution import american_put_derivative
### Note: This function assumes that the optimal stopping time τ* is known and given by the parameter tau. In practice, this would be determined based on the specific conditions of the option and the underlying asset.

import unittest
import math

class TestAmericanPutDerivative(unittest.TestCase):
    """
    Test class for the american_put_derivative function.
    """

    def test_derivative_when_Xtau_less_than_K(self):
        """
        Test the derivative when the underlying asset price at time tau (X_tau) is less than the strike price (K).
        Expected result: -exp(-r * tau)
        """
        X0 = 100.0  # Underlying asset price at time 0
        K = 120.0   # Strike price
        r = 0.05    # Risk-free rate
        tau = 1.0   # Optimal stopping time
        X_tau = 110.0  # Underlying asset price at time tau

        expected_derivative = -math.exp(-r * tau)
        actual_derivative = american_put_derivative(X0, K, r, tau, X_tau)

        self.assertAlmostEqual(actual_derivative, expected_derivative, places=5)

    def test_derivative_when_Xtau_equal_to_K(self):
        """
        Test the derivative when the underlying asset price at time tau (X_tau) is equal to the strike price (K).
        Expected result: 0
        """
        X0 = 100.0  # Underlying asset price at time 0
        K = 120.0   # Strike price
        r = 0.05    # Risk-free rate
        tau = 1.0   # Optimal stopping time
        X_tau = 120.0  # Underlying asset price at time tau

        expected_derivative = 0
        actual_derivative = american_put_derivative(X0, K, r, tau, X_tau)

        self.assertEqual(actual_derivative, expected_derivative)

    def test_derivative_when_Xtau_greater_than_K(self):
        """
        Test the derivative when the underlying asset price at time tau (X_tau) is greater than the strike price (K).
        Expected result: 0
        """
        X0 = 100.0  # Underlying asset price at time 0
        K = 120.0   # Strike price
        r = 0.05    # Risk-free rate
        tau = 1.0   # Optimal stopping time
        X_tau = 130.0  # Underlying asset price at time tau

        expected_derivative = 0
        actual_derivative = american_put_derivative(X0, K, r, tau, X_tau)

        self.assertEqual(actual_derivative, expected_derivative)    

if __name__ == '__main__':
    unittest.main()
