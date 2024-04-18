from routes import db


class Venue(db.Model):
    __tablename__='Venue'
    ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    img=db.Column(db.String)
    name=db.Column(db.String)
    place=db.Column(db.String)
    capacity=db.Column(db.Integer)
    rating=db.Column(db.Integer)
    # show=db.relationship("Show")