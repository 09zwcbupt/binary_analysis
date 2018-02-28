#!/usr/bin/python
# extended from https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

import re
import pdb
import sys
from hexdump import hexdump
from tempfile import mkstemp

pid = 21234
_, dump_file_name = mkstemp()
maps_file = open( "/proc/" + str( pid ) + "/maps", 'r' )
mem_file = open( "/proc/" + str( pid ) + "/mem", 'r', 0 )
dump_file = open( dump_file_name, 'w' )
print "memory dump stored %s" % dump_file_name

for line in maps_file.readlines():  # for each mapped region
    m = re.match( r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line )
    if m.group( 3 ) == 'r':  # if this is a readable region
        start = int( m.group( 1 ), 16 )
        end = int( m.group( 2 ), 16 )
        dump = line + "readable memory segment from %s to %s\n\n" % ( hex( start ), hex( end ) )
        try:
           mem_file.seek( start )  # seek to region start
           chunk = mem_file.read( end - start )  # read region contents
        except IOError:
           dump += "not able to dump this section\n\n"
        except:
           dump += "Unexpected error: " + str( sys.exc_info()[ 0 ] ) + "\n\n"
        else:
           dump += hexdump( chunk, result='return' ) + "\n\n" # dump contents
        dump_file.write( dump )
        
maps_file.close()
mem_file.close()
dump_file.close()
