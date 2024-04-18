from routes import app
from flask import Flask, request,jsonify
from models.admin_data import *
from models.venues_data import *
from models.shows_data import *
from tokensJWT import *



@app.route("/adminLogin", methods=[ "POST"])
def admin_login():
    
    username= request.json['username']
    password= request.json['password']
    try:
        admin = Admin.query.filter_by(UserName = username).one()
        if not admin:
            return jsonify({'message':'Invalid'})
        if admin.Password == password:
            token = genrate_token(username)
            return jsonify({'token':token, 'userType':'admin'})
        else:
            return jsonify({'message':'Invalid'})
    except:
        return jsonify({'message':'Invalid'})

@app.route("/export/<ID>/", methods=["GET"])
@jwt_required
def export(ID):
    print('inside api', ID)
    venue=Venue.query.filter_by(ID=ID).one()
    data=Show.query.filter_by(venueID=ID).all()
    venues={
            "ID" : venue.ID,
            "img": venue.img,
            "name": venue.name,
            "place": venue.place,
            "capacity": venue.capacity,
            "rating": venue.rating
        }
    shows=[]
    for show in data:
        show_dict={
            'ID' : show.ID,
            'img' : show.img,
            'name' : show.name,
            'tags' : show.tags,
            'date' : show.date,
            'ticket': show.ticket,
            'rating' : show.rating,
            'venueID': show.venueID,
            'tickets_booked' : show.tickets_booked,
            'tickets_available' : show.tickets_available
        }
        shows.append(show_dict)
    response={
        'venues': venues,
        'shows': shows,
    }
    return jsonify(response)
