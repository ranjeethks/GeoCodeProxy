from core.config import Config
from core.geocoder.request_here import RequestHere
from core.geocoder.request_geonames import RequestGeonames
from core.geocoder.request_google import RequestGoogle


class Geocoder:
    def __init__(self, http_connection):
        self.config = Config()
        self.http_connection = http_connection

    def geocode(self, address):
        """ get location data from external service for a given address.   
        Args:
        address: address string  
        Returns:
        location_data: coordinate data, lattitude and longitude   
        """ 
        request_here = RequestHere(self.config, address, self.http_connection)
        request_geonames = RequestGeonames(self.config, address, self.http_connection)
        request_google = RequestGoogle(self.config, address, self.http_connection)
        
        
        # HERE - primary provider
        location_data = request_here.geocode()
        
        # geonames - secondary provider
        if location_data == False:
            location_data = request_geonames.geocode()
        
        # Google - tertiary provider
        if location_data == False:
        		location_data = request_google.geocode() 

        return location_data


