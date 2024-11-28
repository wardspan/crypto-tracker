from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    # Basic route for testing
    @app.route('/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'message': 'Flask API is running'
        })
    
    with app.app_context():
        # Import models
        from app.models import Coin, Holding, PriceHistory, Alert, NewsItem
        
        # Create tables
        db.create_all()
        
        # Import and register blueprints
        from app.routes import portfolio, alerts, news
        app.register_blueprint(portfolio.bp)
        app.register_blueprint(alerts.bp)
        app.register_blueprint(news.bp)
        
        return app 