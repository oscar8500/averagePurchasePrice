# Gets all savings purchases (move to savings wallet from spot)

import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client

import configs.config_binance as config

config_logging(logging, logging.DEBUG)

savings_purchase_client = Client(config.key, config.secret)

result = savings_purchase_client.savings_purchase_record("DAILY")
print(result)
result = savings_purchase_client.savings_purchase_record("CUSTOMIZED_FIXED")
print(result)
