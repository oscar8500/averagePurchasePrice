# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = exchange_info_from_dict(json.loads(json_string))

from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class RateLimit:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'RateLimit':
        assert isinstance(obj, dict)
        return RateLimit()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class Symbol:
    symbol: Optional[str]
    status: Optional[str]
    base_asset: Optional[str]
    base_asset_precision: Optional[int]
    quote_asset: Optional[str]
    quote_precision: Optional[int]
    quote_asset_precision: Optional[int]
    order_types: Optional[List[str]]
    iceberg_allowed: Optional[bool]
    oco_allowed: Optional[bool]
    quote_order_qty_market_allowed: Optional[bool]
    allow_trailing_stop: Optional[bool]
    is_spot_trading_allowed: Optional[bool]
    is_margin_trading_allowed: Optional[bool]
    filters: Optional[List[Any]]
    permissions: Optional[List[str]]

    def __init__(self, symbol: Optional[str], status: Optional[str], base_asset: Optional[str], base_asset_precision: Optional[int], quote_asset: Optional[str], quote_precision: Optional[int], quote_asset_precision: Optional[int], order_types: Optional[List[str]], iceberg_allowed: Optional[bool], oco_allowed: Optional[bool], quote_order_qty_market_allowed: Optional[bool], allow_trailing_stop: Optional[bool], is_spot_trading_allowed: Optional[bool], is_margin_trading_allowed: Optional[bool], filters: Optional[List[Any]], permissions: Optional[List[str]]) -> None:
        self.symbol = symbol
        self.status = status
        self.base_asset = base_asset
        self.base_asset_precision = base_asset_precision
        self.quote_asset = quote_asset
        self.quote_precision = quote_precision
        self.quote_asset_precision = quote_asset_precision
        self.order_types = order_types
        self.iceberg_allowed = iceberg_allowed
        self.oco_allowed = oco_allowed
        self.quote_order_qty_market_allowed = quote_order_qty_market_allowed
        self.allow_trailing_stop = allow_trailing_stop
        self.is_spot_trading_allowed = is_spot_trading_allowed
        self.is_margin_trading_allowed = is_margin_trading_allowed
        self.filters = filters
        self.permissions = permissions

    @staticmethod
    def from_dict(obj: Any) -> 'Symbol':
        assert isinstance(obj, dict)
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        status = from_union([from_str, from_none], obj.get("status"))
        base_asset = from_union([from_str, from_none], obj.get("baseAsset"))
        base_asset_precision = from_union([from_int, from_none], obj.get("baseAssetPrecision"))
        quote_asset = from_union([from_str, from_none], obj.get("quoteAsset"))
        quote_precision = from_union([from_int, from_none], obj.get("quotePrecision"))
        quote_asset_precision = from_union([from_int, from_none], obj.get("quoteAssetPrecision"))
        order_types = from_union([lambda x: from_list(from_str, x), from_none], obj.get("orderTypes"))
        iceberg_allowed = from_union([from_bool, from_none], obj.get("icebergAllowed"))
        oco_allowed = from_union([from_bool, from_none], obj.get("ocoAllowed"))
        quote_order_qty_market_allowed = from_union([from_bool, from_none], obj.get("quoteOrderQtyMarketAllowed"))
        allow_trailing_stop = from_union([from_bool, from_none], obj.get("allowTrailingStop"))
        is_spot_trading_allowed = from_union([from_bool, from_none], obj.get("isSpotTradingAllowed"))
        is_margin_trading_allowed = from_union([from_bool, from_none], obj.get("isMarginTradingAllowed"))
        filters = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("filters"))
        permissions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("permissions"))
        return Symbol(symbol, status, base_asset, base_asset_precision, quote_asset, quote_precision, quote_asset_precision, order_types, iceberg_allowed, oco_allowed, quote_order_qty_market_allowed, allow_trailing_stop, is_spot_trading_allowed, is_margin_trading_allowed, filters, permissions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["status"] = from_union([from_str, from_none], self.status)
        result["baseAsset"] = from_union([from_str, from_none], self.base_asset)
        result["baseAssetPrecision"] = from_union([from_int, from_none], self.base_asset_precision)
        result["quoteAsset"] = from_union([from_str, from_none], self.quote_asset)
        result["quotePrecision"] = from_union([from_int, from_none], self.quote_precision)
        result["quoteAssetPrecision"] = from_union([from_int, from_none], self.quote_asset_precision)
        result["orderTypes"] = from_union([lambda x: from_list(from_str, x), from_none], self.order_types)
        result["icebergAllowed"] = from_union([from_bool, from_none], self.iceberg_allowed)
        result["ocoAllowed"] = from_union([from_bool, from_none], self.oco_allowed)
        result["quoteOrderQtyMarketAllowed"] = from_union([from_bool, from_none], self.quote_order_qty_market_allowed)
        result["allowTrailingStop"] = from_union([from_bool, from_none], self.allow_trailing_stop)
        result["isSpotTradingAllowed"] = from_union([from_bool, from_none], self.is_spot_trading_allowed)
        result["isMarginTradingAllowed"] = from_union([from_bool, from_none], self.is_margin_trading_allowed)
        result["filters"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.filters)
        result["permissions"] = from_union([lambda x: from_list(from_str, x), from_none], self.permissions)
        return result


class ExchangeInfo:
    timezone: Optional[str]
    server_time: Optional[int]
    rate_limits: Optional[List[RateLimit]]
    exchange_filters: Optional[List[Any]]
    symbols: Optional[List[Symbol]]

    def __init__(self, timezone: Optional[str], server_time: Optional[int], rate_limits: Optional[List[RateLimit]], exchange_filters: Optional[List[Any]], symbols: Optional[List[Symbol]]) -> None:
        self.timezone = timezone
        self.server_time = server_time
        self.rate_limits = rate_limits
        self.exchange_filters = exchange_filters
        self.symbols = symbols

    @staticmethod
    def from_dict(obj: Any) -> 'ExchangeInfo':
        assert isinstance(obj, dict)
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        server_time = from_union([from_int, from_none], obj.get("serverTime"))
        rate_limits = from_union([lambda x: from_list(RateLimit.from_dict, x), from_none], obj.get("rateLimits"))
        exchange_filters = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("exchangeFilters"))
        symbols = from_union([lambda x: from_list(Symbol.from_dict, x), from_none], obj.get("symbols"))
        return ExchangeInfo(timezone, server_time, rate_limits, exchange_filters, symbols)

    def to_dict(self) -> dict:
        result: dict = {}
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["serverTime"] = from_union([from_int, from_none], self.server_time)
        result["rateLimits"] = from_union([lambda x: from_list(lambda x: to_class(RateLimit, x), x), from_none], self.rate_limits)
        result["exchangeFilters"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.exchange_filters)
        result["symbols"] = from_union([lambda x: from_list(lambda x: to_class(Symbol, x), x), from_none], self.symbols)
        return result


def exchange_info_from_dict(s: Any) -> ExchangeInfo:
    return ExchangeInfo.from_dict(s)


def exchange_info_to_dict(x: ExchangeInfo) -> Any:
    return to_class(ExchangeInfo, x)
