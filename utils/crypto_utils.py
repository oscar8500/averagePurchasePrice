import json

import binance
import configs.config_binance as config
import configs.config_crypto_list as crypto_assets
import logging
import data_maps.data_exchange_info as exchange_info
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)
utils_client = Client(config.key, config.secret)


def get_all_possible_pairs_from_binance():
    exchange_pairs = utils_client.exchange_info()
    encoded_response = json.dumps(exchange_pairs)
    result = exchange_info.exchange_info_from_dict(json.loads(encoded_response))

    universal_pairs = {}

    for info in result.symbols:
        universal_pairs[info.symbol] = [info.base_asset, info.quote_asset]
    return universal_pairs


def get_all_possible_pairs_from_config():
    asset_pairs = {}

    for asset1 in crypto_assets.crypto_assets:
        for asset2 in crypto_assets.crypto_assets:
            asset_pairs[asset1+asset2] = [asset1, asset2]
    return asset_pairs


def get_valid_pairs_from_config():
    valid_pairs = []
    pairs_from_config = get_all_possible_pairs_from_config()
    pairs_from_binance = get_all_possible_pairs_from_binance()

    for config_pair in pairs_from_config:
        try:
            pairs_from_config[config_pair] = pairs_from_binance[config_pair]
            valid_pairs.append(config_pair)
        except KeyError:
            pass

    return valid_pairs
