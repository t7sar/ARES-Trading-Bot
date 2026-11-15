from config.settings import settings
from market_intelligence.analysis import MarketIntelligence
from strategies.base_strategy import BaseStrategy
from risk_management.risk_manager import RiskManager
from execution.broker_interface import PaperBroker


def run_ares():
    print("=" * 45)
    print("ARES TRADING SYSTEM")
    print("=" * 45)

    prices = [
        1.1000, 1.1010, 1.1020, 1.1015,
        1.1030, 1.1040, 1.1050, 1.1060,
        1.1070, 1.1080, 1.1090, 1.1100,
        1.1110, 1.1120, 1.1130, 1.1140,
        1.1150, 1.1160, 1.1170, 1.1180,
        1.1190, 1.1200
    ]

    intelligence = MarketIntelligence()
    strategy = BaseStrategy()

    risk = RiskManager(
        risk_per_trade=settings.RISK_PER_TRADE,
        max_daily_loss=settings.MAX_DAILY_LOSS
    )

    broker = PaperBroker()

    market = intelligence.analyze_market(prices)
    signal = strategy.generate_signal(prices)

    print("\nMARKET ANALYSIS:")
    print(market)

    print("\nTRADING SIGNAL:")
    print(signal)

    print("\nRISK SETTINGS:")
    print("Risk per trade:", risk.risk_per_trade)

    if signal["signal"] in ["BUY", "SELL"]:
        result = broker.execute_order(
            settings.SYMBOL,
            signal["signal"],
            0.01
        )
        print("\nPAPER EXECUTION:")
        print(result)
    else:
        print("\nNO TRADE - WAITING")

    print("\nARES SYSTEM FINISHED")


if __name__ == "__main__":
    run_ares()
