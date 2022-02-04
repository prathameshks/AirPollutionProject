import math
def deg2num(lat_deg, lon_deg, zoom):
	lat_rad = math.radians(lat_deg)
	n = 2.0 ** zoom
	xtile = int((lon_deg + 180.0) / 360.0 * n)
	ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
	return (xtile, ytile)


print(deg2num(75.67, 18.46, 7))







# import requests
# url2="https://tiles.aqicn.org/tiles/{usepa-aqi}/{z}/{x}/{y}.png?token=aa47374836b21e3e050b3b9fb4131bfd74b1474a"
# data=requests.get(url2)

# print(data)

# f=open("htmlfile.html","w")

# txt="""<html><body><div  id='map'  style='height:600px;'  />  
# <link  rel="stylesheet"  href="http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.css"  />  
# <script  src="http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.js"></script>  
#   <script>  
#       var  OSM_URL  =  'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';  
#       var  OSM_ATTRIB  =  '&copy;Python Air Project';  
#       var  osmLayer  =  L.tileLayer(OSM_URL,  {attribution:  OSM_ATTRIB});  
  
#       var  WAQI_URL    =  "https://tiles.waqi.info/tiles/usepa-aqi/{z}/{x}/{y}.png?token=37f96394ffe8b6cca1110af3d8270604c711c688";  
#       var  WAQI_ATTR  =  'JNV 2020';  
#       var  waqiLayer  =  L.tileLayer(WAQI_URL,  {attribution:  WAQI_ATTR});  
  
#       var  map  =  L.map('map').setView([28.63576,77.22445],  11);  
#       map.addLayer(osmLayer).addLayer(waqiLayer);  
# </script></body></html>"""
# f.write(txt)
# f.close()

"""import tkinter as tk
import gmaps
gmaps.configure(api_key='AIzaSyBNV17BBCnBZ0z2JS9UTDPJr1ostm69_bo')

root=tk.Tk()

coordinates = (40.75, -74.00)
fig=gmaps.figure(center=coordinates, zoom_level=12)
# lab=tk.Label(master=root, image=fig)
# lab.pack()
print(type(fig))
gmaps.save("map.png")
root.mainloop()
# Python program to get a google map  
# image of specified location using  
# Google Static Maps API 
  
# importing required modules 
import requests 
  
# Enter your api key here 
api_key = "AIzaSyBNV17BBCnBZ0z2JS9UTDPJr1ostm69_bo"
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map.  
center = "Dehradun"
  
# zoom defines the zoom 
# level of the map 
zoom = 10
  
# get method of requests module 
# return response object 
r = requests.get(url + "center =" + center + "&zoom =" +
                   str(zoom) + "&size = 400x400&key =" +
                             api_key + "sensor = false"+"&size=200") 
  
# wb mode is stand for write binary mode 
f = open('address of the file location ', 'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content) 
  
# close method of file object 
# save and close the file 
f.close() """