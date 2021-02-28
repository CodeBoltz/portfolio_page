from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '43d64d908f55fa813433db5cee72cb05'

# all configs for Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# all configs for where images are stored when uploaded
app.config['IMAGE_UPLOADS'] = '/Users/Greg/Downloads/01_Code/SE_Foundation/portfolio_page/portfoliopage/static/uploads'

# all configs for flask mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_MAX_EMAILS'] = 1
#app.config['MAIL_SUPRESS_SEND'] = False
#app.config['MAIL_ASCII_ATTECHMENTS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

import routes