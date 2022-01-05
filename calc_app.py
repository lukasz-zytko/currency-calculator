import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

def export_items_to_csv():
    with open('currency.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["currency", "code", "bid", "ask"]
        currency = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        currency.writeheader()
        for rate in rates:
            currency.writerow({"currency": rate["currency"], "code": rate["code"], "bid": rate["bid"], "ask": rate["ask"]})

#export_items_to_csv()

print(rates[0]['code'])