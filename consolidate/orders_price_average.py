import decimal

from bson.decimal128 import Decimal128
from pymongo import MongoClient

from utils import crypto_utils

client = MongoClient()
db = client['binance']
collection = db["transactions"]


# Gets the average order price for filled and sell orders
def get_sell_order_price_average():
    query_filter = {
        'status': 'FILLED',
        'side': 'SELL'
    }
    return get_order_price_average(query_filter)


# Gets the average order price for filled and buy orders
def get_buy_order_price_average():
    query_filter = {
        'status': 'FILLED',
        'side': 'BUY'
    }
    return get_order_price_average(query_filter)


# Gets the average order price for a given filter ordered by symbol
def get_order_price_average(query_filter: dict):
    query_project = {
        '_id': 0,
        'symbol': '$symbol',
        'executedQty': {
            '$toDecimal': '$executedQty'
        },
        'cumulativeQuoteQty': {
            '$toDecimal': '$cumulativeQuoteQty'
        },
        'price': {
            '$divide': [
                {
                    '$toDecimal': '$cumulativeQuoteQty'
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
        order_pairs[pair] = {'price': 0, 'cumulativeQuoteQty': 0, 'executedQty': 0}

    for smth in result:
        current_symbol = smth['symbol']
        current_price = Decimal128.to_decimal(smth['price'])
        current_executed_qty = Decimal128.to_decimal(smth['executedQty'])
        current_quote_qty = Decimal128.to_decimal(smth['cumulativeQuoteQty'])

        last_price = decimal.Decimal(order_pairs[current_symbol]['price'])
        last_executed_qty = decimal.Decimal(order_pairs[current_symbol]['executedQty'])
        last_quote_qty = decimal.Decimal(order_pairs[current_symbol]['cumulativeQuoteQty'])

        next_executed_qty = last_executed_qty + current_executed_qty

        last_weighted_executed_qty = (current_executed_qty / next_executed_qty)
        current_weighted_executed_qty = (current_executed_qty / next_executed_qty)

        next_price = last_price * last_weighted_executed_qty + current_price * current_weighted_executed_qty
        next_quote_qty = last_quote_qty + current_quote_qty

        order_pairs[current_symbol]['price'] = next_price
        order_pairs[current_symbol]['executedQty'] = next_executed_qty
        order_pairs[current_symbol]['cumulativeQuoteQty'] = next_quote_qty

    return order_pairs


print(get_buy_order_price_average())
#print(get_sell_order_price_average())
