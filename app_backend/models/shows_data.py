from routes import db   
from .venues_data import Venue

class Show(db.Model):
    __tablename__='Show'
    ID=db.Column(db.Integer , primary_key=True, autoincrement=True)
    img=db.Column(db.String)
    name=db.Column(db.String)
    tags=db.Column(db.String)
    date=db.Column(db.String)
    ticket=db.Column(db.Integer)
    rating=db.Column(db.Integer)
    tickets_booked = db.Column(db.Integer)
    tickets_available = db.Column(db.Integer)
    # venue = db.relationship(Venue, backref=db.backref('shows', lazy=True))
    venueID=db.Column(db.Integer, db.ForeignKey("Venue.ID"))