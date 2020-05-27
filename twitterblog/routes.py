from flask import render_template,url_for,flash,redirect
from twitterblog import app,db,bcrypt
from twitterblog.form import RegistrationForm,LoginForm
from twitterblog.models import User,Post

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
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(" Your account has been created successfully!! You are now able to login",'success')#eikhane flash ar 2nd parameter ta hossce category ar flash bootstrap class support kore tai eikhane bootstrap ar success class diya hoise jate success ar color show kore.eikhane waring,error class o diya jaito but eikhane jehtu condition holo success ar tai success diya hoise
    
        return redirect(url_for('login'))
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

