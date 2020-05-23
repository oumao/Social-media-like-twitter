from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello!'

@app.route('/about')
def about():
    return '<h1>About page</h1>'


app.run(debug=True)