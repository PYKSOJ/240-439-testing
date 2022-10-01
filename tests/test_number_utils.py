from src.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_2_return_is_Prime_numbers(self):
        prime_list = [2]
        expects = 'is Prime numbers'
        is_prime = is_prime_list(prime_list)
        self.assertEqual(expects, is_prime)

    def test_give_2_4_6_return_is_not_Prime_numbers(self):
        tmp = [2, 4, 6]  # 2 is prime
        expects = 'is n\'t Prime numbers'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)

    def test_give_3_5_7_return_is_prime_numbers(self):
        tmp = [3, 5, 7]  # every argument are prime
        expects = 'is Prime numbers'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)

    def test_give_1_return_error(self):
        tmp = [1]
        expects = 'error'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)

    def test_give_0_return_error(self):
        tmp = [0]
        expects = 'error'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)

    def test_give_negative_2_return_error(self):
        tmp = [-2]
        expects = 'error'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)

    def test_give_27651_return_is_not_Prime_numbers(self):
        tmp = [27651]
        expects = 'is n\'t Prime numbers'
        is_prime = is_prime_list(tmp)
        self.assertEqual(expects, is_prime)
