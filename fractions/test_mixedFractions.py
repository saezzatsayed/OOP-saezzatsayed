import unittest
import mixedFractions
import classes

class test_mixFrac(unittest.TestCase):

    def test_div(self):
        div_frac = classes.fraction()
        div_frac.set_x(27)
        div_frac.set_y(12)
        self.assertEqual(div_frac.get_x()/div_frac.get_y(), 27/12)

    def test_mixFrac(self):
        mix_frac = classes.reminder()
        mix_frac.set_whole(int(27/12))
        mix_frac.set_rem(27 % 12)
        result = f'{mix_frac.get_whole()} {mix_frac.get_rem()} / 12'
        self.assertEqual(result,'2 3 / 12')