import unittest
from main import calculate_sinus, calculate_cosinus
import numpy as np

class TestTrigonometricFunctions(unittest.TestCase):

    def test_calculate_sine(self):
        self.assertAlmostEqual(calculate_sinus(0), 0)
        self.assertAlmostEqual(calculate_sinus(np.pi / 2), 1)
        self.assertAlmostEqual(calculate_sinus(np.pi), 0)
        self.assertAlmostEqual(calculate_sinus(3 * np.pi / 2), -1)
        self.assertAlmostEqual(calculate_sinus(np.pi / 4), np.sqrt(2) / 2)

    def test_calculate_cosine(self):
        self.assertAlmostEqual(calculate_cosinus(0), 1)
        self.assertAlmostEqual(calculate_cosinus(np.pi / 2), 0)
        self.assertAlmostEqual(calculate_cosinus(np.pi), -1)
        self.assertAlmostEqual(calculate_cosinus(3 * np.pi / 2), 0)
        self.assertAlmostEqual(calculate_cosinus(np.pi / 4), np.sqrt(2) / 2)

if __name__ == "__main__":
    unittest.main()
#last_changes