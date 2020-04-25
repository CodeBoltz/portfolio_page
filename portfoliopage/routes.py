from flask import render_template, url_for, flash, redirect, request
from portfoliopage import app
from portfoliopage.forms import DesignForm
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
@app.route('/design_submit', methods=['GET', 'POST'])
def design_submit():
    form = DesignForm()
    return render_template('design_submit.html', title='Submit Design', form=form)