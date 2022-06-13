# Gets all Order Transactions and store them in mongoDB

import json
import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from pymongo import MongoClient

import configs.config_binance as cfg
import data_maps.data_orders as order
import utils.crypto_utils as crypto_utils

config_logging(logging, logging.DEBUG)

order_client = Client(cfg.key, cfg.secret)

valid_pairs = crypto_utils.get_valid_pairs_from_config()
binance_orders_list = list()

for pair in valid_pairs:
    returned_values = order_client.get_orders(pair)
    if len(returned_values) > 0:
        encoded_response = json.dumps(returned_values)
        binance_orders_list.extend(order.orders_from_dict(json.loads(encoded_response)))

client = MongoClient()
db = client['binance']
collection = db["transactions"]

for order in binance_orders_list:
    result = collection.insert_one(order.to_dict())
