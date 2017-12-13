from core.geocoder.request import Request

class RequestGoogle(Request):
    #HOST and PATH ID for GOOGLE service
	HOST = 'https://maps.googleapis.com'
	PATH = '/maps/api/geocode/json'

	def params(self):
		return {
			"address": self.address
		}

	def extract_coordinates_from_response(self, response):
		data = response.json()
		return data['results'][0]['geometry']['location']
