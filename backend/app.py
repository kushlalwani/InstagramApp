import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','templates'))


load_dotenv()

app = Flask(__name__, template_folder=template_dir)

# Force absolute DB path in root directory
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(basedir, 'instagram.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from backend.models import Follower, Following

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/followers')
def show_followers():
    followers = Follower.query.all()
    return render_template('followers.html', followers=followers)

@app.route('/following')
def show_following():
    following = Following.query.all()
    return render_template('following.html', following=following)

@app.route('/not-following-back')
def not_following_back():
    followers_set = {f.username for f in Follower.query.all()}
    following_set = {f.username for f in Following.query.all()}
    
    not_following_back = following_set - followers_set
    
    return render_template('followers.html', followers=not_following_back, title='Not Following Back')

@app.route('/dont-follow-back')
def dont_follow_back():
    followers_set = {f.username for f in Follower.query.all()}
    following_set = {f.username for f in Following.query.all()}
    
    dont_follow_back = followers_set - following_set
    
    return render_template('followers.html', followers=dont_follow_back, title='Dont Follow Back')
