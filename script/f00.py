# -*- coding: utf-8 -*-
"""
Calculates data and creates image for f00
"""
import ibei
import datac
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

script_abspath = os.path.dirname(os.path.abspath(__file__))
script_filename = os.path.basename(os.path.abspath(__file__))
script_filename_root = os.path.splitext(script_filename)[0]
parent_repo_abspath = os.path.dirname(script_abspath)

data_filename = script_filename_root + ".dat"
data_dir_relpath = "dat"
datafile_fqpn = os.path.join(parent_repo_abspath, data_dir_relpath, data_filename)


# Set up abscissae.
params = {"temp_sun": 6000.}
bandgaps = np.linspace(0, 3.25, 100)

abscissae = datac.generate_abscissae(bandgaps, "bandgap", params)
data = datac.generate_ordinates(abscissae, ibei.SQSolarcell, "calc_efficiency")

# Write data to file.
datac.write_json(datafile_fqpn, data)
