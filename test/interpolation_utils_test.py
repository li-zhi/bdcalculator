import unittest

from interpolation_utils import InterpolationUtils

__copyright__ = "Copyright 2022, Zhi Li"
__license__ = "MIT"


class InterpolationUtilsTest(unittest.TestCase):

    def test_pchipend(self):
        self.assertAlmostEqual(
            InterpolationUtils.pchipend(
                h1=2.9558999999999997,
                h2=3.148299999999999,
                delta1=0.08599253956237607,
                delta2=0.08164606680773055),
            0.088097277089891, places=8)
