
import unittest

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
# most accurate result pythons data types allows
def bisection_method(
        f: callable,
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

# Gets the difference quotient (an approximation
# of its derivative) of f using two points at
# (x + d, f(x + d)) and (x - d, f(x - d)).
# 
# f: function whose difference quotient to
# calculate
# x: the position at which to calculate the
# difference quotient
# d: the distance (along the x-axis) of the
# points to use in the calculation.
def difference_quotient(
        f: callable,
        x: float,
        d: float
    ) -> float:
    return (f(x + d) - f(x - d)) / (2 * d)
    

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

class TestDifferenceQuotient(unittest.TestCase):
    def test_difference_quotient(self):
        f = lambda x: x ** x
        x = .5
        d = .1

        res = difference_quotient(f, x, d)
        res = round(res, 3)
        
        self.assertEqual(res, 0.214)

if __name__ == '__main__':
    unittest.main()

