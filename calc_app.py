from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)

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

@app.route('/calc/', methods = ['GET', 'POST'])
def calc():
    codes = []
    for rate in rates:
        codes.append(rate['code'])
    if request.method == 'GET':
        return render_template("currency-calc.html", codes=codes)
    if request.method == 'POST':
        data = request.form
        currency = data.get("currency")
        amount = int(data.get("amount"))
        for rate in rates:
            if currency == rate['code']:
                exchange_price = rate['ask']
                currency_name = rate['currency']
        exchange_value = round(amount * exchange_price,2)
        return render_template("currency-calc.html", codes=codes, exchange_value=exchange_value, currency=currency, amount=amount, currency_name=currency_name)

if __name__ == "__main__":
    app.run(debug=True)