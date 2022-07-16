from builtins import classmethod, len, print
from cmath import exp
import email
import flask
from flask import Flask, redirect, render_template, abort, request, request_started, url_for, send_from_directory,flash 
from flask_login import LoginManager, current_user, login_user, login_required, logout_user 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField,TextAreaField,validators 
# from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename 
from werkzeug.exceptions import RequestEntityTooLarge
from urllib.parse import urlparse, urljoin
import database
import json
import os  
import PIL.Image as Image



app = Flask(__name__, template_folder='templates', static_url_path = '/static')
app.config['UPLOAD_DIRECTORY'] = 'static/upload/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16mb
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']
login_manager = LoginManager()
# auth = HTTPBasicAuth()
login_manager.init_app(app)
db = database.ProductsDatabase()

 
app.secret_key = b'jkrg,fjfvklsvsjkhvbjknvjknvhjbsfbshvbhjv09886-3'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User():

    def __init__(self, id):
        self.id = id

    def is_authenticated(self):
        return True

    def is_active():
        return True

    def is_anonymous():
        return False

    def get_id(self):
        return self.id

    @classmethod 
    def get(cls,id):
       return User(id)

class LoginForm(FlaskForm):
 user = StringField('User')
 password = PasswordField('Password')
 submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
 user = StringField('User',[validators.Length(min=4, max=25)])
 email = StringField('Email Address', [validators.Length(min=6, max=35)])
 password = PasswordField('Password')
 submit = SubmitField('Submit')

class Payment(FlaskForm):
 name = StringField('Name')
 email = StringField('Email Address', [validators.Length(min=6, max=35)])
 address = StringField('Address')
 city = StringField('City')
 state = StringField('State')
 zip = StringField('Zip')
 cardh = StringField('Cardh')
 creditcardn = StringField('Creditcardn')
 expmon = StringField('Expmon')
 expyear = StringField('Expyear')
 cvc = StringField('CVC')
 submit = SubmitField('Submit')







def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http','https') and \
           ref_url.netloc == test_url.netloc



@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if request.method=='POST':
        user=request.form['user']
        password=request.form['password']
        user = db.get_id_by_user(user)[0] 
        if user and  check_password_hash(user['Password'], password):

            user = User(user['Id'])

            login_user(user)

            return redirect("payment")
        else:
            flash("Username and Password Mismatch","danger")
    return render_template('index.html')

# def register_login(request):
#     if "register" in request.method == "POST": 

#       if "login" in request.method == "POST":
#        return render_template('home.html')   



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
            try:
                    user=request.form['user']
                    email=request.form['email']
                    password=generate_password_hash(request.form['password'])

                    db.create_user(user,email,password)
            
                    user_id = db.get_id_by_user(user)[0]
                    
                    user = User(user_id['Id'])

                    login_user(user)

                    flask.flash('Logged in successfully.')

                    # next = flask.request.args.get('next')
                    # is_safe_url should check if the url is safe for redirects.
                    # See http://flask.pocoo.org/snippets/62/ for an example.
            except:
                flash("Error in Insert Operation","danger")
            finally:
                return redirect(url_for("payment"))
    
    return render_template('index.html') 
    


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shopping')
def shopping():

    return render_template("shopping.html")

@app.route('/sproduct')
def sproduct():

    return render_template("sproduct.html")

@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():

    return render_template("payment.html")

if __name__ == '__main__':
    app.run(debug=True)



