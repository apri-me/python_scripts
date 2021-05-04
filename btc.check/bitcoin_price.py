import requests

url = "https://api.coinex.com/v1/market/ticker"
market = 'BTCUSDT'
params = {'market': market}
r = requests.get(url, params=params)
if r.json()['code']:
    raise Exception(r.json()['message'])
print(r.json()['data']['ticker']['last'])