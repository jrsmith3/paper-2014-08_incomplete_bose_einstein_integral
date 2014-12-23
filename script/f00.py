# -*- coding: utf-8 -*-
# The MIT License (MIT)

# Copyright (c) 2014 Joshua Ryan Smith (joshua.r.smith@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Calculates data and creates image for f00

This figure is a recreation of Shockley and Queisser's \ref{10.1063/1.1736034} Fig. 3; the efficiency vs. bandgap of a single junction solar cell.
"""
import ibei
import datac
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

# Overload the `Datac.plot` method to give me what I want
class f00(datac.Datac):
    def plot(self):
        fig = plt.figure(figsize=(5.,4.))
        plt.plot(self.abscissae, self.ordinates)
        plt.xlabel("Bandgap [eV]")
        plt.ylabel("Efficiency")


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


# Set up abscissae.
params = {"temp_sun": 6000.}
bandgaps = np.linspace(0, 3.25, 100)

dt = f00(params, bandgaps, "bandgap", ibei.SQSolarcell.calc_efficiency)
dt.savefig(figfile_fqpn, bbox_inches=0)
# dt.show()

# Write data to file.
# datac.write_json(datafile_fqpn, data)
