#!/usr/local/bin/python3
import math
import sys

print (math)
print (sys)

"""
sqare root function
 y = (x + a/x)/2
 useage sqrt(integer) integer is non-negative
 returns float

"""

def sqrt( a ) :
    if a <1:
        print ("sorry, we dont do negative number or zero")
        print ("useage sqrt( non-negative-integer ) "   )

    y=1.0			# force floating point
    x=a
    while x != y :
        x=y        
        y = ( x + a/x ) / 2
    return y

def test_sqrt(tri) :
    print ( "\n\t Testing my sqrt vs math.sqrt")
    print (sys.version_info)
    if sys.version_info[0] == 3:
        print ("\t\t p3 My sqrt of %d is %.5f " % (tri, sqrt(tri)))
        print ("\t\t math.sqrt \t %.5f" % math.sqrt(tri))
    else:
        print ("\t\t p2 My sqrt of %d is  %.5f " % (tri, sqrt(tri)))
        print ("\t\t math.sqrt \t %.5f" % math.sqrt(tri))

#    ----------

test_sqrt(555)

