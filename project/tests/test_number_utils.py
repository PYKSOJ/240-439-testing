from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase): 
    def test_give_true_is_prinme(self):    
        prime_list = [3]
        is_prime = is_prime_list(prime_list)    
        self.assertTrue(is_prime)
    # Corrct Case
    def test_give_odd_prime_list(self):
        tmp = [2, 4, 6] #2 is prime
        is_prime = is_prime_list(tmp)
        self.assertTrue(is_prime) 
    # Correct Case
    def test_give_even_prime_list(self):
        tmp = [3, 5, 7] # every argument are prime
        is_prime = is_prime_list(tmp)   
        self.assertTrue(is_prime) 
    # Correct Case
    def test_give_zero_prime_list(self):
        tmp = [0]
        is_prime = is_prime_list(tmp)
        self.assertTrue(is_prime)
    # Corrct Case
    def test_give_negative_prime_list(self):
        tmp = [-2]
        is_prime = is_prime_list(tmp)
        self.assertTrue(is_prime)
    # Corrct Case