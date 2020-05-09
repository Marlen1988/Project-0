from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/LogIn')
def LogIn():
    return render_template('LogIn.html')
@app.route('/SignUp')
def SignUp():
    return render_template('SignUp.html')
@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')
