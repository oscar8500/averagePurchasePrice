# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = savings_purchase_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class LendingType(Enum):
    DAILY = "DAILY",
    CUSTOMIZED_FIXED = "CUSTOMIZED_FIXED"


class Status(Enum):
    SUCCESS = "SUCCESS"


class SavingsPurchaseElement:
    purchase_id: Optional[int]
    create_time: Optional[int]
    product_name: Optional[str]
    asset: Optional[str]
    amount: Optional[str]
    status: Optional[Status]
    lending_type: Optional[LendingType]

    def __init__(self, purchase_id: Optional[int], create_time: Optional[int], product_name: Optional[str], asset: Optional[str], amount: Optional[str], status: Optional[Status], lending_type: Optional[LendingType]) -> None:
        self.purchase_id = purchase_id
        self.create_time = create_time
        self.product_name = product_name
        self.asset = asset
        self.amount = amount
        self.status = status
        self.lending_type = lending_type

    @staticmethod
    def from_dict(obj: Any) -> 'SavingsPurchaseElement':
        assert isinstance(obj, dict)
        purchase_id = from_union([from_int, from_none], obj.get("purchaseId"))
        create_time = from_union([from_int, from_none], obj.get("createTime"))
        product_name = from_union([from_str, from_none], obj.get("productName"))
        asset = from_union([from_str, from_none], obj.get("asset"))
        amount = from_union([from_str, from_none], obj.get("amount"))
        status = from_union([Status, from_none], obj.get("status"))
        lending_type = from_union([LendingType, from_none], obj.get("lendingType"))
        return SavingsPurchaseElement(purchase_id, create_time, product_name, asset, amount, status, lending_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["purchaseId"] = from_union([from_int, from_none], self.purchase_id)
        result["createTime"] = from_union([from_int, from_none], self.create_time)
        result["productName"] = from_union([from_str, from_none], self.product_name)
        result["asset"] = from_union([from_str, from_none], self.asset)
        result["amount"] = from_union([from_str, from_none], self.amount)
        result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        result["lendingType"] = from_union([lambda x: to_enum(LendingType, x), from_none], self.lending_type)
        return result


def savings_purchase_from_dict(s: Any) -> List[SavingsPurchaseElement]:
    return from_list(SavingsPurchaseElement.from_dict, s)


def savings_purchase_to_dict(x: List[SavingsPurchaseElement]) -> Any:
    return from_list(lambda x: to_class(SavingsPurchaseElement, x), x)
