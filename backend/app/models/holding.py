from app import db
from datetime import datetime

class Holding(db.Model):
    __tablename__ = 'holdings'
    
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'), nullable=False)
    quantity = db.Column(db.Numeric, nullable=False)
    purchase_price = db.Column(db.Numeric, nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    broker_fees = db.Column(db.Numeric, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'coin_id': self.coin_id,
            'quantity': float(self.quantity),
            'purchase_price': float(self.purchase_price),
            'purchase_date': self.purchase_date.isoformat(),
            'broker_fees': float(self.broker_fees),
            'created_at': self.created_at.isoformat()
        }
