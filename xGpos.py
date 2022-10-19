# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from math import isclose

def xnum1(pos1,tri):
    areaT = abs((((tri[1,0]-tri[0,0])*(tri[2,1]-tri[0,1]))-((tri[2,0]-tri[0,0])*(tri[1,1]-tri[0,1])))/2)
    areaP = list()
    for i in [[0,1],[0,2],[1,2]]:
        t = np.concatenate((tri[i,:],pos1))
        tA = abs((((t[1,0]-t[0,0])*(t[2,1]-t[0,1]))-((t[2,0]-t[0,0])*(t[1,1]-t[0,1])))/2)
        areaP.append(tA)
   # print(areaT)
    #print(sum(areaP))
    return(isclose(areaT,sum(areaP),abs_tol=0.00001))

