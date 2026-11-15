
class PaperBroker:

    def __init__(self):
        self.balance = 10000.0
        self.open_positions = []
        self.trade_history = []

    def execute_order(self, symbol, signal, volume):

        if signal not in ["BUY", "SELL"]:
            return {
                "status": "REJECTED",
                "reason": "Invalid signal"
            }

        if volume <= 0:
            return {
                "status": "REJECTED",
                "reason": "Invalid volume"
            }

        order = {
            "symbol": symbol,
            "type": signal,
            "volume": volume,
            "status": "SIMULATED"
        }

        self.trade_history.append(order)

        return order

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.trade_history
