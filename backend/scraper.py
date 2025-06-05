from app import app, db
from models import Follower, Following
from script import get_following_and_follower 
from datetime import datetime
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Call your function that handles everything internally
following_set, followers_set = get_following_and_follower()
print("scraped usernames")

# Save new followers to the database
with app.app_context():
    for username in followers_set:
        if not Follower.query.filter_by(username=username).first():
            db.session.add(Follower(username=username, followed_at=datetime.now()))
    for username in following_set:
        if not Following.query.filter_by(username=username).first():
            db.session.add(Following(username=username, followed_at=datetime.now()))
    db.session.commit()

print("✅ Saved followers to DB.")

# Comparison logic
not_following_back = following_set - followers_set
unfollowers = followers_set - following_set
mutuals = followers_set.intersection(following_set)


print("\n🚫 Not Following Back:")
for user in sorted(not_following_back):
    print(f"- {user}")

print("\nYou Don't Follow Back")
for user in sorted(unfollowers):
    print(f"- {user}")

print("\nMutuals")
for user in sorted(mutuals):
    print(f"- {user}")