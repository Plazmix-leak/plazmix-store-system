from app import db


class Aggregator(db.Model):
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, unique=True)

    name = db.Column(db.String(100), nullable=False, unique=True)
    title = db.Column(db.String(200), nullable=False)

    notification_url = db.Column(db.String(500), nullable=True)
    
    payments = db.relationship("Payment", back_populates="aggregator", cascade="all, delete-orphan")
