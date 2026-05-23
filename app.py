from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    coin = "bitcoin"

    if request.method == 'POST':
        coin = request.form['coin']

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    data = response.json()

    try:
        price = data[coin]['usd']
    except:
        price = "Coin Not Found"

    return render_template(
        "index.html",
        coin=coin,
        price=price
    )

if __name__ == '__main__':
    app.run(debug=True)