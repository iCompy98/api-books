from flask import Flask
from project import views

app = Flask(__name__)

app.register_blueprint(views.routes)
