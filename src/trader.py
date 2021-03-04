from types import SimpleNamespace

import json
import requests

from config import *


def get_ark_holdings():
    r = requests.get(ARK_HOLDINGS, params={'symbol': 'ARKK'})
    return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))


def get_ark_today_trades():
    r = requests.get(ARK_TRADES, params={'symbol': 'ARKK'})
    return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))


def create_order(symbol, notional, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "notional": notional,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


buying_power = get_account().buying_power
for i in get_ark_holdings().holdings:
    portfolio_amount = "{:.2f}".format(float(buying_power) * (i.weight / 100))
    print(f'{i.ticker}, {portfolio_amount}, buy, market, day')
    response = create_order(i.ticker, portfolio_amount, "buy", "market", "day")

for i in get_ark_today_trades().trades:
    print(f'{i.ticker} - {i.etf_percent} - {i.direction}')
