import unittest
from app import add, subtract

class TestMathfunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,10),20,msg="addition error")
        self.assertEqual(add(10,-10),0,msg="addition error")
        
    def test_subtract(self):
        self.assertEqual(subtract(10,-10),20,msg="subtraction error")
        self.assertEqual(subtract(10,10),0,msg="subtraction error")   

if __name__ == "__main__":
    unittest.main()         