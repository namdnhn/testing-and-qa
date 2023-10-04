import unittest
import banking


class TestDoSomething(unittest.TestCase):
    def test_T1(self):
        id = "test"
        mission = "withdraw"
        money = 1000000

        captured_output = banking.doSomething(id, mission, money)

        expected_output = "ID không tồn tại."
        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)

    def test_T2(self):
        id = 'donhuhoangnam'
        mission = "withdraw"
        money = -1000
        expected_output = "Số tiền phải lớn hơn 0."

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T3(self):
        id = 'donhuhoangnam'
        mission = "withdraw"
        money = 100000000
        expected_output = "Số dư của bạn không đủ."

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T4(self):
        id = 'phananhngoc'
        mission = "withdraw"
        money = 1000000
        expected_output = "Bạn đã rút thành công 1000000 VNĐ. Số dư của bạn là 18000000 VNĐ."

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T5(self):
        id = 'hothugiang'
        mission = 'deposit'
        money = -1000
        expected_output = "Số tiền phải lớn hơn 0."

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T6(self):
        id = 'trinhkieuanh'
        mission = 'deposit'
        money = 1000000
        expected_output = "Bạn đã nạp thành công 1000000 VNĐ. Số dư của bạn là 15000000 VNĐ."

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    def test_T7(self):
        id = 'hothugiang'
        mission = 'test'
        money = 1000000
        expected_output = "Thao tác không hợp lệ"

        captured_output = banking.doSomething(id, mission, money)

        print(captured_output)
        print(expected_output)
        self.assertEqual(captured_output, expected_output)
        
    


if __name__ == "__main__":
    unittest.main()