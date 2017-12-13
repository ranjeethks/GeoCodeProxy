# Geocoding Proxy Service

A simple proxy service that can fetch latitude and longitude for a given address using third party geocoding services (such as HERE, Geonames, Google). 
One of the services act as primary service and the remaining are back-up service. 
Script follows a RESTful HTTP Interface and uses JSON for data serialization.

## Procedure

Requirement: Python3+ 

1. Clone this github repository to a local directory. Go to the local directory through a terminal (e.g. cmd prompt in windows systems). 
2. Change `secrets.json.example` to `secrets.json`

Getting credentials for service providers:
3. Create an account with [Here](https://developer.here.com/documentation/geocoder/topics/quick-start.html) and get your "app id" and "app code". Copy respective fields to those in `secrets.json`
4. Create an account with [Geonames](http://www.geonames.org/login) and add your geonames username field in `secrets.json`

# How to Run and Use:

Start the server: Server can be started by running 'server.py' code in the repository. Default server is 'localhost' and default port is 8800. Optionally, the user can change the port number by using the argument `--port` as shown below.

```
./server
```
In a terminal, type 
```
python server.py --port 8880
```

This will run the service through port 8880 and displays the following:
```
Server is running at http://localhost:8800
Go to your favorite browser and type http://localhost:8800/?address=*YOUR ADDRESS*

Returns {'lat':, 'long':} values..

Press Ctrl+C to exit..
```
As shown above, go to your favourite browser and type *YOUR ADDRESS*

For example:

```
http://localhost:8880/?address=2500%20University%20Drive%20NW%20Calgary
{"lat": 51.07462, "lng": -114.12839}
```
