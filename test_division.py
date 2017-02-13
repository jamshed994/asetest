#!/usr/bin/env python
from __future__ import division

#############################################
# File name: test_division.py               #
# Author: Vidya Venkiteswaran               #
# Email: vv2269@columbia.edu                #
# Date created: 01/25/2017                  #
# Usage: python test_division.py            #
# Python Version: 3.5.2                     #
# Instructor: Prof. Ewan Lowe               #
#############################################

import numpy as np


def integer_division(a, b):
    """Divide a by b

    Divide a by b of same data type

    Parameters
    ----------
    a : any-type
      divisor
    b : any-type
      dividend

    Returns
    -------
    res
        quotient
    """

    return None if b == 0 else a/b


def test_division():
    """Result of 2/8

    Check result of 2 divided by 8

    Parameters
    ----------
    

    Returns
    -------
    bool
        True or False
    """

    assert integer_division(2, 8) == 0.25

    numpy_a = np.array([2])
    numpy_b = np.array([8])

    assert integer_division(numpy_a, numpy_b) == 0.25
