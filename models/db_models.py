"""DB model schemas module"""

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Stock(Base):
    """ORM of metadata about a stock"""

    __tablename__ = "stocks"
    ticker = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    industry = Column(String)


class Price(Base):
    """ORM of price data about a stock given t"""

    __tablename__ = "prices"
    ticker = Column(String, ForeignKey("stocks.ticker"), primary_key=True)
    ts = Column(TIMESTAMP(timezone=True), primary_key=True)
    open = Column(Numeric(10, 4), CheckConstraint("open >= 0"), nullable=False)
    close = Column(Numeric(10, 4), CheckConstraint("close >= 0"), nullable=False)
    high = Column(Numeric(10, 4), CheckConstraint("high >= 0"), nullable=False)
    low = Column(Numeric(10, 4), CheckConstraint("low >= 0"), nullable=False)
    volume = Column(Integer, CheckConstraint("volume >= 0"), nullable=False)


class Indicator(Base):
    """ORM of indicators data about a stock given t"""

    __tablename__ = "indicators"
    ticker = Column(String, primary_key=True)
    ts = Column(TIMESTAMP(timezone=True), primary_key=True)

    # Returns
    returns = Column(Numeric(12, 8))
    log_returns = Column(Numeric(12, 8))

    # Historic volatility
    hv_21d = Column(Numeric(12, 8), CheckConstraint("hv_21d >= 0"))
    hv_63d = Column(Numeric(12, 8), CheckConstraint("hv_63d >= 0"))
    hv_252d = Column(Numeric(12, 8), CheckConstraint("hv_252d >= 0"))

    # Beta (against market)
    beta_21d = Column(Numeric(12, 8))
    beta_63d = Column(Numeric(12, 8))
    beta_252d = Column(Numeric(12, 8))

    # Moving averages
    # Short-term
    ema_9d = Column(Numeric(10, 4), CheckConstraint("ema_9d >= 0"))
    ema_21d = Column(Numeric(10, 4), CheckConstraint("ema_21d >= 0"))
    sma_7d = Column(Numeric(10, 4), CheckConstraint("sma_7d >= 0"))
    sma_20d = Column(Numeric(10, 4), CheckConstraint("sma_20d >= 0"))
    # Medium-term
    ema_50d = Column(Numeric(10, 4), CheckConstraint("ema_50d >= 0"))
    sma_50d = Column(Numeric(10, 4), CheckConstraint("sma_50d >= 0"))
    ema_100d = Column(Numeric(10, 4), CheckConstraint("ema_100d >= 0"))
    # Long-term
    ema_200d = Column(Numeric(10, 4), CheckConstraint("ema_200d >= 0"))
    sma_200d = Column(Numeric(10, 4), CheckConstraint("sma_200d >= 0"))

    # Relative strength index (RSI)
    rsi_14d = Column(Numeric(5, 2), CheckConstraint("rsi_14d >= 0 AND rsi_14d <= 100"))
    rsi_21d = Column(Numeric(5, 2), CheckConstraint("rsi_21d >= 0 AND rsi_21d <= 100"))
    rsi_30d = Column(Numeric(5, 2), CheckConstraint("rsi_30d >= 0 AND rsi_30d <= 100"))
