# -*- coding: utf-8 -*-
"""
Determine the maximum number of terms that will need to be summed to calculate the polylogarithm function.
"""
import numpy as np

U = 1e-5
z = 0.99999

print np.log10(U) / np.log10(z)
