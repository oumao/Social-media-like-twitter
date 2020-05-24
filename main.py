from flask import Flask,render_template,url_for
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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)    
app.run(debug=True)