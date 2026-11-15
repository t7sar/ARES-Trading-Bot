
class BaseStrategy:

    def __init__(self):
        self.name = "ARES Strategy"

    def generate_signal(self, prices):

        if len(prices) < 20:
            return {
                "signal": "HOLD",
                "reason": "Insufficient market data"
            }

        short_sma = sum(prices[-5:]) / 5
        long_sma = sum(prices[-20:]) / 20

        previous_short = sum(prices[-6:-1]) / 5
        previous_long = sum(prices[-21:-1]) / 20

        if previous_short <= previous_long and short_sma > long_sma:
            signal = "BUY"

        elif previous_short >= previous_long and short_sma < long_sma:
            signal = "SELL"

        else:
            signal = "HOLD"

        return {
            "strategy": self.name,
            "signal": signal,
            "fast_sma": short_sma,
            "slow_sma": long_sma
        }
