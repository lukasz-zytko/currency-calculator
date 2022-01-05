import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

for rate in rates:
    print(rate['code']+";"+str(rate['bid']))