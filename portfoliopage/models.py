from portfoliopage import db
from sqlalchemy import ForeignKey

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jp')

def __repr__(self):
    return f"Work('{self.title}','{self.date}', '{self.description}', '{self.image}' )"
