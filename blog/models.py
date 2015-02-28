from blog.app import db
import datetime

class Post(db.Document):
  title = db.StringField(max_length=100,required=True)
  content = db.StringField(max_length=1000, required=True)
  pub_date = db.DateTimeField(default=datetime.datetime.now, required=True)
  slug = db.StringField(max_length=100,required=True)

  meta = {
    'ordering': ['-pub_date']
  }

class User(db.Document):
  username = db.StringField(max_length=100)
  password = db.StringField(max_length=100)
  admin = db.BooleanField()
