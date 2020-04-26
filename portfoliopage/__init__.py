from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_uploads import UploadSet, configure_uploads, IMAGES

#photos = UploadSet ('photos', IMAGES)

app = Flask(__name__)
app.config['SECRET_KEY'] = '43d64d908f55fa813433db5cee72cb05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['UPLOAD_PHOTOS_DEST'] = "/static/uploads"
#configure_uploads(app, photos)
db = SQLAlchemy(app)

from portfoliopage import routes