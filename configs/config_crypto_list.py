import datetime

# This is a list of crypto assets you're interested in or have executed orders with.
crypto_assets = ['ADA', 'ALGO', 'ALPINE', 'AVAX', 'BETH', 'BNB', 'BTC', 'BUSD', 'CAKE', 'DOCK', 'DOT', 'ETH', 'FTM',
                 'FTT', 'GAL', 'GALA', 'HBAR', 'LINK', 'LTC', 'LUNA', 'LUNC', 'MANA', 'MATIC', 'NEAR', 'SHIB', 'SOL',
                 'TRX', 'USDT', 'XRP']

__starting_date_year = 2021
__starting_date_month = 10
__starting_date_day = 1

starting_timestamp = int(
    datetime.datetime.timestamp(
        datetime.datetime(__starting_date_year,
                          __starting_date_month,
                          __starting_date_day)
    ) * 1000)
