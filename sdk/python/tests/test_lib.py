import unittest
import arin

class TestLib(unittest.TestCase):

    def test_leor(self):
        self.assertEqual(arin.to_leor(0.5), 50000000)
        self.assertEqual(arin.from_leor(5000000), 0.05)

if __name__ == "__main__":
    unittest.main()