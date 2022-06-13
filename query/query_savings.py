# Gets all existent savings and saves them in mongoDB

import json
import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client

import configs.config_binance as cfg
import data_maps.data_savings as savings

config_logging(logging, logging.DEBUG)

savings_client = Client(cfg.key, cfg.secret)

returned_values = savings_client.savings_account()

encoded_response = json.dumps(returned_values)
binance_savings_info = savings.savings_from_dict(returned_values)

print("Total Savings Balance in BTC: " + str(binance_savings_info.total_amount_in_btc))
print("Total Savings Balance in USDT: " + str(binance_savings_info.total_amount_in_usdt))

print("Flexible Savings Balance in BTC: " + str(binance_savings_info.total_flexible_in_btc))
print("Flexible Savings Balance in USDT: " + str(binance_savings_info.total_flexible_in_usdt))

print("Fixed Savings Balance in BTC: " + str(binance_savings_info.total_fixed_amount_in_btc))
print("Fixed Savings Balance in USDT: " + str(binance_savings_info.total_fixed_amount_in_usdt))

for asset in binance_savings_info.position_amount_vos:
    print(str(asset.asset))
    print(str(asset.amount))
    print(str(asset.amount_in_btc))
    print(str(asset.amount_in_usdt))
