# -*- coding: utf-8 -*-
"""
Maximum efficiency of single junction solar cell according to DeVos
"""
import ibei
params = {"temp_sun": 5762.,
          "temp_planet": 289.,
          "bandgap": 1.15,}

sc = ibei.DeVosSolarcell(params)
print sc.calc_efficiency()
