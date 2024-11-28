import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/crypto_tracker')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    COINGECKO_API_KEY = os.getenv('COINGECKO_API_KEY')
    CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE_API_KEY')
    COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY') 