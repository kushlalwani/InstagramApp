import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Force absolute DB path in root directory
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(basedir, 'instagram.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)