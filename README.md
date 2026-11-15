
"""
ARES Trading Bot
Main application entry point.
Development mode only.
"""

from config.settings import settings


def start_ares():
    print("=" * 40)
    print("ARES TRADING BOT")
    print("=" * 40)

    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"Symbol: {settings.SYMBOL}")
    print(f"Timeframe: {settings.TIMEFRAME}")

    print("ARES system initialized.")
    print("Trading mode: PAPER ONLY")
    print("No live broker connection.")


if __name__ == "__main__":
    start_ares()
