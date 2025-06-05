from .app import db

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    followed_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Follower {self.username}>"
    
class Following(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    followed_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Following {self.username}>"