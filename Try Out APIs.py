import requests

data = requests.get('http://api.open-notify.org/iss-now.json')

# convert to dictionary
data=data.json()

print(data)
print(type(data))
print(data['iss_position'])

print(data['iss_position']['longitude'])


data2 = requests.get('http://api.open-notify.org/astros.json')

# convert to dictionary
data2=data2.json()

print(data2)
print(type(data2))

for p in data2['people']:
    print(p['name'])

data3 = requests.get('https://dev.elsevier.com/payloads/metadata/abstractCitationResp.json')
# convert to dictionary
data3=data3.json()
print(data3)