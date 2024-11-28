CREATE TABLE IF NOT EXISTS coins (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS holdings (
    id SERIAL PRIMARY KEY,
    coin_id INTEGER REFERENCES coins(id),
    quantity DECIMAL NOT NULL,
    purchase_price DECIMAL NOT NULL,
    purchase_date TIMESTAMP NOT NULL,
    broker_fees DECIMAL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS price_history (
    id SERIAL PRIMARY KEY,
    coin_id INTEGER REFERENCES coins(id),
    price DECIMAL NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    coin_id INTEGER REFERENCES coins(id),
    price_threshold DECIMAL NOT NULL,
    condition VARCHAR(10) NOT NULL, -- 'above' or 'below'
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS news_items (
    id SERIAL PRIMARY KEY,
    coin_id INTEGER REFERENCES coins(id),
    title TEXT NOT NULL,
    content TEXT,
    source VARCHAR(100),
    url TEXT,
    published_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 