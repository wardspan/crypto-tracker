from app import db
from datetime import datetime

class PriceHistory(db.Model):
    __tablename__ = 'price_history'
    
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'coin_id': self.coin_id,
            'price': float(self.price),
            'timestamp': self.timestamp.isoformat(),
            'created_at': self.created_at.isoformat()
        }
