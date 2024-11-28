from flask import Blueprint, jsonify, current_app
from app import db
from app.models import Coin
from sqlalchemy import text

bp = Blueprint('portfolio', __name__)

@bp.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify({
        'message': 'Portfolio endpoint working'
    })

@bp.route('/api/portfolio/test', methods=['GET'])
def test_connection():
    try:
        # Test database connection with proper text() wrapper
        db.session.execute(text('SELECT 1'))
        
        # Try to create a test coin
        test_coin = Coin(
            symbol='BTC',
            name='Bitcoin'
        )
        db.session.add(test_coin)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Database connection successful',
            'test_coin': test_coin.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
