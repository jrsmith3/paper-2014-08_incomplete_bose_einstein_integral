# -*- coding: utf-8 -*-
"""
Calculates data and creates image for f00
"""
import ibei
import numpy as np
import matplotlib.pyplot as plt
import copy


def init_abscissa(params, abscissae, abscissa_name):
    """
    List of dicts to initialize object w/ calc method

    This method generates a list of dicts; each dict is sufficient to initialize an object featuring a calculator method of interest. This list can be thought of as the abscissae of a set of data. Each dict will contain data which remains constant for each calculation, but it nonetheless required to initialize the object. Each dict will also contain a datum which is the abscissa for the calculation and is also required to initialize the object.

    :param dict params: Static parameters required to initialize the object featuring the ordinate calculator method.
    :param list abscissae: Independent variable also required to initialize object featuring the ordinate calculator method.
    :param str abscissa_name: Dictionary key for the abscissa name.
    """
    dict_list = []

    for abscissa in abscissae:
        param_dict = copy.copy(params)
        param_dict[abscissa_name] = abscissa
        dict_list.append(param_dict)

    return dict_list


# Set up ordinates.
temp_sun = 6000.
bandgaps = np.linspace(0, 3.25, 100)

# Initialize empty list for abscissae.
efficiencies = []

for bandgap in bandgaps:
    input_params = {"temp_sun": temp_sun, "bandgap": bandgap}
    sc = ibei.SQSolarcell(input_params)
    efficiency = sc.calc_efficiency()
    efficiencies.append(efficiency)
