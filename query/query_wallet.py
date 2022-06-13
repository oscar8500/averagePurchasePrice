#!/usr/bin/env python

import json
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from datetime import datetime
import configs.config_binance as cfg
import data_maps.data_spot as spot

config_logging(logging, logging.DEBUG)

spot_client = Client(cfg.key, cfg.secret)

today = datetime.today()
first_day = datetime.today().replace(day=1)

today_timestamp = int(datetime.timestamp(today)) * 1000
first_day_timestamp = int(datetime.timestamp(first_day)) * 1000

returned_values = spot_client.account_snapshot("SPOT", startTime=first_day_timestamp, endTime=today_timestamp)

encoded_response = json.dumps(returned_values)
binance_spot_info = spot.BinanceSpotfromdict(json.loads(encoded_response))

for snapshot_value in binance_spot_info.snapshotVos:
    update_type = snapshot_value.type.value
    update_time = datetime.fromtimestamp(int(snapshot_value.updateTime) / 1000)

    print(update_time)
    print(update_type)

    total_BTC = snapshot_value.data.totalAssetOfBtc
    print("Spot Balance in BTC: " + total_BTC)

    for asset in snapshot_value.data.balances:
        if float(asset.free) + float(asset.locked) > 0:
            print("Balance in " + str(asset.asset) + ": " + str(asset.free))
    print("----------**********----------**********----------**********----------**********----------**********----------**********----------**********")
