import unittest
import volumes


class Test_volumes(unittest.TestCase):

    def test_get_cube_vol_basic1(self):
        self.assertEqual(volumes.get_cube_vol(3), 27)

    def test_get_cube_vol_basic2(self):
        self.assertEqual(volumes.get_cube_vol(4), 64)

