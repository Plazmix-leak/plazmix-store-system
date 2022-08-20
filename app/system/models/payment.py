import datetime
import uuid

from sqlalchemy_utils import UUIDType

from app import db


class Payment(db.Model):
    uuid = db.Column(UUIDType, primary_key=True, unique=True, default=uuid.uuid4)
    aggregator = db.relationship("Aggregator", back_populates="payments", uselist=False)
    amount = db.Column(db.Float, default=0.0)
    status = db.Column(db.Enum("CREATE", "WAIT", "PAID", "FAIL", "CLOSE"), default="CREATE")

    # Technical Information
    create_time = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    final_time = db.Column(db.DateTime, nullable=True)
    aggregator_payload = db.Column(db.JSON, nullable=True)
