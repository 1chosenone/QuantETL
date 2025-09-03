-- Timescaledb extension for better time-series capabilities
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- Hypertable for stock prices
SELECT create_hypertable('prices', 'ts');

-- Hypertable for stock indicators
SELECT create_hypertable('indicators', 'ts');