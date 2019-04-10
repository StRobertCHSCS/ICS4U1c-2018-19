import math


def foo1(num):
    try:
        return math.sqrt(num)
    except ValueError:
        raise ValueError("Cannot square root a negative number.")
    except TypeError:
        raise TypeError("Cannot square root a non-number.")


def fooList(numList):
    """
    Compute the sum of the values in the list
    :param numList:
    :return:
    """
    # check if the list is empty
    try:
        if len(numList) == 0:
            raise ValueError("Cannot process empty list")
        return sum(numList)
    except TypeError:
        raise TypeError("Cannot total non-numbers.")


