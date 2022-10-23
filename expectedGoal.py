# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
#Statistical fitting of models
import statsmodels.api as sm
import statsmodels.formula.api as smf

def xG(a,d):
    #these numbers were gotten through tyhe xGmodel jupyter notebook EDA
    B0 = 0.890883
    Bangle = -1.313904
    Bdistance = 0.113712
    bsum = B0 + (Bangle*a) + (Bdistance*d)
    xG = 1 / (1 + np.exp(bsum))
    return xG