import requests, json 

api_key = 'AIzaSyAZO5u3CT44YzNDSVdzit3dxs_TL_dZ9iM'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query = input('Search query: ') 
r = requests.get(url + 'query=' + query + '&key=' + api_key)
file = open("output.json", "w")
file.write(r.text)
file.close()




