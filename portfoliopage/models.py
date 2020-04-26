from portfoliopage import db
from sqlalchemy import ForeignKey

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False,)
    description = db.Column(db.Text, nullable=False,)
    image = db.Column('WorkImage')

class WorkImage(db.Model):
    id = db.Column(db.Integer, ForeignKey('work.id'), primary_key=True)
    name = db.column(db.String(300))
    data = db.column(db.LargeBinary)

def __repr__(self):
    return f"Work('{self.title}','{self.date}', '{self.description}', '{self.image}' )"
