import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

def export_items_to_csv():
    with open('currency.csv', 'w', newline='') as csvfile:
        fieldnames = ["currency", "code", "bid", "ask"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for rate in rates:
            writer.writerow({"currency": rate["currency"], "code": rate["code"], "bid": rate["bid"], "ask": rate["ask"]})

export_items_to_csv()

for rate in rates:
    print(rate['code']+";"+str(rate['bid']))

"""
def load_items_from_csv(a='magazyn.csv'):
    with open(a, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        items.clear()
        for row in reader:
            items.append({"name": row["name"], "quantity": row["quantity"], "unit": row["unit"], "unit_price": row["unit_price"]})
        print("List successfully loaded!")
"""