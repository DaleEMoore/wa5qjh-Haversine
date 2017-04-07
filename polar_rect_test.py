import sys
import math
print ('π: %.30f' % math.pi)
print ('e: %.30f' % math.e)
import matht
print ('π: %.30f' % matht.pi)
print ('e: %.30f' % matht.e)
import polar_rect
print ("""
This module is test base for my polar_rect module
math.py is imported and degrees(x), radians(x)
hypot( x,y ), atan2( y/x ), sqrt( x ), sin(x), cos(x) 
are used. 
useage:
pol_rect( radius, deg )   #rather than radians output is Real
returns x & y
rect_pol ( x,y )   # output is x and deg rather than radians

Auth: Gary B. Corell
""")

print()
print ("Test Code....degrees and radians........")

formatPol = "Polar:   radius = %f  angle %f degrees" 
print (formatPol % (polar_rect.rect_pol( 3,4) ))
#print (formatPol % (rect_pol( 3,4) ))
formatRect ="Rectangular:   x= %f    y= %f "
print (formatRect % (polar_rect.pol_rect(5.0,53.13) ))

formatter = "  %f      %f "
formatter2 = " %d   %g   %f  "
#print  formatter % ToRadians(53.1301), ToDegrees(0.928)
print  ()
print  (formatter2 %  ( 4.0/3.0,  polar_rect.ToDegrees(math.atan2( 4.0, 3.0)) ,
                        polar_rect.ToDegrees(math.atan(1.33333333))  ))

    