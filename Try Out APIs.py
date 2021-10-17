import requests
import pandas as pd

"""
#data = requests.get('http://api.open-notify.org/iss-now.json')
API_KEY = 'eyJhbGciOiJub25lIn0.eyJleHAiOjE2MzQ5ODIzOTcsImp0aSI6ImY0MThjNTE4LTQ4YmYtNGU5My1iZDI1LWRmOGZhODlkNmM4NyJ9.'
payload = {
    'api_key': API_KEY,
    'format': 'json',
    'fromDateAccepted':'2021-01-01'
}

data = requests.get('http://api.openaire.eu/search/publications')
print(data.headers)
print(data.status_code)
print(type(data))
# convert to dictionary
#ddata = data.json()

#print(response)

#print(data.keys())
#print(data['iss_position'])

#print(data['iss_position']['longitude'])


data2 = requests.get('http://api.open-notify.org/astros.json')
print(type(data2))
# convert to dictionary
data2=data2.json()

print(data2)
print(type(data2))

#for p in data2['people']:
#    print(p['name'])

#data3 = requests.get('https://dev.elsevier.com/payloads/metadata/abstractCitationResp.json')
# convert to dictionary
#data3=data3.json()
#print(data3)

"""
response1 = requests.get('https://api.crossref.org/works?rows=1')

output = response1.json()
data3 = pd.DataFrame(output)
# Printing the first 5 rows of the DataFrame using the head() method:

print(data3.head())
# Studying the data size (total rows and columns) using the shape attribute:
print(data3.shape)
#print(data3['message']['items'].keys())
"""
print(data3['message'])
print(data3['message']['items'])
print("1st record: ", data3['message']['items'][0])
print(data3['message']['items'][0]['publisher'])

data4 = pd.DataFrame(data3.keys())
print(data4.head())
"""


### Data Source 2 - Data from WHO Open Data API - Understanding Life Expectancy at Birth

## Step 1 - Querying the Data from WHO Open Data API for Life Expectancy at birth (years) data -
# Loading the requests library to make the HTTP request:

# Packaging the request, sending it and catching the response for WHO OData API url for Life Expectancy at Birth (years) data:
response = requests.get('https://ghoapi.azureedge.net/api/WHOSIS_000001')
# Printing the response and the response status code received from the get request sent:
print(response)


## Step 2 - Retrieving the Data from API and Importing it into a DataFrame -
# Importing the pandas library (alias as pd):
import pandas as pd
# Getting the API response in JSON format and assigning it to a variable:
Life_exp = response.json()
# Importing the JSON response into Pandas DataFrame:
data = pd.DataFrame(Life_exp)
# Printing the first 5 rows of the DataFrame using the head() method:
print(type(data))
print(data.head())
# Studying the data size (total rows and columns) using the shape attribute:
print(data.shape)