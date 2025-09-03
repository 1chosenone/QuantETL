from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_models import Base, Stock, Price, Indicator  # Import your models


# Create an in-memory SQLite DB for testing
@pytest.fixture(scope="module")
def test_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_stock_model(test_session):
    stock = Stock(
        ticker="AAPL",
        company_name="Apple Inc.",
        sector="Technology",
        industry="Consumer Electronics",
    )
    test_session.add(stock)
    test_session.commit()

    result = test_session.query(Stock).filter_by(ticker="AAPL").first()
    assert result.company_name == "Apple Inc."
    assert result.sector == "Technology"
    assert result.industry == "Consumer Electronics"


def test_price_model(test_session):
    price = Price(
        ticker="AAPL",
        ts=datetime(2023, 9, 1, 14, 30, 0),
        open=175.00,
        close=177.25,
        high=178.00,
        low=174.50,
        volume=12000000,
    )
    test_session.add(price)
    test_session.commit()

    result = test_session.query(Price).filter_by(ticker="AAPL").first()
    assert result.ts == datetime(2023, 9, 1, 14, 30, 0)
    assert result.open == 175.00
    assert result.close == 177.25
    assert result.high == 178.00
    assert result.low == 174.50
    assert result.volume == 12000000


def test_indicator_model(test_session):
    indicator = Indicator(
        ticker="AAPL",
        ts=datetime(2023, 9, 1, 14, 30, 0),
        returns=0.0012,
        log_returns=0.0011,
        hv_21d=0.25,
        beta_21d=1.12,
        ema_9d=175.42,
        rsi_14d=55.23,
    )
    test_session.add(indicator)
    test_session.commit()

    result = test_session.query(Indicator).filter_by(ticker="AAPL").first()
    assert result.ts == datetime(2023, 9, 1, 14, 30, 0)
    assert float(result.returns) == 0.0012
    assert float(result.log_returns) == 0.0011
    assert result.hv_21d == 0.25
    assert float(result.beta_21d) == 1.12
    assert float(result.ema_9d) == 175.42
    assert float(result.rsi_14d) == 55.23
