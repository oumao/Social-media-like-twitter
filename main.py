from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='c32bb949a4350a4f3ab9b179fc44f79d'
posts=[
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
    return render_template('home.html',posts=posts)

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
            flash(f"Unsuccessfull log in!!",'success')
    return render_template('login.html',title='Login', form=form)    
app.run(debug=True)