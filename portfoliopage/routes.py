from flask import render_template, url_for, flash, redirect, request
from portfoliopage import app, db
from portfoliopage.forms import DesignForm
from portfoliopage.models import Work
import os

# routes for main page
@app.route('/')
def index():
    return render_template('index.html', title="Home")

# routes for sub pages
@app.route('/profile')
def profile():
    return render_template('profile.html', title="Profile")

@app.route('/work')
def work():
    return render_template('work.html', title="Work")

@app.route('/ping_work')
def ping_work():
    return render_template('ping_work.html', title="Test work page")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

# route for forms
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = DesignForm()
    if form.validate_on_submit():
        if request.files:
            image = request.files['image']
            print(image)
            image.save( os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
        work = Work(title=form.title.data, date=form.date.data, description=form.description.data)
        db.session.add(work)
        db.session.commit()
        flash(f'Your design work has been submited!', 'success')
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit Design', form=form)


