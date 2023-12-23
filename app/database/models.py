from . import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depth = db.Column(db.Float, nullable=False, unique=True)
    image_data = db.Column(db.LargeBinary, nullable=False)
