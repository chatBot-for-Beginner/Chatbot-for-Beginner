from server import db

class corpus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)