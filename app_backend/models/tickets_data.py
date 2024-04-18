from routes import db


class Ticket(db.Model):
    __tablename__='Ticket'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String)
    venueName = db.Column(db.String)
    showName = db.Column(db.String)
    date = db.Column(db.String)
    seats = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img = db.Column(db.String)
    