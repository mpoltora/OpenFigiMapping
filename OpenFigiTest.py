import json
import requests

openfigi_url = 'https://api.openfigi.com/v1/mapping'
with open('key.txt', 'r') as f:  # Requires a text file containing the API key
    openfigi_apikey = f.readline()
openfigi_headers = {'Content-Type': 'text/json'}

sampleUserData = ['UN', 'UF', 'LN', 'US']  # Sample user data. Users will input the exchanges they would like to search

if openfigi_apikey:
    openfigi_headers['X-OPENFIGI-APIKEY'] = openfigi_apikey

# jobs = [{'idType': 'TICKER', 'idValue': 'APC', "exchCode":"GF"}]

# jobs = [{'idType': 'TICKER', 'idValue': 'APC', "exchCode":"GS"}]

# jobs.append({'idType': 'TICKER', 'idValue': 'APC', "exchCode":"GF"})`

# jobs = [{'idType': 'TICKER', 'idValue': 'GOOGL', "exchCode":"SW"}]

# jobs = [{'idType': 'TICKER', 'idValue': 'AAPL*', "exchCode":"MM"}]

# jobs = [{'idType': 'TICKER', 'idValue': 'AAPL*'}]

jobs = []

# Check each of the exchanges for a given ticker
for i in sampleUserData:
    jobs.append({'idType': 'TICKER', 'idValue': 'GOOG', "exchCode":i})

r = requests.post('https://api.openfigi.com/v1/mapping',
                      headers=openfigi_headers,
                      data=json.dumps(jobs))
print(r)

for job, result in zip(jobs, r.json()):
    figi_list = result.get('data')
    print(figi_list)
