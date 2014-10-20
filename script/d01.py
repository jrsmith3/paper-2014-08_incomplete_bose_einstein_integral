# -*- coding: utf-8 -*-
"""
Maximum efficiency of single junction solar cell according to DeVos
"""
import ibei
import datac
import numpy as np
import matplotlib.pyplot as plt


# Overload the `Datac.plot` method to give me what I want
class f01(datac.Datac):
    def plot(self):
        # fig = plt.figure(figsize=(5.,4.))
        plt.plot(self.abscissae, self.ordinates)
        plt.xlabel("Voltage [V]")
        plt.ylabel("Efficiency")


params = {"temp_sun": 5762.,
          "temp_planet": 289.,
          "bandgap": 1.15,}

voltages = np.linspace(0, 0.975 * params["bandgap"], 1000)

dt = f01(params, voltages, "voltage", ibei.DeVosSolarcell.calc_efficiency)
# dt.show()
print max(dt.ordinates)
