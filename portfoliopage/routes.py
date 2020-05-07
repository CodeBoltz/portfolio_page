import os
from flask import render_template, url_for, flash, redirect, request
from portfoliopage import app, db, bcrypt
from portfoliopage.forms import DesignForm, LoginForm, RegistrationForm
from portfoliopage.models import Work, Admin
from flask_login import login_user, current_user, logout_user, login_required

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
    work = Work.query.all()
    return render_template('work.html', title="Work", work=work)

@app.route('/ping_work')
def ping_work():
    return render_template('ping_work.html', title="Test work page")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

'''
!!! THIS IS COMMENTED OUT SO NOBODY ELSE CAN REGISTER TO MY PAGE !!!
# route for registration form
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(username=form.username.data, password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form) '''

# route for login form
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# route for logout 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

# route for submit form
@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = DesignForm()
    if form.validate_on_submit():
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            url = image.filename
            try:
                image2 = request.files['image2']
                image2.save(os.path.join(app.config['IMAGE_UPLOADS'], image2.filename))
                url2 = image2.filename
            except:
                url2 = ''
            try:
                image3 = request.files['image3']
                image3.save(os.path.join(app.config['IMAGE_UPLOADS'], image3.filename)) 
                url3 = image3.filename
            except:
                url3 = ''
        work = Work(title=form.title.data, date=form.date.data, description=form.description.data, image=url, image2=url2, image3=url3, link=form.link.data)
        db.session.add(work)
        db.session.commit()
        flash(f'Your design work has been submited!', 'success')
        return redirect(url_for('work'))
    return render_template('submit.html', title='Submit Design', form=form)

#route for all work pages 
@app.route('/work/<string:work_id>')
def post(work_id):
    work = Work.query.get_or_404(work_id)
    return render_template('post.html', title=work.title, work=work)

#route to update post
@app.route('/work/<string:work_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(work_id):
    work = Work.query.get_or_404(work_id)
    form = DesignForm()
    if form.validate_on_submit():
        work.title = form.title.data
        work.date = form.date.data
        work.description = form.description.data
        work.image = form.image.data
        work.image2 = form.image2.data
        work.image3 = form.image3.data
        work.link = form.link.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('work', work_id=work.id))
    elif request.method == 'GET':
        form.title.data = work.title 
        form.date.data = work.date
        form.description.data = work.description 
        form.image.data = work.image 
        form.image2.data = work.image2 
        form.image3.data = work.image3  
        form.link.data = work.link  
    return render_template('submit.html', title='Update Post', form=form, work=work, legend='Update Post')

#route to delte post
@app.route('/work/<string:work_id>/delete', methods=['POST'])
@login_required
def delete_post(work_id):
    work = Work.query.get_or_404(work_id)
    db.session.delete(work)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('work'))