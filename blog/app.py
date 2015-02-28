from flask.ext.mongoengine import MongoEngine
from flask import Flask


app = Flask('blog')

app.config["MONGODB_SETTINGS"] = {'DB': "FlaskBlog"}

db = MongoEngine(app)


from blog import controllers