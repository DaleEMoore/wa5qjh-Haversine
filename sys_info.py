#1/usr/local/bin/python3
import sys
print (" \n\t =======")

print ( sys.version_info[ 0 ] )


if sys.version_info[0] ==3 :
    print (" 3  sys info  %s %s %s  " % sys.version_info[0:3] )
else:
    print ( " 2  sysinfo  %s  " % sys.version_info)
 
 