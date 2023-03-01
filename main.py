from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      if 'register' in request.form:
        return redirect(url_for('register'))
      elif 'login' in request.form:
        return 'acc page after login'
    return render_template('index.html') 

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    user = request.form['user1']
    pas = request.form['pas1']
    return f'Your username is {user} and password is {pas}. Return to GianBook to login'
  elif request.method == 'GET':
    return render_template('register.html')

@app.route('/account')
def account():
  return 'hi'
app.run(host='0.0.0.0', port=81)
