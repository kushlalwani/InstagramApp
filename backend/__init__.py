from app import app, db
from models import Follower

with app.app_context():
    db.create_all()
    print("✅ Database tables created.")