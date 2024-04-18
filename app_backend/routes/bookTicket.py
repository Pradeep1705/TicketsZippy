from routes import app, db
from flask import Flask, request, jsonify
import jwt
from tokensJWT import *
from models.venues_data import *
from models.shows_data import *
from models.tickets_data import *
import datetime


@app.route("/bookTicket/<int:ID>/<int:venueID>/", methods=["GET", "POST"])
@jwt_required
def book_ticket(ID, venueID):
    if request.method == 'GET':
        token = request.headers.get('Authorization') # Extract the token from the headers
        payload = jwt.decode(token, 'prad1705', algorithms=['HS256'])
        
        show= Show.query.filter_by(ID=ID).one()
        venue= Venue.query.filter_by(ID=venueID).one()
        if show.tickets_available > 0:
            show_data={
                "ID" : show.ID,
                "img" : show.img,
                "name" : show.name,
                "tags" : show.tags,
                'date' : show.date,
                'ticket': show.ticket,
                'rating' : show.rating,
                'venueName': venue.name,
                'venueID': show.venueID,
                'tickets_booked' : show.tickets_booked,
                'tickets_available' : show.tickets_available
            }
            
            return jsonify(show_data)
        return jsonify({"message":"tickets_unavailable"})
    if request.method == "POST":
        token = request.headers.get('Authorization')  # Extract the token from the headers
        payload = jwt.decode(token, 'prad1705', algorithms=['HS256'])
        print(payload)
        user_id = payload.get('ID')  # Access the username from the payload
        user_name = User.query.filter_by(ID=user_id).one()
        show= Show.query.filter_by(ID=ID).one()
        venue= Venue.query.filter_by(ID=venueID).one()
        tickets= request.json['ticket']
        seat = int(tickets)
        print(seat)
        if seat > show.tickets_available:
            return jsonify({"message":"tickets_excess"})
        show.tickets_booked += int(tickets)
        show.tickets_available = int(show.tickets_available) - int(tickets) 
        
        user_ticket = Ticket(userName = user_name.UserName, venueName = venue.name, showName = show.name, date = show.date, seats = int(tickets),price = (int(tickets))*(int(show.ticket)), img = show.img) 
        db.session.add(user_ticket)
        db.session.add(show)
        db.session.commit()
        print(user_ticket)
        ticket_info={
            "userName":user_ticket.userName,
            "venueName":user_ticket.venueName,
            "showName":user_ticket.showName,
            "date":user_ticket.date,
            "seats":user_ticket.seats,
            "price":user_ticket.price,
            "img": user_ticket.img
            }
        return jsonify(ticket_info)
