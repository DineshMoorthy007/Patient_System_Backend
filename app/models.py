from datetime import datetime
from . import db

class Patient(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)  # type: ignore[attr-defined]
    name = db.Column(db.String(100), nullable=False)  # type: ignore[attr-defined]
    age = db.Column(db.Integer, nullable=False)  # type: ignore[attr-defined]
    condition = db.Column(db.String(200), nullable=False)  # type: ignore[attr-defined]
    priority = db.Column(db.Integer, nullable=False)  # type: ignore[attr-defined]
    arrival_time = db.Column(db.DateTime, default=datetime.utcnow)  # type: ignore[attr-defined]
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'condition': self.condition,
            'priority': self.priority,
            'arrival_time': self.arrival_time.isoformat()
        }