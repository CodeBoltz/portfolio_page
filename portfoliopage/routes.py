from flask import render_template, url_for, flash, redirect
from portfoliopage import app
from portfoliopage.forms import RegistrationForm, LoginForm
from portfoliopage.models import Work


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