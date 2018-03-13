# coding: utf-8

import numpy as np
import xarray as xr
from nose.tools import ok_
from smrt.core import result


# Tests written in response to -ve intensity bug in result.py
res_example = result.Result([[[[4.01445680e-03, 3.77746658e-03, 0.00000000e+00]],
                    [[3.83889082e-03, 3.85904771e-03, 0.00000000e+00]],
                    [[2.76453599e-20, -2.73266027e-20, 0.00000000e+00]]]],
                    coords = [('theta', [35]), ('polarization', ['V','H','U']),
                    ('theta_inc', [35]), ('polarization_inc', ['V','H','U'])])

def test_positive_sigmaVV():
    ok_(res_example.sigmaVV()>0)

def test_positive_sigmaVH():
    ok_(res_example.sigmaVH()>0)

def test_positive_sigmaHV():
    ok_(res_example.sigmaHV()>0)

def test_positive_sigmaHH():
    ok_(res_example.sigmaHH()>0)