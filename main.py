from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime
pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SECRET_KEY']='c32bb949a4350a4f3ab9b179fc44f79d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/twitter'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(120),nullable=False)
    image = db.Column(db.String(80),nullable=False,default='default.jpg')
    posts=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username},{self.email},{self.image}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



post_demo=[
      {
          'title':'blog',
          'author':'Milton',
          'content':'This is first post',
          'date'   :'May 23,2020'
      },
      {
    'title':'blog 2',
    'author':'Milton',
    'content':'This is second post',
    'date'   :'May 24,2020'
}
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=post_demo)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!!",'success')#eikhane flash ar 2nd parameter ta hossce category ar flash bootstrap class support kore tai eikhane bootstrap ar success class diya hoise jate success ar color show kore.eikhane waring,error class o diya jaito but eikhane jehtu condition holo success ar tai success diya hoise
    
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():#form submit or validate ki na? eita ei function check kore true hole kaj kore
        if form.email.data=='admin@gmail.com' and form.password.data=='12345':
            flash(f"You have been logged in!!",'success')
            return redirect(url_for('home'))
        else:
            flash(f"Unsuccessfull log in!! Please check username or password",'danger')
    return render_template('login.html',title='Login', form=form)    
app.run(debug=True)