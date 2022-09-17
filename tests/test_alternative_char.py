import unittest
from src.alternative_char import alternating_char

class TestAlternatingCharacters(unittest.TestCase):
  def test_give_AABAAB(self):
    text = 'AABAAB'
    expect = 2
    result = alternating_char(text)
    self.assertEqual(expect, result)
    
  def test_give_EEEEE(self):
    text = 'EEEEE'
    expect = 4
    result = alternating_char(text)
    self.assertEqual(expect, result)
  
  def test_give_BABABA_return_0(self):
      text = 'BABABA'
      expect = 0
      result = alternating_char(text)
      self.assertEqual(expect, result)
  
  def test_give_AAABBB_return_4(self):
      text = 'AAABBB'
      expect = 4
      result = alternating_char(text)
      self.assertEqual(expect, result)