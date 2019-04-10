import unittest
import foo_lib

class Test_foo_lib(unittest.TestCase):

    def test_foo1_general1(self):
        self.assertEqual(2, foo_lib.foo1(4))

    def test_foo1_general2(self):
        self.assertEqual(3, foo_lib.foo1(9))

    def test_foo1_unusual_type_basic(self):
        self.assertRaises(TypeError, foo_lib, "hello")

    def test_foo1_unusual_type_specific_msg(self):
        """
        test for incorrect type and specific error message
        :return:
        """
        with self.assertRaises(TypeError) as err:
            foo_lib.foo1("hello")

        self.assertEqual("Cannot square root a non-number.", str(err.exception))

    def test_foo1_unusual_negative_basic(self):
        self.assertRaises(ValueError, foo_lib.foo1, -2)


    def test_fooList1_general(self):
        self.assertEqual(6, foo_lib.fooList([1,2,3]))

    def test_fooList1_corner_singleValue(self):
        self.assertEqual(5, foo_lib.fooList([5]))

    def test_fooList1_unusual_emptyList(self):
        self.assertRaises(ValueError, foo_lib.fooList, [])

    def test_fooList1_unusual_emptyList_specific_msg(self):
        with self.assertRaises(ValueError) as err:
            foo_lib.fooList([])

        self.assertEqual("Cannot process empty list", str(err.exception))

    def test_fooList1_unusual_stringvalue(self):
        self.assertRaises(TypeError, foo_lib.fooList, ["5", "6"])

    def test_fooList1_unusual_stringvalue_specific_msg(self):
        with self.assertRaises(TypeError) as err:
            foo_lib.fooList(["5", "6"])

        self.assertEqual("Cannot total non-numbers.", str(err.exception) )









