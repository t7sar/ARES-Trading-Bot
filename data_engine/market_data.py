
from dataclasses import dataclass


@dataclass
class MarketData:
    symbol: str
    timeframe: str
    open: float
    high: float
    low: float
    close: float
    volume: float


class DataEngine:

    def validate(self, data: MarketData) -> bool:

        if data.high < data.low:
            return False

        if data.high < max(data.open, data.close):
            return False

        if data.low > min(data.open, data.close):
            return False

        if min(data.open, data.high, data.low, data.close) <= 0:
            return False

        if data.volume < 0:
            return False

        return True

    def process(self, data: MarketData):

        if not self.validate(data):
            raise ValueError("Invalid market data")

        return {
            "symbol": data.symbol,
            "timeframe": data.timeframe,
            "close": data.close,
            "volume": data.volume,
            "status": "VALID"
        }
