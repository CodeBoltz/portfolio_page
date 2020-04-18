from app import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False,)
    image_file = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False, )

    def __repr__(self):
        return f"Work('{self.title}','{self.date}', '{self.image_file}', '{self.description}')"

