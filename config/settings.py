
import os


class Settings:
    ENVIRONMENT = os.getenv("ARES_ENV", "DEVELOPMENT")
    SYMBOL = os.getenv("ARES_SYMBOL", "EURUSD")
    TIMEFRAME = os.getenv("ARES_TIMEFRAME", "M15")

    STARTING_BALANCE = 10000.0
    RISK_PER_TRADE = 0.01
    MAX_DAILY_LOSS = 0.03


settings = Settings()
