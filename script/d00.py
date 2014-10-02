# -*- coding: utf-8 -*-
"""
Maximum efficiency of single junction solar cell according to Shockley and Queisser 
"""
import ibei
params = {"temp_sun": 6000.,
          "bandgap": 1.1,}

sc = ibei.SQSolarcell(params)
print sc.calc_efficiency()
