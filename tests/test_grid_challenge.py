import unittest
from src.grid_challenge import grid_challenge


class TestGridChallength(unittest.TestCase):

    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_return_yes(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expect = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, expect)
    
    def test_give_ebacd_zzzzz_olmkn_trpqs_xywuv_return_no(self):
        grid = ['ebacd', 'zzzzz', 'olmkn', 'trpqs', 'xywuv']
        expect = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, expect)