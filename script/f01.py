# -*- coding: utf-8 -*-
"""
Calculates data and creates image for f01

This figure is the uncertainty ratio vs. number of terms in the partial sum approximation of the polylogarithm for a family of curves corresponding to different values of argument.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

def uncertainty_ratio(z, l):
    """
    Uncertainty ratio of polylogarithm

    Corresponds to eq:47 in the main.txt.
    """
    return np.power(z, l) - 1

# Code for saving the file
script_abspath = os.path.dirname(os.path.abspath(__file__))
script_filename = os.path.basename(os.path.abspath(__file__))
script_filename_root = os.path.splitext(script_filename)[0]
parent_repo_abspath = os.path.dirname(script_abspath)

data_filename = script_filename_root + ".dat"
data_dir_relpath = "dat"
datafile_fqpn = os.path.join(parent_repo_abspath, data_dir_relpath, data_filename)

fig_filename = script_filename_root + ".pdf"
build_dir_relpath = "build"
figfile_fqpn = os.path.join(parent_repo_abspath, build_dir_relpath, fig_filename)


# Actual generation of the figure.
l = np.linspace(1, 10000, 100)
z = 0.1

U = uncertainty_ratio(z, l)
plt.semilogx(l, U)
plt.show()
