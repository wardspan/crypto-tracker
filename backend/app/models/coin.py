from app import db
from datetime import datetime

class Coin(db.Model):
    __tablename__ = 'coins'
    
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    holdings = db.relationship('Holding', backref='coin', lazy=True)
    price_history = db.relationship('PriceHistory', backref='coin', lazy=True)
    alerts = db.relationship('Alert', backref='coin', lazy=True)
    news_items = db.relationship('NewsItem', backref='coin', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'name': self.name,
            'created_at': self.created_at.isoformat()
        }
