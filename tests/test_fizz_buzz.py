from src.fizz_buzz import fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_alway_true_1(self):
        num = 3
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def test_give_alway_true_2(self):
        num = 5
        test = fizz_buzz(num)   
        self.assertTrue(test)
        
    def test_give_alway_true_3(self):
        num = 15
        test = fizz_buzz(num)   
        self.assertTrue(test)
        
    def test_give_zero(self):
        num = 0
        test = fizz_buzz(num) 
        self.assertTrue(test)
        
    def test_give_lowest(self):
        num = 1
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def test_give_almost_lowest(self):
        num = 2
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def tst_give_almost_heightest(self):
        num = 998
        test = fizz_buzz(num)
        self.assertTrue(test)
        
    def test_give_almost_heightest(self):
        num = 999
        test = fizz_buzz(num)
        self.assertTrue(test)
    
    def test_give_heighter_of_range(self):
        num = 1000
        test = fizz_buzz(num)
        self.assertTrue(test)
            
