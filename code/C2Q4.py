#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:12:03 2017

@author: chintan
"""

from __future__ import print_function, division
#%matplotlib inline
import numpy as np
import nsfg
import first

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

print('The Cohen\'s for weight (in lbs) for first babies and others is:')
print(CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
print('The Cohen\'s for pregnancy length for first babies and others is:')
print(CohenEffectSize(firsts.prglngth,others.prglngth))