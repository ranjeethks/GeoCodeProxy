"""
    ProxyServer: HTTP Request Handler for Geocode-proxy-server.
"""
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from core.geocoder import Geocoder
from core.Connect import HttpConnection
import json

class ProxyServer(BaseHTTPRequestHandler):

    """Performs 'do_GET' operation for proxy server
    """
    def do_GET(self):
        
        """ perform GET call to the proxy server. """
        location_data = self.geocoding_operation()

        if location_data is None:
            self.send_json(400, {
    				'MESSAGE': 'Provide an address to geocode your request, example: "?address=2500%20University%20Dr")'
            })
        elif location_data is False:
        		self.send_json(503, {
    				'MESSAGE': 'Sorry! No geocoding services available now. Please try later.'
            })
        else:
            self.send_json(200, location_data)
    
        return

    def geocoding_operation(self):
        
        """ Method to create geoCoder instance and call service providers
        Args:
            None
        Returns:
            location_data: coordinate data, lattitude and longitude
        """
                   
        http_connection = HttpConnection()
        geocoder = Geocoder(http_connection)
        uri = urlparse(self.path)
        query = parse_qs(uri.query)
    
        if query.get('address') is None:
            return None
    
        location_data = geocoder.geocode(query['address'][0])
        return location_data

    def send_json(self, http_status_code, data):
        
        """Method to send json data to the server   
        Args:
            http_status_code: HTTP status code response from external API
            data: relevant message such as coordinates  
        """       
        response_text = json.dumps(data)
        self.send_response(http_status_code)
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))
        return