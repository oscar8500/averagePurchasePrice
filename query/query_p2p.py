# Gets all P2P Transactions and store them in mongoDB

import json
import logging
from datetime import datetime, timedelta

from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from pymongo import MongoClient

import configs.config_binance as cfg
from configs.config_crypto_list import starting_timestamp
from data_maps.data_p2p import p2_p_from_dict

config_logging(logging, logging.DEBUG)

p2p_client = Client(cfg.key, cfg.secret)


def get_p2p_historic(start_timestamp: int, end_timestamp: int):
    # 30 day limit
    returned_values = p2p_client.c2c_trade_history(tradeType='BUY',
                                                   startTimestamp=start_timestamp,
                                                   endTimestamp=end_timestamp)
    encoded_response = json.dumps(returned_values)
    p2p_response = p2_p_from_dict(json.loads(encoded_response))
    return p2p_response


def get_p2p_all_history():
    start_date = datetime.fromtimestamp(starting_timestamp / 1000)
    delta = timedelta(days=30)
    end_date = datetime.now()
    p2p_order_list = list()

    while start_date < end_date:
        start_timestamp = int(datetime.timestamp(start_date)) * 1000
        end_timestamp = int(datetime.timestamp(start_date + delta)) * 1000

        p2p_historic = get_p2p_historic(start_timestamp, end_timestamp)
        p2p_order_list.extend(p2p_historic.to_dict()["data"])

        if start_date < end_date:
            start_date = start_date + delta
        if start_date == end_date:
            start_date = end_date + delta
        if start_date > end_date:
            start_date = end_date

    return p2p_order_list


client = MongoClient()
db = client['binance']
collection = db["p2p"]
for order in get_p2p_all_history():
    result = collection.insert_one(order)
