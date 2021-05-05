# Ako nemate flask onda sljedeća naredba u terminalu:
# pip install -r requirements.txt 
# Ako javlja grešku za requests onda sljedeća naredba u terminalu::
# pip3 install requests 

from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    api_key = "" # upišite svoj API ključ!!! sa stranice https://www.alphavantage.co/

    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={0}".format(api_key)

    data = requests.get(url=url)

    data_json = data.json()

    print(data_json) # ispisujemo sve podatke

    btc = "{:.2f}".format(float(data_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])) # uzimamo vrijednost bitcoina u dolarima i formatiramo na dvije decimale

    print(btc)

    return render_template("index.html", btc=btc)

if __name__ == "__main__":
    app.run()
