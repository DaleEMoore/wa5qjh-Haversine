#!/usr/local/bin/python2
import math
import sys

print (math)
print (sys)
print (sys.version_info)
"""
sqare root function
 y = (x + a/x)/2

"""

def sqrt( a ) :
    y=1.0			# force floating point
    x=a
    while x != y :
        x=y        
        y = ( x + a/x ) / 2
    return y

#    ----------    
print ( "\n\t Testing my sqrt vs math.sqrt \n")
tri=556

if sys.version_info[ 0] ==  3 :
    print ("\t\t p3 My sqrt of %d is \t %.5f " %  (tri, sqrt( tri ) ) )
    print ("\t\t math.sqrt \t\t\t\t %.5f" % math.sqrt( tri ) )
else:
    print ("\t\t p2 My sqrt of %d is  %.5f " %  ( tri, sqrt( tri ) ) )
    print ("\t\t math.sqrt \t %.5f" %  math.sqrt( tri ) )


