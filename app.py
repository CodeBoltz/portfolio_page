from flask import Flask, jsonify, send_file
from flask_cors import CORS
from flask import render_template


app = Flask(__name__)
# enable the api to be accessed by frontend running on localhost
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

# define what to do when the user navigates to "/"
# this serves a static html file. 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/ping_work')
def ping_work():
    return render_template('ping_work.html')

# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__':  
    app.debug = True
    app.run() 