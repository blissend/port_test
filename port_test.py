#!/usr/bin/python
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Quickly test if a connection can be made to requested address:port via sockets
NOTE: Works on python 2.3 and above, preferably 2.6 and upward
USAGE: python port_test.py 27017 mngcl15l-prf-08 8.8.8.8
"""

__author__ = ('Adam Carlin')
__version__ = '2015.04.27'
__usage__ = 'python port_test.py <port> <address1> <address2> ...'

import sys
import socket

if __name__ == '__main__':
    # Parse args
    verbose = False
    for _ in xrange(2):
        if sys.argv[1] == '-v':
            verbose = True
            del sys.argv[1]
        elif sys.argv[1] == '-V':
            print(__version__)
            del sys.argv[1]
    try:
        port = int(sys.argv[1])
    except ValueError:
        print('Bad Value: First argument must be an integer!')
        print(__usage__)
        sys.exit()
    hosts = sys.argv[2:]

    # Test each host:port for connectivity
    for host in hosts:
        if verbose == True:
            print("Trying " + str(host) + " on port " + str(port))
        try:
            # Check if python version is 2.6 in order to use easy method
            ver = float(sys.version[:3])
            if ver >= 2.6:
                conn = socket.create_connection((host,port),timeout=1)
            else:
                conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn.settimeout(1)
                conn.connect((host,int(port)))
        except socket.timeout:
            print("EXCEPTION: Trouble connecting to " + str(host))
        except socket.gaierror:
            print("EXCEPTION: Trouble connecting to " + str(host))
        else:
            if verbose == True:
                print("SUCCESS for " + str(host))
            else:
                print("SUCCESS")