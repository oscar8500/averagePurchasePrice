# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ticker_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class TickerElement:
    symbol: str
    price: int

    @staticmethod
    def from_dict(obj: Any) -> 'TickerElement':
        assert isinstance(obj, dict)
        symbol = from_str(obj.get("symbol"))
        price = from_str(obj.get("price"))
        return TickerElement(symbol, price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["symbol"] = from_str(self.symbol)
        result["price"] = from_str(self.price)
        return result


def ticker_from_dict(s: Any) -> List[TickerElement]:
    return from_list(TickerElement.from_dict, s)


def ticker_to_dict(x: List[TickerElement]) -> Any:
    return from_list(lambda x: to_class(TickerElement, x), x)
