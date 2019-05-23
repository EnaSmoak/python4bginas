from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    user = {'username' : 'Gifty'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
