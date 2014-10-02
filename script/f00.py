# -*- coding: utf-8 -*-
"""
Calculates data and creates image for f00
"""
import ibei
import datac
import numpy as np
import matplotlib.pyplot as plt
import copy


# Set up abscissae.
params = {"temp_sun": 6000.}
bandgaps = np.linspace(0, 3.25, 100)

abscissae = datac.generate_abscissae(bandgaps, "bandgap", params)
data = datac.generate_ordinates(abscissae, ibei.SQSolarcell, "calc_efficiency")
