from live_updates import app
from flask import render_template, redirect
from author.form import RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to live updates"

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('author/register.html', form=form)
