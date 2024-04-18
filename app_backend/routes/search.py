from routes import app
from tokensJWT import *
from models.venues_data import *
from models.shows_data import *
import os
import base64

@app.route("/search", methods = ["POST"])
@jwt_required
def search():
    query= request.json['searched']
    get_venues = Venue.query.filter(Venue.name.like(f'%{query}%')).all()
    get_shows = Show.query.filter(Show.name.like(f'%{query}%')).all()
    get_places = Venue.query.filter(Venue.place.like(f'%{query}%')).all()

    if get_venues and get_shows and get_places =="":
        return jsonify({'message':'Invalid'})

    venues=[]
    for venue in get_venues:
        img_path = os.path.join('static', 'images', venue.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
        venue_dict={
            'ID' : venue.ID,
            'img' : base64_encoded_data,
            'name' : venue.name,
            'place' : venue.place,
            'capacity' : venue.capacity,
            'rating' : venue.rating
        }
        venues.append(venue_dict)

    shows=[]
    for show in get_shows:
        venue = Venue.query.filter_by(ID = show.venueID).one()
        img_path = os.path.join('static', 'images', show.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
        show_dict={
            'ID' : show.ID,
            'img' : base64_encoded_data,
            'name' : show.name,
            'tags' : show.tags,
            'date' : show.date,
            'ticket': show.ticket,
            'rating' : show.rating,
            'venueID': show.venueID,
            'tickets_booked' : show.tickets_booked,
            'tickets_available' : show.tickets_available,
            'venueName': venue.name
        }
        shows.append(show_dict)

    places=[]
    for venue in get_places:
        img_path = os.path.join('static', 'images', venue.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
        venue_dict={
            'ID' : venue.ID,
            'img' : base64_encoded_data,
            'name' : venue.name,
            'place' : venue.place,
            'capacity' : venue.capacity,
            'rating' : venue.rating
        }
        places.append(venue_dict)
    response={
        'venues': venues,
        'shows': shows,
        'places': places
    }
    return jsonify(response)
