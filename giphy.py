#API kep: nxhW6mUexwlk7glVKoxgrrjs95KHADId
import urllib, json, requests

big_list=[]

new_list = []

payload = {'api_key':'nxhW6mUexwlk7glVKoxgrrjs95KHADId','limit':'60'}
r = requests.get('http://api.giphy.com/v1/gifs/trending?', params=payload)

print(r.status_code)

#print(r.text)

data = json.loads(r.text)

for item in data['data']:


			big_list.append(item)


json.dump(big_list,open('big_list.json','w'),indent=2)

big_list = json.load(open('big_list.json','r'))

for thing in big_list:
	#print(thing['snippet'])
	new_list.append(thing['url'])

json.dump(new_list,open('snip_list.json','w'),indent=2)