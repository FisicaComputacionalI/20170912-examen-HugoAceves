                                                                             #lineplot.py                                                                                                               
import numpy as np
import pylab as pl
# Make an array of x values                                                                                                 
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pl.xlabel('edad')
# Make an array of y values
#tus valores deber'ian de haber incrementado 1997, 1998, 1999, etc.                                                                                                  
#y = [1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997]
y = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016] 
pl.ylabel('anio')
# use pylab to plot x and y                                                                                                 
pl.title('Hugo')
pl.plot(x,y, 'ro')
# show the plot on the screen                                                                                               
pl.savefig('temp1.png')
