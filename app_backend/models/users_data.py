from routes import db

class User(db.Model):
    __tablename__='User'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String, unique=True)
    Email=db.Column(db.String, unique=True)
    Password=db.Column(db.String)

class loggedIn(db.Model):
    __tablename__ = 'loggedIn'
    userName = db.Column(db.String, primary_key=True)
    time = db.Column(db.Integer)