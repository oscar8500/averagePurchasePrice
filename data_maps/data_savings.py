# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = savings_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class PositionAmountVo:
    asset: Optional[str]
    amount: Optional[str]
    amount_in_btc: Optional[str]
    amount_in_usdt: Optional[str]

    def __init__(self, asset: Optional[str], amount: Optional[str], amount_in_btc: Optional[str],
                 amount_in_usdt: Optional[str]) -> None:
        self.asset = asset
        self.amount = amount
        self.amount_in_btc = amount_in_btc
        self.amount_in_usdt = amount_in_usdt

    @staticmethod
    def from_dict(obj: Any) -> 'PositionAmountVo':
        assert isinstance(obj, dict)
        asset = from_union([from_str, from_none], obj.get("asset"))
        amount = from_union([from_str, from_none], obj.get("amount"))
        amount_in_btc = from_union([from_str, from_none], obj.get("amountInBTC"))
        amount_in_usdt = from_union([from_str, from_none], obj.get("amountInUSDT"))
        return PositionAmountVo(asset, amount, amount_in_btc, amount_in_usdt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_union([from_str, from_none], self.asset)
        result["amount"] = from_union([from_str, from_none], self.amount)
        result["amountInBTC"] = from_union([from_str, from_none], self.amount_in_btc)
        result["amountInUSDT"] = from_union([from_str, from_none], self.amount_in_usdt)
        return result


class Savings:
    total_amount_in_btc: Optional[str]
    total_amount_in_usdt: Optional[str]
    total_fixed_amount_in_btc: Optional[str]
    total_fixed_amount_in_usdt: Optional[str]
    total_flexible_in_btc: Optional[str]
    total_flexible_in_usdt: Optional[str]
    position_amount_vos: Optional[List[PositionAmountVo]]

    def __init__(self, total_amount_in_btc: Optional[str], total_amount_in_usdt: Optional[str],
                 total_fixed_amount_in_btc: Optional[str], total_fixed_amount_in_usdt: Optional[str],
                 total_flexible_in_btc: Optional[str], total_flexible_in_usdt: Optional[str],
                 position_amount_vos: Optional[List[PositionAmountVo]]) -> None:
        self.total_amount_in_btc = total_amount_in_btc
        self.total_amount_in_usdt = total_amount_in_usdt
        self.total_fixed_amount_in_btc = total_fixed_amount_in_btc
        self.total_fixed_amount_in_usdt = total_fixed_amount_in_usdt
        self.total_flexible_in_btc = total_flexible_in_btc
        self.total_flexible_in_usdt = total_flexible_in_usdt
        self.position_amount_vos = position_amount_vos

    @staticmethod
    def from_dict(obj: Any) -> 'Savings':
        assert isinstance(obj, dict)
        total_amount_in_btc = from_union([from_str, from_none], obj.get("totalAmountInBTC"))
        total_amount_in_usdt = from_union([from_str, from_none], obj.get("totalAmountInUSDT"))
        total_fixed_amount_in_btc = from_union([from_str, from_none], obj.get("totalFixedAmountInBTC"))
        total_fixed_amount_in_usdt = from_union([from_str, from_none], obj.get("totalFixedAmountInUSDT"))
        total_flexible_in_btc = from_union([from_str, from_none], obj.get("totalFlexibleInBTC"))
        total_flexible_in_usdt = from_union([from_str, from_none], obj.get("totalFlexibleInUSDT"))
        position_amount_vos = from_union([lambda x: from_list(PositionAmountVo.from_dict, x), from_none],
                                         obj.get("positionAmountVos"))
        return Savings(total_amount_in_btc, total_amount_in_usdt, total_fixed_amount_in_btc, total_fixed_amount_in_usdt,
                       total_flexible_in_btc, total_flexible_in_usdt, position_amount_vos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalAmountInBTC"] = from_union([from_str, from_none], self.total_amount_in_btc)
        result["totalAmountInUSDT"] = from_union([from_str, from_none], self.total_amount_in_usdt)
        result["totalFixedAmountInBTC"] = from_union([from_str, from_none], self.total_fixed_amount_in_btc)
        result["totalFixedAmountInUSDT"] = from_union([from_str, from_none], self.total_fixed_amount_in_usdt)
        result["totalFlexibleInBTC"] = from_union([from_str, from_none], self.total_flexible_in_btc)
        result["totalFlexibleInUSDT"] = from_union([from_str, from_none], self.total_flexible_in_usdt)
        result["positionAmountVos"] = from_union(
            [lambda x: from_list(lambda x: to_class(PositionAmountVo, x), x), from_none], self.position_amount_vos)
        return result


def savings_from_dict(s: Any) -> Savings:
    return Savings.from_dict(s)


def savings_to_dict(x: Savings) -> Any:
    return to_class(Savings, x)
