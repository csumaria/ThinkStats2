#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:52:36 2017

@author: chintan
"""
import thinkstats2
import random
import thinkplot

rndm = [int(random.random()*1000) for x in range(0,1000)]
print(rndm)

pmf = thinkstats2.Pmf(rndm, label='PMF of Random Numbers')
cdf=thinkstats2.Cdf(rndm, label='CDF of Random Numbers')

thinkplot.Pmf(pmf)
thinkplot.show(xlabel='Number',ylabel='pmf',axis=[0,1000,0,0.5])
thinkplot.Cdf(cdf)
thinkplot.show(xlabel='Number',ylabel='cdf')
