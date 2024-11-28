from app import db
from datetime import datetime

class Alert(db.Model):
    __tablename__ = 'alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'), nullable=False)
    price_threshold = db.Column(db.Numeric, nullable=False)
    condition = db.Column(db.String(10), nullable=False)  # 'above' or 'below'
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'coin_id': self.coin_id,
            'price_threshold': float(self.price_threshold),
            'condition': self.condition,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }
