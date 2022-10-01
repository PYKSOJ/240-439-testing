import unittest
from src.caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_give_a_to_z_step_3(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        step = 3
        expect = 'defghijklmnopqrstuvwxyzabc'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)

    def test_give_a_to_z_step_26(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        step = 26
        expect = 'abcdefghijklmnopqrstuvwxyz'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)

    def test_give__step_negtive1_(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        step = -1
        expect = 'zabcdefghijklmnopqrstuvwxy'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)

    def test_give_pongsapuk_step_5(self):
        text = 'pongsapuk'
        step = 5
        expect = 'utslxfuzp'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)

    def test_give_sawaroj_step_negative_7(self):
        text = 'sawaroj'
        step = -7
        expect = 'ltptkhc'
        result = caesar_cipher(text, step)
        self.assertEqual(expect, result)
