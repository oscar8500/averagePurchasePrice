#!/usr/bin/env python

import json
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
import configs.config_binance as cfg
import data_maps.data_ticker as ticker
import utils.crypto_utils as utils

config_logging(logging, logging.DEBUG)


spot_client = Client(cfg.key, cfg.secret)
symbol = utils.get_valid_pairs_from_config()


returned_values = list()

if symbol is not None:
    for q_symbol in symbol:
        returned_values.append(spot_client.ticker_price(q_symbol))

encoded_response = json.dumps(returned_values)

binance_ticker_info = ticker.ticker_from_dict(json.loads(encoded_response))
