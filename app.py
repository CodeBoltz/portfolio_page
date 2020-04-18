from flask import Flask, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '43d64d908f55fa813433db5cee72cb05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False,)
    image_file = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False, )

    def __repr__(self):
        return f"Work('{self.title}','{self.date}', '{self.image_file}', '{self.description}')"

# define what to do when the user navigates to "/"
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/profile')
def profile():
    return render_template('profile.html', title="Profile")

@app.route('/work')
def work():
    return render_template('work.html', title="Work")

@app.route('/ping_work')
def ping_work():
    return render_template('ping_work.html')

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

# route for forms
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__':  
    app.debug = True
    app.run() 