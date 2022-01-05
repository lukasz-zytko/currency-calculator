import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = response.json()[0].get('rates')

def export_items_to_csv():
    with open('currency.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["currency", "code", "bid", "ask"]
        currency = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        currency.writeheader()
        for rate in rates:
            currency.writerow({"currency": rate["currency"], "code": rate["code"], "bid": rate["bid"], "ask": rate["ask"]})

export_items_to_csv()

"""
def load_items_from_csv(a='magazyn.csv'):
    with open(a, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        items.clear()
        for row in reader:
            items.append({"name": row["name"], "quantity": row["quantity"], "unit": row["unit"], "unit_price": row["unit_price"]})
        print("List successfully loaded!")
"""