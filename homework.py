"""C4RM Class 05: NumPy homework.

All four assignment functions use no loops.
Rates are annual decimals, maturity is in years, and ppy is payments/year.
"""

import numpy as np


def WhoAmI():
    """Return the identifier already supplied in the assignment workbook."""
    return 'zn2106'


def getBondPrice(y, face, couponRate, m, ppy=1):
    """Present value of coupons and principal, with periodic compounding.

    Assumes valuation on a coupon date and a positive integer m * ppy.
    """
    periods = np.arange(1, int(round(m * ppy)) + 1)
    cashflows = np.full(periods.size, face * couponRate / ppy, dtype=float)
    cashflows[-1] += face
    discount_factors = (1 + y / ppy) ** (-periods.astype(float))
    return float(np.sum(cashflows * discount_factors))


def getBondDuration(y, face, couponRate, m, ppy=1):
    """Return Macaulay duration in years (not modified duration)."""
    periods = np.arange(1, int(round(m * ppy)) + 1)
    cashflows = np.full(periods.size, face * couponRate / ppy, dtype=float)
    cashflows[-1] += face
    present_values = cashflows * (1 + y / ppy) ** (-periods.astype(float))
    times = periods / ppy
    return float(np.sum(times * present_values) / np.sum(present_values))


def FizzBuzz(start, finish):
    """Return an object array for integers in [start, finish).

    Multiples of 3 become 'fizz', of 5 'buzz', and of both 'fizzbuzz'.
    Other elements remain integers. An empty interval returns an empty array.
    """
    numbers = np.arange(start, finish)
    result = np.array(numbers, dtype=object)
    result[numbers % 3 == 0] = 'fizz'
    result[numbers % 5 == 0] = 'buzz'
    result[numbers % 15 == 0] = 'fizzbuzz'
    return result

