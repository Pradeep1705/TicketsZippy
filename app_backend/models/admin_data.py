from routes import db

class Admin(db.Model):
    __tablename__='Admin'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String, unique=True)
    Email=db.Column(db.String, unique=True)
    Password=db.Column(db.String)