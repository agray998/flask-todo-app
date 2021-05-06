from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('secretkey')

db = SQLAlchemy(app)

class AddTask(FlaskForm):
    task_name = StringField('Task name')
    task_desc = StringField('Description')
    task_stat = StringField('Status')
    submit = SubmitField('Add Task')

class UpdateTask(FlaskForm):
    task_name = StringField('Task name')
    task_desc = StringField('Description')
    task_stat = StringField('Status')
    submit = SubmitField('Update Task')

from application import routes
