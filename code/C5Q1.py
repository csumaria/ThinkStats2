#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:20:12 2017

@author: chintan
"""

import thinkstats2
import scipy.stats

mu = 178
sigma = 7.7
normal_height_dist = scipy.stats.norm(loc=mu, scale=sigma)
cdf_height1 = normal_height_dist.cdf(177.8) 
cdf_height2 = normal_height_dist.cdf(185.4) 
print('The fraction of US male population in the low-high height range is:')
print(100*(cdf_height2-cdf_height1))