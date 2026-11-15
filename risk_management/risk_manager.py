
class RiskManager:

    def __init__(
        self,
        risk_per_trade=0.01,
        max_daily_loss=0.03
    ):
        self.risk_per_trade = risk_per_trade
        self.max_daily_loss = max_daily_loss

        if not 0 < risk_per_trade <= 0.05:
            raise ValueError("Invalid risk percentage")

        if not 0 < max_daily_loss <= 0.20:
            raise ValueError("Invalid daily loss limit")

    def calculate_position_size(
        self,
        balance,
        entry_price,
        stop_loss
    ):

        if balance <= 0:
            raise ValueError("Invalid balance")

        distance = abs(entry_price - stop_loss)

        if distance <= 0:
            raise ValueError("Invalid stop loss")

        risk_amount = balance * self.risk_per_trade

        position_size = risk_amount / distance

        return {
            "risk_amount": risk_amount,
            "position_size": position_size
        }

    def check_daily_loss(
        self,
        starting_balance,
        current_balance
    ):

        if starting_balance <= 0:
            raise ValueError("Invalid starting balance")

        loss = starting_balance - current_balance

        max_loss = (
            starting_balance * self.max_daily_loss
        )

        if loss >= max_loss:
            return False

        return True
