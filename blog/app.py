from flask.ext.mongoengine import MongoEngine
from flask import Flask



app = Flask('blog')

app.config["MONGODB_SETTINGS"] = {'DB': "PythonBlogg"}
app.debug = True
app.secret_key = 'abcd'
db = MongoEngine(app)


from blog import controllers
from blog.models import Post, Admin