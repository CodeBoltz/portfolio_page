from portfoliopage import db, login_manager
from sqlalchemy import ForeignKey
from flask_login import UserMixin

@login_manager.user_loader
def load_Admin(admin_id):
    return Admin.query.get(int(admin_id))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False, unique=True)

def __repr__(self):
    return f"Admin('{self.username}','{self.password}')"

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jp')
    image2 = db.Column(db.String(20), nullable=False)
    image3 = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(200), nullable=False)

def __repr__(self):
    return f"Post('{self.title}','{self.date}', '{self.description}', '{self.image}', '{self.image2}', '{self.image3}', '{self.link}' )"