from blog.models import Admin, Post
from blog.app import app
import re
import datetime


from flask import session, render_template, flash, request, redirect, url_for, session, abort
import hashlib

def slugify(text):
  delim = u'-'
  res = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
  result = []
  for word in res.split(text.lower()):
    word = word.encode('ascii')
    if word:
      result.append(word)
    return unicode(delim.join(result))


@app.route('/')
def home():
  post = False
  if session.get('logged_in'):
    post = True

  return render_template('home.html', post=post)

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('home'))


@app.route('/register', methods=["POST", "GET"])
def register():
  return abort(404)
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    us = Admin.objects(username=username)
    if us:
      flash("Username already taken.")
      return redirect(url_for('register'))

    hash_pass = hashlib.sha512(password).hexdigest()
    u = Admin(username, hash_pass)
    u.save()
    session['logged_in'] = True
    flash('You successfully made an account.')
    return redirect(url_for('home'))


  return render_template('register.html')

@app.route('/login', methods=["POST","GET"])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    u = Admin.objects.get(username=username)
    print "pass is %s" % (u.password)
    print "hash is %s" % (hashlib.sha512(password).hexdigest())
    if u.password == hashlib.sha512(password).hexdigest():
      session['logged_in'] = True
      flash("You successfully logged in.")
      return redirect(url_for('home'))
    else:
      flash("Wrong Pass")


  return render_template('login.html')

@app.route('/new', methods=["POST","GET"])
def new_post():
  if not session.get('logged_in'):
    return redirect(url_for('home'))

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    slug = slugify(title)
    p = Post(title, content, datetime.datetime.now, slug)
    p.save()
    flash('You created the post')
    return redirect(url_for('blog'))

  return render_template('new.html')

@app.route('/blog')
def blog():
  posts = Post.objects.all()
  return render_template('blog.html',posts=posts)


@app.route('/blog/<slug>')
def post(slug):
  post = Post.objects.get(slug=slug)
  return render_template('post.html',post=post)