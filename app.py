from flask import Flask, jsonify, send_file
from flask_cors import CORS
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# test data for flask template
posts = [
    {
        'headlin': 'Ping',
        'when': 'September 2018, Berlin',
        'what': 'In my first semester as an Interaction Design student, my team and I created the app “Ping”. Ping is a social network of explorers and people who want to get out of their comfort zone and meet new people. To demonstrate our idea I created mock–ups, landing page, clickable prototype, and a unique logo.',
        'categories': 'First post content',
        'find it here': 'April 20, 2018'
    }
]

app = Flask(__name__)
# secruity messure
app.config['SECRET_KEY'] = '43d64d908f55fa813433db5cee72cb05'
# enable the api to be accessed by frontend running on localhost
#CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

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
@app.route('/register')
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