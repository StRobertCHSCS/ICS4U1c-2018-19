import unittest
import Fraction


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.fraction1 = Fraction.Fraction(3, 4)

        # 1. create a fraction2 object with numerator 2 and denominator 3

        # 2. create a fraction3 object with numerator 1 and denominator 4

    def test_instance_creation(self):
        self.assertIsInstance(self.fraction1, Fraction.Fraction)

    def test_instance_creation_0Denom(self):
        self.assertRaises(ValueError, Fraction.Fraction, 1,0)

    def test_get_numerator(self):
        self.assertEquals(self.fraction1.get_numerator(), 3)

    def test_get_denominator(self):
        # 3. create a test to check the denominator of the self.fraction1 object
        pass

    def test_set_denominatorBasic(self):
        self.fraction1.set_denominator(8)
        self.assertEquals(self.fraction1.__str__(), "3/8")

    def test_set_denominator0(self):
        # 4. test that setting the denominator of self.fraction1 raises a ValueError
        pass

    def test_str(self):
        self.assertEquals(self.fraction1.__str__(), "3/4")

    def test_add(self):
        self.fraction1.add(self.fraction2)
        self.assertEquals(self.fraction1.__str__(), "17/12")

    def test_add_reduce(self):
        self.fraction3.add(self.fraction3)
        self.assertEquals(self.fraction3.__str__(), "1/2")

    def test_subtract(self):
        # 5. test self.fraction1 - self.fraction2
        pass

    def test_subtract_reduce(self):
        self.fraction1.subtract(self.fraction3)
        self.assertEquals(self.fraction1.__str__(), "1/2")

    def test_multiply(self):
        # 6. test the multiply method, checking fraction1 * fraction2
        pass


if __name__ == '__main__':
    unittest.main()


