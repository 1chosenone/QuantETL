-- Table containing metadata about stocks
CREATE TABLE IF NOT EXISTS stocks (
    ticker TEXT PRIMARY KEY,
    company_name VARCHAR(64),
    sector VARCHAR(64),
    industry VARCHAR(64)
);

-- Table containing data about stock prices
CREATE TABLE IF NOT EXISTS prices(
    ticker TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    open NUMERIC(10,4) NOT NULL CHECK (open >= 0),
    high NUMERIC(10,4) NOT NULL CHECK (high >= 0),
    low NUMERIC(10,4) NOT NULL CHECK (low >= 0),
    close NUMERIC(10,4) NOT NULL CHECK (close >= 0),
    volume BIGINT NOT NULL CHECK (volume >= 0),
    PRIMARY KEY(ticker, ts),
    FOREIGN KEY(ticker) REFERENCES stocks(ticker) ON DELETE CASCADE
);

-- Speeds up queries that filter or join on the 'ticker' column in the 'prices' table
CREATE INDEX idx_prices_ticker ON prices(ticker); 

-- Table containing data about stock prices
CREATE TABLE IF NOT EXISTS indicators(
    ticker TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,

    -- Returns
    returns NUMERIC(12,8),
    log_returns NUMERIC(12,8),

    -- Historical volatility
    hv_21d NUMERIC(12,8) CHECK (hv_21d >= 0),
    hv_63d NUMERIC(12,8) CHECK (hv_63d >= 0),
    hv_252d NUMERIC(12,8) CHECK (hv_252d >= 0),

    -- Beta (against market)
    beta_21d NUMERIC(12,8),
    beta_63d NUMERIC(12,8),
    beta_252d NUMERIC(12,8),

    -- Moving averages
    -- Short-term
    ema_9d NUMERIC(10,4) CHECK (ema_9d >= 0),
    ema_21d NUMERIC(10,4) CHECK (ema_21d >= 0),
    sma_7d NUMERIC(10,4) CHECK (sma_7d >= 0),
    sma_20d NUMERIC(10,4) CHECK (sma_20d >= 0),
    -- Medium-term
    ema_50d NUMERIC(10,4) CHECK (ema_50d >= 0),
    sma_50d NUMERIC(10,4) CHECK (sma_50d >= 0),
    ema_100d NUMERIC(10,4) CHECK (ema_100d >= 0),
    -- Long-term
    ema_200d NUMERIC(10,4) CHECK (ema_200d >= 0),
    sma_200d NUMERIC(10,4) CHECK (sma_200d >= 0),

    -- Relative strength index (RSI)
    rsi_14d NUMERIC(5, 2) CHECK (rsi_14d >= 0 AND rsi_14d <= 100),
    rsi_21d NUMERIC(5, 2) CHECK (rsi_21d >= 0 AND rsi_21d <= 100),
    rsi_30d NUMERIC(5, 2) CHECK (rsi_30d >= 0 AND rsi_30d <= 100),

    PRIMARY KEY(ticker, ts),
    FOREIGN KEY(ticker) REFERENCES stocks(ticker) ON DELETE CASCADE
);
