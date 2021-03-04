from keys import *

API_KEY = API
SECRET_KEY = SECRET

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)

ARK_HOLDINGS = 'https://arkfunds.io/api/v1/etf/holdings'
ARK_TRADES = 'https://arkfunds.io/api/v1/etf/trades'

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
