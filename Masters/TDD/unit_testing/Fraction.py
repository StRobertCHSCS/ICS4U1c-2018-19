"""
-------------------------------------------------------------------------------
Name:		Fraction.py
Purpose:
Creates fractions and performs operations on them

Author:		Fabroa.E

Created:		23/03/2019
------------------------------------------------------------------------------
"""

class Fraction(object):
    """
    Models a fraction object
    """

    def __init__(self, numerator, denominator):
        """
        Initializes the numerator and denominator from user input. Raises a ValueError if the denominator is zero.

        :param numerator: int The numerator of the fraction
        :param denominator: int The denominator of the fraction
        :return: None
        """

        if denominator == 0:
            raise ValueError()

        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        """
        Retrieves the current numerator of an instance of a fraction
        :return: int The current value of the numerator attribute
        """
        return self.numerator

    def get_denominator(self):
        """
        Retrieves the current denominator of an instance of a fraction
        :return: int The current value of the denominator attribute
        """
        return self.denominator

    def set_numerator(self, new_numerator):
        """
        Sets the current numerator to a new numerator based on a user's input
        :param new_numerator: int The new desired numerator of the fraction from the user
        :return: None
        """
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):
        """
        Sets the current denominator to a new numerator. Raises a ValueError if the new denominator is zero
        :param new_denominator: int The new desired denominator of the fraction from the user
        :return: None
        """

        if new_denominator == 0:
            raise ValueError()

        self.denominator = new_denominator

    def __str__(self):
        """
        Returns a reduced fraction as a string
        :return: string The reduced fraction from the current numerator and denominator
        """

        self.__reduce()
        return str(int(self.numerator)) + "/" + str(int(self.denominator))

    def add(self, otherFraction):
        """
        Adds another Fraction object to the current Fraction object
        :param otherFraction: object The other Fraction object
        :return: None
        """

        # Adds numerators together if both fractions have the same denominator
        if self.denominator == otherFraction.denominator:
            self.numerator += otherFraction.numerator
        # Cross multiplies to create a common factor for both then adds
        else:
            self.numerator *= otherFraction.denominator
            otherFraction.numerator *= self.denominator
            self.denominator *= otherFraction.denominator
            self.numerator += otherFraction.numerator

    def subtract(self, otherFraction):
        """
        Subtracts another Fraction object from the current Fraction object
        :param otherFraction: object The other Fraction object
        :return: None
        """

        # Subtracts numerators together if both fractions have the same denominator
        if self.denominator == otherFraction.denominator:
            self.numerator -= otherFraction.numerator
        # Cross multiplies to create a common factor for both then subtracts
        else:
            self.numerator *= otherFraction.denominator
            otherFraction.numerator *= self.denominator
            self.denominator *= otherFraction.denominator
            self.numerator -= otherFraction.numerator

    def multiply(self, otherFraction):
        """
        Multiplies the current Fraction object by another Fraction object
        :param otherFraction: object The other Fraction object
        :return: None
        """

        self.numerator = self.numerator * otherFraction.numerator
        self.denominator = self.denominator * otherFraction.denominator

    def __reduce(self):
        """
        Reduces fraction to lowest terms
        return: None
        """

        a = self.numerator
        b = self.denominator

        # Checks to see which out of the numerator and denominator is lower and finds to biggest common factor to divide
        if abs(a) <= b:
            while a > 1:
                if self.numerator % a == 0 and self.denominator % a == 0:
                    self.numerator /= a
                    self.denominator /= a
                    break
                else:
                    a -= 1
        else:
            while b > 1:
                if self.numerator % b == 0 and self.denominator % b == 0:
                    self.numerator /= b
                    self.denominator /= b
                    break
                else:
                    b -= 1


