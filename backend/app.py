import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, set_key
from datetime import datetime
from .script import get_following_and_follower

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

@app.route("/rescrape", methods=["POST"])
def rescrape():
    try:
        # Get old data from DB
        old_followers = {f.username for f in Follower.query.all()}
        old_following = {f.username for f in Following.query.all()}

        # Get new data
        new_following, new_followers = get_following_and_follower()

        # Clear existing DB entries
        Follower.query.delete()
        Following.query.delete()
        db.session.commit()

        # Save new data
        for username in new_followers:
            db.session.add(Follower(username=username, followed_at=datetime.now()))
        for username in new_following:
            db.session.add(Following(username=username, followed_at=datetime.now()))
        db.session.commit()

        # Compare old vs new
        new_unfollowers = sorted(old_followers - new_followers)


        return render_template(
            "rescrape_results.html",
            new_unfollowers=new_unfollowers,
        )
    except Exception as e:
        print("❌ Scraping failed:", e)
        return "Rescrape failed. Check your network or try again later.", 500

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Save credentials to .env
        set_key(ENV_PATH, "IG_USERNAME", username)
        set_key(ENV_PATH, "IG_PASSWORD", password)

        # Load them into the environment for this session
        load_dotenv(ENV_PATH)

        # Check if it's the first run (tables are empty)
        is_first_run = Follower.query.count() == 0 and Following.query.count() == 0

        if is_first_run:
            following_set, followers_set = get_following_and_follower()

            for user in followers_set:
                db.session.add(Follower(username=user, followed_at=datetime.now()))
            for user in following_set:
                db.session.add(Following(username=user, followed_at=datetime.now()))
            db.session.commit()

        return redirect(url_for("index"))

    return render_template("login.html")