from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '43d64d908f55fa813433db5cee72cb05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['IMAGE_UPLOADS'] = '/Users/Greg/Downloads/01_Code/SE_Foundation/portfolio_page/portfoliopage/static/uploads'
db = SQLAlchemy(app)

from portfoliopage import routes