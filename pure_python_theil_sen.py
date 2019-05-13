#!/usr/bin/env python
# vim: set fileencoding=utf-8 ts=4 sts=4 sw=4 et tw=80 :
#
#    Pure Python implementation of Theil-Sen estimator (for sequencer scripts).
#
# Rob Siverd
# Created:       2017-12-04
# Last modified: 2017-12-04
#--------------------------------------------------------------------------
#**************************************************************************
#--------------------------------------------------------------------------

## Current version:
__version__ = "0.0.1"

## Modules:
import signal
import os
import sys
import time
#import numpy as np
#import datetime as dt
#from functools import partial
#from collections import OrderedDict
#import multiprocessing as mp
#np.set_printoptions(suppress=True)
#import theil_sen as ts
import itertools as itt

##--------------------------------------------------------------------------##

def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0


def calc_slope_unweight(x_srt, y_srt):
    """
    The Theil-Sen slope estimate is obtained by taking the median of all
    possible pair-wise slopes. In other words, we compute the list of slopes
    measured from point i to point j (j > i) for all possible i,j combinations.
    We then accept the median of that list as the best estimate.
    
    NOTE: Input data should be sorted by x (so that dx > 0 for each pair).
    """
    pairs = [(i, j) for (i, j) in itt.combinations(range(len(x_srt)), 2)]
    #for i,j in pairs:
    #    dx = x_srt[j] - x_srt[i]
    #    dy = y_srt[j] - y_srt[i]
    slopes = [((y_srt[j] - y_srt[i]) / (x_srt[j] - x_srt[i])) for i,j in pairs]
    robust_slope = median(slopes)
    return robust_slope

def linefit(x_vec, y_vec):
    """
    Robust line fit to data in two lists.

    Returns (intercept, slope).
    """

    xs, ys = zip(*sorted(zip(x_vec, y_vec)))
    slope = calc_slope_unweight(xs, ys)
    icept = median([(ys - slope * xs) for xs,ys in zip(xs, ys)])
    return icept,slope

##--------------------------------------------------------------------------##




######################################################################
# CHANGELOG (pure_python_theil_sen.py):
#---------------------------------------------------------------------
#
#  2017-12-04:
#     -- Increased __version__ to 0.0.1.
#     -- First created pure_python_theil_sen.py.
#
