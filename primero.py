                                                                             #lineplot.py                                                                                                               
import numpy as np
import pylab as pl
# Make an array of x values                                                                                                 
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pl.xlabel('edad')
# Make an array of y values                                                                                                 
y = [1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997]
pl.ylabel('anio')
# use pylab to plot x and y                                                                                                 
pl.title('Hugo')
pl.plot(x,y, 'ro')
# show the plot on the screen                                                                                               
pl.savefig('temp1.png')
