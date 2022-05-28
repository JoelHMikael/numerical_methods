
import unittest
from typing import Callable

# Finds a zero of f between x1 and x2 with the
# bisection method. x1 must be on the opposite
# side of the x-axis compared to x2. The bisec-
# tion method can be thought of as a special
# case of the binary search algorithm.
# Further reading:
# https://en.wikipedia.org/wiki/Bisection_method
# 
# f: the function whose zero to find
# x1: start of the range. It's mark must be
# opposite to x2's.
# x2: end of the range. It's mark must be
# opposite to x1's.
# [accuracy]: accurate number of decimals to
# get. Defaults to infinity, which leads to the
# most accurate result
# pythons data types allows.
def bisection_method(
    f: Callable,
    x1: float,
    x2: float,
    accuracy: int = float('inf')
) -> float:
    a = x1

    b = x2

    if x1 * x2 > 0:
        raise ValueError(
            "x1 and x2 must be on opposite " +
            "sides of the x-axis"
            )

    middle = None

    # To monitor the accuracy.
    previous_middle = None

    while True:
        middle = (a + b) / 2

        if f(a) * f(middle) < 0:
            # There is a zero between
            # a and middle
            b = middle
        else:
            # There is a zero between
            # b and middle
            a = middle

        # Stop iterating when accurate enough
        if accuracy == float('inf'):
            if middle == previous_middle:
                break
        elif previous_middle != None and (
            round(middle, accuracy) ==
            round(previous_middle, accuracy)
        ):
            break

        previous_middle = middle

    # Final rounding before return
    if not accuracy == float('inf'):
        middle = round(middle, accuracy)

    return middle

class TestZeroFinders(unittest.TestCase):
    def test_bisection_method(self):
        from math import sin
        f = lambda x: .5 * sin(2 * x) - x + 2
        self.assertEqual(
            bisection_method(f, 0, 3, 3),
            1.789
        )
        with self.assertRaises(ValueError):
            bisection_method(f, 3.0, 3.5)

if __name__ == '__main__':
    unittest.main()

