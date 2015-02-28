from blog.app import app
from flask import session, render_template, flash
import hashlib

@app.route('/')
def hello():
  return render_template('home.html')

@app.route('/register', methods=["POST", "GET"])
def register():
  #if request.method == 'POST':
  #  username = request.form['username']
  #  password = request.form['password']
  #  hash_pass = hashlib.sha512(password).digest()
  #  u = User(username, hash_pass, False)
  #  u.save()
  #  flash('You successfully made an account.')
  #else:
  return render_template('register.html')