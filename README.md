# Crypto Portfolio Tracker

A full-stack web application for tracking cryptocurrency investments, built with React, Flask, and PostgreSQL.

## Features

- **Portfolio Dashboard**
  - Real-time portfolio value tracking
  - Profit/loss visualization
  - Individual coin performance graphs
  - 7-day historical data views

- **Portfolio Management**
  - Add/edit cryptocurrency holdings
  - Track purchase prices and dates
  - Record broker fees
  - Support for both coin symbols and full names

- **Price Alerts**
  - Set custom price alerts for held coins
  - Email notifications (coming soon)

- **News Aggregation**
  - 7-day news history for held coins
  - Filter news by specific coins
  - Aggregated news from multiple sources

## Tech Stack

### Frontend
- React
- Material-UI
- Recharts for data visualization
- React Router for navigation
- Axios for API requests

### Backend
- Flask
- SQLAlchemy
- PostgreSQL
- Flask-CORS

### External APIs
- CoinGecko
- CryptoCompare
- CoinFeeds
- Bitstamp
- CoinMarketCap

## Prerequisites

- Docker and Docker Compose
- Node.js (for local development)
- Python 3.11+ (for local development)
- PostgreSQL (for local development)

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/crypto-portfolio-tracker.git
```

2. Install dependencies:
```
npm install
```

3. Set up environment variables:
```
cp .env.example .env
```
```
DATABASE_URL=postgresql://user:password@db:5432/crypto_tracker
SECRET_KEY=your-secret-key-here
COINGECKO_API_KEY=your-coingecko-api-key
CRYPTOCOMPARE_API_KEY=your-cryptocompare-api-key
COINMARKETCAP_API_KEY=your-coinmarketcap-api-key
```

3. Build and start the containers:
```
docker-compose up --build
```

4. Access the application:
```
http://localhost:3000
```

## Development

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5001
- Database: localhost:5432

### API Endpoints

- `GET /api/portfolio` - Get portfolio summary
- `GET /api/portfolio/test` - Test database connection
- `GET /api/alerts` - Get price alerts
- `GET /api/news` - Get news items

## Project Structure

- `frontend/` - React application
- `backend/` - Flask API
- `db/` - Database schema and migrations
- `docker-compose.yml` - Docker Compose configuration
- `README.md` - This file

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- CoinGecko API
- CryptoCompare API
- Material-UI Team
- Flask Team

## Contact

Ward - [@wardspan](https://twitter.com/wardspan)