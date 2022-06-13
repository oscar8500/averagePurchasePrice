import decimal
from bson.decimal128 import Decimal128
from pymongo import MongoClient

from utils import crypto_utils

client = MongoClient()
db = client['binance']
collection = db["transactions"]


def get_sell_order_price_average():
    query_filter = {
        'status': 'FILLED',
        'side': 'SELL'
    }
    return get_order_price_average(query_filter)


def get_buy_order_price_average():
    query_filter = {
        'status': 'FILLED',
        'side': 'BUY'
    }
    return get_order_price_average(query_filter)


def get_order_price_average(query_filter: dict):
    query_project = {
        '_id': 0,
        'symbol': '$symbol',
        'executedQty': {
            '$toDecimal': '$executedQty'
        },
        'cummulativeQuoteQty': {
            '$toDecimal': '$cummulativeQuoteQty'
        },
        'price': {
            '$divide': [
                {
                    '$toDecimal': '$cummulativeQuoteQty'
                }, {
                    '$toDecimal': '$executedQty'
                }
            ]
        }
    }
    query_sort = list({
                          'symbol': 1
                      }.items())

    result = client['binance']['transactions'].find(filter=query_filter,
                                                    projection=query_project,
                                                    sort=query_sort
                                                    )
    valid_pairs = crypto_utils.get_valid_pairs_from_config()
    order_pairs = dict()

    for pair in valid_pairs:
        order_pairs[pair] = {'price': 0, 'cummulativeQuoteQty': 0, 'executedQty': 0}

    for smth in result:
        currentSymbol = smth['symbol']
        currentPrice = Decimal128.to_decimal(smth['price'])
        currentExecutedQty = Decimal128.to_decimal(smth['executedQty'])
        currentQuoteQty = Decimal128.to_decimal(smth['cummulativeQuoteQty'])

        lastPrice = decimal.Decimal(order_pairs[currentSymbol]['price'])
        lastExecutedQty = decimal.Decimal(order_pairs[currentSymbol]['executedQty'])
        lastQuoteQty = decimal.Decimal(order_pairs[currentSymbol]['cummulativeQuoteQty'])

        nextExecutedQty = lastExecutedQty + currentExecutedQty

        lastWExecutedQty = (lastExecutedQty / nextExecutedQty)
        currentWExecutedQty = (currentExecutedQty / nextExecutedQty)

        nextPrice = lastPrice * lastWExecutedQty + currentPrice * currentWExecutedQty
        nextQuoteQty = lastQuoteQty + currentQuoteQty

        order_pairs[currentSymbol]['price'] = nextPrice
        order_pairs[currentSymbol]['executedQty'] = nextExecutedQty
        order_pairs[currentSymbol]['cummulativeQuoteQty'] = nextQuoteQty

    return order_pairs

print(get_buy_order_price_average())
print(get_sell_order_price_average())