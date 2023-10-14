import unittest
import prices


class TestDoSomething(unittest.TestCase):
    def test_T1(self):
        amount=2
        price=20000

        captured_output = prices.price_calculator(amount, price)

        expected_output = 40000
        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)

    def test_T2(self):
        amount=5
        price=20000

        captured_output = prices.price_calculator(amount, price)

        expected_output = 95000
        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T3(self):
        amount=10
        price=20000

        captured_output = prices.price_calculator(amount, price)

        expected_output = 180000
        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
if __name__ == "__main__":
    unittest.main()