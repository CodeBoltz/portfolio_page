import os
from flask import render_template, url_for, flash, redirect, request
from portfoliopage import app, db
from portfoliopage.forms import DesignForm
from portfoliopage.models import Work

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
            image2 = request.files['image2']
            image3 = request.files['image3']
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            image2.save(os.path.join(app.config['IMAGE_UPLOADS'], image2.filename))
            image3.save(os.path.join(app.config['IMAGE_UPLOADS'], image3.filename)) 
            url = image.filename
            url2 = image2.filename
            url3 = image3.filename
        work = Work(title=form.title.data, date=form.date.data, description=form.description.data, image=url, image2=url2, image3=url3, link=form.link.data)
        db.session.add(work)
        db.session.commit()
        flash(f'Your design work has been submited!', 'success')
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit Design', form=form)

#route for test work page template
'''
@app.route('/work_template')
def work_template():
    data = Work.query
    return render_template('work_template.html', data=list, image=image)
'''
#route for all work pages 

@app.route('/work_template')
def detail():
    work = Work.query.filter_by(id='2')
    return render_template('work_template.html', work=work)


