from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from blog import views
from author import views
