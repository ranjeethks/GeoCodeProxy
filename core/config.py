import json

class Config:
	def __init__(self):
     #Read json file
		secrets_file = open('./secrets.json')
		self.data = json.loads(secrets_file.read())
		secrets_file.close()