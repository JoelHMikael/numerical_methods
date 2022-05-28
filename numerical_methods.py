
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

# Finds a zero of f with Newton's method.
# https://en.wikipedia.org/wiki/Newton%27s_method
# It is good to note that this may result in an
# error if the iteration happens to reach a
# place where the functions derivative is zero.
# The newtons method may also end up in an
# infinite loop, so specifying max_iterations
# might be wise.
# 
# f: the function whose zero to find
# startx: start value of iteration
# [df]: derivative of f. Defaults to using
# difference_quotient (specified in this file)
# for approximating the derivative.
# [accuracy]: accurate number of decimals to
# get. Defaults to infinity, which leads to the
# most accurate result pythons data types allows
# [max_iterations]: maximum number of iterations
# to do before returning None. Defaults to
# infinity which means the function might end up
# in an infinite loop.
def newtons_method(
        f: callable,
        startx: float,
        df: callable = None,
        accuracy: float = float('inf'),
        max_iterations=float('inf')
    ) -> float:
    if df == None:
        df = lambda x: difference_quotient(f, x)

    x = startx

    # To measure the accuracy
    lastx = None

    iteration = 0

    while True:
        iteration += 1

        # Get the next value of x. The whole
        # core of Newton's method is this single
        # line...
        x -= f(x) / df(x)

        # break out if x is accurate enough
        if accuracy == float('inf'):
            if x == lastx:
                break
        elif lastx != None and (
                round(x, accuracy) ==
                round(lastx, accuracy)
            ):
            break
        
        # Exit if stuck in apparently endless
        # loop based on number of iterations.
        if iteration >= max_iterations:
            return None

        lastx = x

    # final rounding before return
    if accuracy != float('inf'):
        x = round(x, accuracy)

    return x

# Gets the difference quotient (an approximation
# of its derivative) of f using central
# difference ( two points at (x + d, f(x + d))
# and (x - d, f(x - d)) ).
# 
# f: function whose difference quotient to
# calculate
# x: the position at which to calculate the
# difference quotient
# [d]: the distance (along the x-axis) of the
# points to use in the calculation. Defaults to
# one tenth.
def difference_quotient(
        f: callable,
        x: float,
        d: float = .1
    ) -> float:
    return (f(x + d) - f(x - d)) / (2 * d)
    
class TestZeroFinders(unittest.TestCase):
    # A bit untraditional way to use the setup
    # function. I wanted anyways to be able to
    # use the same function across multiple
    # tests without it being global scope, and
    # I couldn't come up with anything better.
    def setUp(self):
        from math import sin

        # it just works (TM)
        self.f = lambda x: .5*sin(2*x) - x + 2

        self.accuracy = 3

        self.result = 1.789

    def test_bisection_method(self):
        actual_result = bisection_method(
            self.f,
            0,
            3,
            self.accuracy
        )

        self.assertEqual(
            actual_result,
            self.result
        )

        with self.assertRaises(ValueError):
            bisection_method(self.f, 3.0, 3.5)

    def test_newtons_method(self):
        # Test if it can find the zero of f
        zero_of_f = newtons_method(
            self.f,
            1,
            accuracy=self.accuracy
        )

        self.assertEqual(
            zero_of_f,
            self.result
        )

        # Test the max iterations mechanism
        def infinite_loop_derivative(x):
            if x < self.result:
                return .001
            else:
                return -.001

        infinite_loop_result = newtons_method(
            self.f,
            1,
            infinite_loop_derivative,
            max_iterations = 100
        )

        self.assertEqual(
            infinite_loop_result,
            None
        )
        

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

