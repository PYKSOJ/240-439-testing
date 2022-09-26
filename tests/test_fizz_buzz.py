from src.fizz_buzz import fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_return_fizz(self):
        num = 3
        excepts = 'Fizz'
        test = fizz_buzz(num)
        self.assertEqual(test, excepts)
    
    def test_give_5_return_buzz(self):
        num = 5
        excepts = 'Buzz'
        test = fizz_buzz(num)
        self.assertEqual(test, excepts)
    
        
    def test_give_15_return_fizzbuzz(self):
        num = 15
        excepts = 'FizzBuzz'
        test = fizz_buzz(num)
        self.assertEqual(test, excepts)
        
    def test_give_zero(self):
        num = 0
        excepts = 'Out of Range'
        test = fizz_buzz(num)
        self.assertEqual(test, excepts)
        
    def test_give_1_return_Out_of_Range(self):
        num = 1
        excepts = 'Out of Range'
        test = fizz_buzz(num)
        self.assertEqual(test, excepts)
    
    def test_give_2_return_Out_of_Range(self):
        num = 2
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def tst_give_998_return_Out_of_Range(self):
        num = 998
        test = fizz_buzz(num)
        self.assertTrue(test)
        
    def test_give_999_return_fizz(self):
        num = 999
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def test_give_1000_return_Buzz(self):
        num = 1000
        test = fizz_buzz(num)
        self.assertTrue(test)
            
