from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='c32bb949a4350a4f3ab9b179fc44f79d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/twitter'
db = SQLAlchemy(app)
login_manager=LoginManager(app)

from twitterblog import routes