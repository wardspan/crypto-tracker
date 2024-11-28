from app import db
from datetime import datetime

class NewsItem(db.Model):
    __tablename__ = 'news_items'
    
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    source = db.Column(db.String(100))
    url = db.Column(db.Text)
    published_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'coin_id': self.coin_id,
            'title': self.title,
            'content': self.content,
            'source': self.source,
            'url': self.url,
            'published_date': self.published_date.isoformat() if self.published_date else None,
            'created_at': self.created_at.isoformat()
        }
