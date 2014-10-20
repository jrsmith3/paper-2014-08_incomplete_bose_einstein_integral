# -*- coding: utf-8 -*-
"""
Maximum efficiency of single junction solar cell according to DeVos
"""
import ibei
import datac
import numpy as np
import matplotlib.pyplot as plt


params = {"temp_sun": 5762.,
          "temp_planet": 289.,
          "bandgap": 1.15,}

voltages = np.linspace(0, 0.975 * params["bandgap"], 1000)

dt = datac.Datac(params, voltages, "voltage", ibei.DeVosSolarcell.calc_efficiency)
print max(dt.ordinates)
