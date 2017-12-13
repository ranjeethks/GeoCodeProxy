#!/usr/bin/env python3


"""
    #########################################
    GeoCode Proxy Server - script starts here
    #########################################

"""

import os, sys
from http.server import HTTPServer


package_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(package_directory, 'core'))

from server import ProxyServer
from argparse import ArgumentParser


if __name__ == "__main__":
    
    #Main function begins
    #default server is - localhost
    #Default port is 8800  - ask the user to enter the port number of their choice as: --port ####
    parser = ArgumentParser(description="GeoCoding Proxy Server")
    message = 'Server Port (default=8800)'
    parser.add_argument("-p", "--port", default=8800, type=int, help=message)
    arg = parser.parse_args()

    try:
        httpd = HTTPServer(('0.0.0.0', arg.port), ProxyServer)
        print("Server is running at http://localhost:"+str(arg.port))  
        print("Go to your favorite browser and type http://localhost:"+str(arg.port)+"/?address=*YOUR ADDRESS*") 
        print("\nReturns {'lat':, 'long':} values..") 
        print("\nPress Ctrl+C to exit..")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n User Interruption, Exiting!")
        sys.exit()
