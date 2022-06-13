# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = p2_p_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")

def from_bool(x:Any) ->bool:
    assert isinstance(x,bool)
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


class Datum:
    order_number: Optional[str]
    adv_no: Optional[str]
    trade_type: Optional[str]
    asset: Optional[str]
    fiat: Optional[str]
    fiat_symbol: Optional[str]
    amount: Optional[str]
    total_price: Optional[str]
    unit_price: Optional[str]
    order_status: Optional[str]
    create_time: Optional[int]
    commission: Optional[str]
    counter_part_nick_name: Optional[str]
    advertisement_role: Optional[str]

    def __init__(self, order_number: Optional[str], adv_no: Optional[str], trade_type: Optional[str], asset: Optional[str], fiat: Optional[str], fiat_symbol: Optional[str], amount: Optional[str], total_price: Optional[str], unit_price: Optional[str], order_status: Optional[str], create_time: Optional[int], commission: Optional[str], counter_part_nick_name: Optional[str], advertisement_role: Optional[str]) -> None:
        self.order_number = order_number
        self.adv_no = adv_no
        self.trade_type = trade_type
        self.asset = asset
        self.fiat = fiat
        self.fiat_symbol = fiat_symbol
        self.amount = amount
        self.total_price = total_price
        self.unit_price = unit_price
        self.order_status = order_status
        self.create_time = create_time
        self.commission = commission
        self.counter_part_nick_name = counter_part_nick_name
        self.advertisement_role = advertisement_role

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        order_number = from_union([from_str, from_none], obj.get("orderNumber"))
        adv_no = from_union([from_str, from_none], obj.get("advNo"))
        trade_type = from_union([from_str, from_none], obj.get("tradeType"))
        asset = from_union([from_str, from_none], obj.get("asset"))
        fiat = from_union([from_str, from_none], obj.get("fiat"))
        fiat_symbol = from_union([from_str, from_none], obj.get("fiatSymbol"))
        amount = from_union([from_str, from_none], obj.get("amount"))
        total_price = from_union([from_str, from_none], obj.get("totalPrice"))
        unit_price = from_union([from_str, from_none], obj.get("unitPrice"))
        order_status = from_union([from_str, from_none], obj.get("orderStatus"))
        create_time = from_union([from_int, from_none], obj.get("createTime"))
        commission = from_union([from_str, from_none], obj.get("commission"))
        counter_part_nick_name = from_union([from_str, from_none], obj.get("counterPartNickName"))
        advertisement_role = from_union([from_str, from_none], obj.get("advertisementRole"))
        return Datum(order_number, adv_no, trade_type, asset, fiat, fiat_symbol, amount, total_price, unit_price, order_status, create_time, commission, counter_part_nick_name, advertisement_role)

    def to_dict(self) -> dict:
        result: dict = {}
        result["orderNumber"] = from_union([from_str, from_none], self.order_number)
        result["advNo"] = from_union([from_str, from_none], self.adv_no)
        result["tradeType"] = from_union([from_str, from_none], self.trade_type)
        result["asset"] = from_union([from_str, from_none], self.asset)
        result["fiat"] = from_union([from_str, from_none], self.fiat)
        result["fiatSymbol"] = from_union([from_str, from_none], self.fiat_symbol)
        result["amount"] = from_union([from_str, from_none], self.amount)
        result["totalPrice"] = from_union([from_str, from_none], self.total_price)
        result["unitPrice"] = from_union([from_str, from_none], self.unit_price)
        result["orderStatus"] = from_union([from_str, from_none], self.order_status)
        result["createTime"] = from_union([from_int, from_none], self.create_time)
        result["commission"] = from_union([from_str, from_none], self.commission)
        result["counterPartNickName"] = from_union([from_str, from_none], self.counter_part_nick_name)
        result["advertisementRole"] = from_union([from_str, from_none], self.advertisement_role)
        return result


class P2P:
    code: Optional[str]
    message: Optional[str]
    data: Optional[List[Datum]]
    total: Optional[int]
    success: Optional[bool]

    def __init__(self, code: Optional[str], message: Optional[str], data: Optional[List[Datum]], total: Optional[int], success: Optional[bool]) -> None:
        self.code = code
        self.message = message
        self.data = data
        self.total = total
        self.success = success

    @staticmethod
    def from_dict(obj: Any) -> 'P2P':
        assert isinstance(obj, dict)
        code = from_union([from_str, from_none], obj.get("code"))
        message = from_union([from_str, from_none], obj.get("message"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        total = from_union([from_int, from_none], obj.get("total"))
        success = from_union([from_bool, from_none], obj.get("success"))
        return P2P(code, message, data, total, success)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_str, from_none], self.code)
        result["message"] = from_union([from_str, from_none], self.message)
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["total"] = from_union([from_int, from_none], self.total)
        result["success"] = from_union([from_bool, from_none], self.success)
        return result


def p2_p_from_dict(s: Any) -> P2P:
    return P2P.from_dict(s)


def p2_p_to_dict(x: P2P) -> Any:
    return to_class(P2P, x)
