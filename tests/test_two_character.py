import unittest
from src.two_character import two_characters

class test_two_character(unittest.TestCase):
    def test_give_haveaniceday_return_5(self):
        text = 'haveaniceday'
        expect = 5
        result = two_characters(text)
        self.assertEqual(result, expect)
        
    def test_give_nonestr(self):
        text = ''
        expect = 0
        result = two_characters(text)
        self.assertEqual(result, expect)
    
    def test_give_abc(self):
        text = 'abc'
        expect = 2
        result = two_characters(text)
        self.assertEqual(result, expect)
    