
class MarketIntelligence:

    def calculate_sma(self, prices, period):

        if period <= 0:
            raise ValueError("Period must be positive")

        if len(prices) < period:
            return None

        selected = prices[-period:]

        return sum(selected) / period

    def analyze_trend(self, prices):

        if len(prices) < 20:
            return "INSUFFICIENT_DATA"

        short_sma = self.calculate_sma(prices, 5)
        long_sma = self.calculate_sma(prices, 20)

        if short_sma > long_sma:
            return "BULLISH"

        elif short_sma < long_sma:
            return "BEARISH"

        return "SIDEWAYS"

    def analyze_market(self, prices):

        trend = self.analyze_trend(prices)

        return {
            "trend": trend,
            "last_price": prices[-1] if prices else None,
            "data_points": len(prices)
        }
