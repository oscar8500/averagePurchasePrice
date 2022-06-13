# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = orders_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Order:
    symbol: Optional[str]
    order_id: Optional[int]
    order_list_id: Optional[int]
    client_order_id: Optional[str]
    price: Optional[str]
    orig_qty: Optional[str]
    executed_qty: Optional[str]
    cummulative_quote_qty: Optional[str]
    status: Optional[str]
    time_in_force: Optional[str]
    type: Optional[str]
    side: Optional[str]
    stop_price: Optional[str]
    iceberg_qty: Optional[str]
    time: Optional[int]
    update_time: Optional[int]
    is_working: Optional[bool]
    orig_quote_order_qty: Optional[str]

    def __init__(self, symbol: Optional[str], order_id: Optional[int], order_list_id: Optional[int], client_order_id: Optional[str], price: Optional[str], orig_qty: Optional[str], executed_qty: Optional[str], cummulative_quote_qty: Optional[str], status: Optional[str], time_in_force: Optional[str], type: Optional[str], side: Optional[str], stop_price: Optional[str], iceberg_qty: Optional[str], time: Optional[int], update_time: Optional[int], is_working: Optional[str], orig_quote_order_qty: Optional[str]) -> None:
        self.symbol = symbol
        self.order_id = order_id
        self.order_list_id = order_list_id
        self.client_order_id = client_order_id
        self.price = price
        self.orig_qty = orig_qty
        self.executed_qty = executed_qty
        self.cummulative_quote_qty = cummulative_quote_qty
        self.status = status
        self.time_in_force = time_in_force
        self.type = type
        self.side = side
        self.stop_price = stop_price
        self.iceberg_qty = iceberg_qty
        self.time = time
        self.update_time = update_time
        self.is_working = is_working
        self.orig_quote_order_qty = orig_quote_order_qty

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        assert isinstance(obj, dict)
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        order_id = from_union([from_int, from_none], obj.get("orderId"))
        order_list_id = from_union([from_int, from_none], obj.get("orderListId"))
        client_order_id = from_union([from_str, from_none], obj.get("clientOrderId"))
        price = from_union([from_str, from_none], obj.get("price"))
        orig_qty = from_union([from_str, from_none], obj.get("origQty"))
        executed_qty = from_union([from_str, from_none], obj.get("executedQty"))
        cummulative_quote_qty = from_union([from_str, from_none], obj.get("cummulativeQuoteQty"))
        status = from_union([from_str, from_none], obj.get("status"))
        time_in_force = from_union([from_str, from_none], obj.get("timeInForce"))
        type = from_union([from_str, from_none], obj.get("type"))
        side = from_union([from_str, from_none], obj.get("side"))
        stop_price = from_union([from_str, from_none], obj.get("stopPrice"))
        iceberg_qty = from_union([from_str, from_none], obj.get("icebergQty"))
        time = from_union([from_int, from_none], obj.get("time"))
        update_time = from_union([from_int, from_none], obj.get("updateTime"))
        is_working = from_union([from_bool, from_none], obj.get("isWorking"))
        orig_quote_order_qty = from_union([from_str, from_none], obj.get("origQuoteOrderQty"))
        return Order(symbol, order_id, order_list_id, client_order_id, price, orig_qty, executed_qty, cummulative_quote_qty, status, time_in_force, type, side, stop_price, iceberg_qty, time, update_time, is_working, orig_quote_order_qty)

    def to_dict(self) -> dict:
        result: dict = {}
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["orderId"] = from_union([from_int, from_none], self.order_id)
        result["orderListId"] = from_union([from_int, from_none], self.order_list_id)
        result["clientOrderId"] = from_union([from_str, from_none], self.client_order_id)
        result["price"] = from_union([from_str, from_none], self.price)
        result["origQty"] = from_union([from_str, from_none], self.orig_qty)
        result["executedQty"] = from_union([from_str, from_none], self.executed_qty)
        result["cummulativeQuoteQty"] = from_union([from_str, from_none], self.cummulative_quote_qty)
        result["status"] = from_union([from_str, from_none], self.status)
        result["timeInForce"] = from_union([from_str, from_none], self.time_in_force)
        result["type"] = from_union([from_str, from_none], self.type)
        result["side"] = from_union([from_str, from_none], self.side)
        result["stopPrice"] = from_union([from_str, from_none], self.stop_price)
        result["icebergQty"] = from_union([from_str, from_none], self.iceberg_qty)
        result["time"] = from_union([from_int, from_none], self.time)
        result["updateTime"] = from_union([from_int, from_none], self.update_time)
        result["isWorking"] = from_union([from_bool, from_none], self.is_working)
        result["origQuoteOrderQty"] = from_union([from_str, from_none], self.orig_quote_order_qty)
        return result


def orders_from_dict(s: Any) -> List[Order]:
    return from_list(Order.from_dict, s)


def orders_to_dict(x: List[Order]) -> Any:
    return from_list(lambda x: to_class(Order, x), x)
