"""  #!/usr/local/bin/python3     """
import sys
import math
'''
This module performs polar to rectangular
and rectangular to polar notation
math.py is imported and degrees(x), radians(x)
hypot( x,y ), atan2( y/x ), sqrt( x ), sin(x), cos(x) 
are used. 
useage:
pol_rect( radius, deg )   #rather than radians output is Real
returns x & y
rect_pol ( x,y )   # output is x and deg rather than radians

Auth: Gary B. Corell   '''

def ToDegrees( radians ):
 	return radians/0.017453292519943295   

def ToRadians( degrees ):
 	return degrees * 0.017453292519943295   

def pol_rect( radius, deg ):
    angle = ToRadians( deg )
    x = radius* math.cos( ToRadians( angle ) )
    y = radius*math.sin(( ToRadians( angle )))
    return x,y

def rect_pol( x, y ):
    radius = math.hypot( x , y )
    angle = ToDegrees(math.atan2( y , x ) )
    return radius, angle

#================   Test Code Section   ====================
print ("\n \n Test Code....degrees and radians........")
print "math lib imported: %s \n" % math
formatPol = "  To Polar:   radius: %.4f  angle: %.3f degrees" 
formatRect ="  To Rectangular:   x= %.4f    y= %.4f "
x = 3
y = 4
rad = .50000
deg = 53.130100
print (" \n \n")

#print ( "radians %.3f degrees %f" %  rad deg )
#print  ( "degrees %.3f radians %.3f " % deg ToRadians( deg ) )
## Print with Format statements print Format % ( parm , parm)
print " %.3f radians  %.3f degrees\n"  % ( rad , deg )
print  " radius: %.3f   %.3f degrees \n" % (ToDegrees( rad )  , ToRadians( deg )  )
print "\t End 1st test of math functions \n"
print ("Test math. trig functions")
print "Math.cos %.3f" % ( math.cos(9.564738) )
print "Math.sin %.3f" % ( math.sin( 9.918273) )
print "Math.atan %.3f" % ( math.atan(9.9999))
print "Math.atan2  %.3f" % ( math.atan2( 3.0 , 4) )
print "Math.sqrt  %.3f \n" % ( math.sqrt(100) )
print "Polar to rect  %.4f x  %.4f y " % ( pol_rect(  rad,deg) )

print ("____  end of trig function tests ____________ \n \n")

print ( "\tPolar to rectangular")
print formatRect % (( pol_rect(  rad , deg ) ) )
print ("----------" )
print ("\tRectangular to polar")
print formatPol % ((rect_pol( x , y ) )  )


print ("__________________")
formatter = "  %f      %f "
formatter2 = " %f   %g   %f  "
#print  formatter % ToRadians(53.1301), ToDegrees(0.928)
print  ()
#print  formatter2 % ( 4.0/3.0,  ToDegrees(math.atan2( 4.0, 3.0)) ,   ToDegrees(math.atan(1.33333333))  )
print ("......... EOT \n \n")
