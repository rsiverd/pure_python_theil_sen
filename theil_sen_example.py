#!/usr/bin/env python

import os, sys, time
reload = sys.modules['imp' if 'imp' in sys.modules else 'importlib'].reload

import pure_python_theil_sen
reload(pure_python_theil_sen)
ppts = pure_python_theil_sen


## -----------------------------------------------------------------------

## Example focus sequence dataset (focus, fwhm_avg, fwhm_med):
test_data = [
    (+2.0,   13.0,   13.6),
    (+1.5,   11.8,   13.2),
    (+1.0,   11.9,   11.4),
    (+0.5,   10.5,    9.5),
    (+0.0,    8.2,    8.1),
    (-0.5,    7.6,    7.3),
    (-1.0,    6.9,    6.2),
    (-1.5,    6.2,    6.2),
    (-2.0,    4.9,    4.8)]

## Make sure data are sorted by focus:
data_points = sorted(test_data)

## Run the fit:
foc_vals, fwhm_avg, fwhm_med = zip(*data_points)
icept, slope = ppts.linefit(foc_vals, fwhm_avg)

## Calculate residuals:
res_avg = [(y - icept - slope*x) for x,y,_ in data_points]
res_med = [(y - icept - slope*x) for x,_,y in data_points]

## Best-fit line for plotting:
ts_x = [min(foc_vals), max(foc_vals)]
ts_y = [(icept + slope*x) for x in ts_x]

## -----------------------------------------------------------------------
## Plot of results for illustration:
import matplotlib.pyplot as plt

plt.clf()
plt.grid()
plt.scatter(foc_vals, fwhm_avg)
plt.plot(ts_x, ts_y, c='r')
plt.savefig('theil_sen_fit.png')

