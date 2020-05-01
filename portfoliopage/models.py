from portfoliopage import db
from sqlalchemy import ForeignKey

class Work(db.Model):
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jp')
    image2 = db.Column(db.String(20))
    image3 = db.Column(db.String(20))
    link = db.Column(db.String(200), nullable=False)


def __repr__(self):
    return f"Work('{self.title}','{self.date}', '{self.description}', '{self.image}' )"
