# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = BinanceSpotfromdict(json.loads(json_string))

from dataclasses import dataclass
from enum import Enum
from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


@dataclass
class Balance:
    asset: str
    free: int
    locked: int

    @staticmethod
    def from_dict(obj: Any) -> 'Balance':
        assert isinstance(obj, dict)
        asset = from_str(obj.get("asset"))
        free = from_str(obj.get("free"))
        locked = (from_str(obj.get("locked")))
        return Balance(asset, free, locked)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = from_str(self.asset)
        result["free"] = from_str(self.free)
        result["locked"] = from_str(str(self.locked))
        return result


@dataclass
class Data:
    totalAssetOfBtc: str
    balances: List[Balance]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        totalAssetOfBtc = from_str(obj.get("totalAssetOfBtc"))
        balances = from_list(Balance.from_dict, obj.get("balances"))
        return Data(totalAssetOfBtc, balances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalAssetOfBtc"] = from_str(self.totalAssetOfBtc)
        result["balances"] = from_list(lambda x: to_class(Balance, x), self.balances)
        return result


class TypeEnum(Enum):
    spot = "spot"


@dataclass
class SnapshotVo:
    type: TypeEnum
    updateTime: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'SnapshotVo':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        updateTime = from_int(obj.get("updateTime"))
        data = Data.from_dict(obj.get("data"))
        return SnapshotVo(type, updateTime, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["updateTime"] = from_int(self.updateTime)
        result["data"] = to_class(Data, self.data)
        return result


@dataclass
class BinanceSpot:
    code: int
    msg: str
    snapshotVos: List[SnapshotVo]

    @staticmethod
    def from_dict(obj: Any) -> 'BinanceSpot':
        assert isinstance(obj, dict)
        code = from_int(obj.get("code"))
        msg = from_str(obj.get("msg"))
        snapshotVos = from_list(SnapshotVo.from_dict, obj.get("snapshotVos"))
        return BinanceSpot(code, msg, snapshotVos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_int(self.code)
        result["msg"] = from_str(self.msg)
        result["snapshotVos"] = from_list(lambda x: to_class(SnapshotVo, x), self.snapshotVos)
        return result


def BinanceSpotfromdict(s: Any) -> BinanceSpot:
    return BinanceSpot.from_dict(s)


def BinanceSpottodict(x: BinanceSpot) -> Any:
    return to_class(BinanceSpot, x)
