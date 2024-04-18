from routes import app
from tokensJWT import *
from models.venues_data import *
import base64
import os
import base64
import redis
import json

redis_cli = redis.Redis(host="localhost", port=6379, db=0)

@app.route("/getVenues", methods=["GET"])
@jwt_required
def user_venue():
    cached_venues = redis_cli.get('cached_venues')
    if cached_venues:
        return cached_venues.decode('utf-8')
       

    data = Venue.query.all()
    venues = []

    for venue in data:
        img_path = os.path.join('static', 'images', venue.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')  

        venue_dict = {
            'ID': venue.ID,
            'img': base64_encoded_data, 
            'name': venue.name,
            'place': venue.place,
            'capacity': venue.capacity,
            'rating': venue.rating
        }
        venues.append(venue_dict)

    venues_json = json.dumps(venues)
    redis_cli.setex('cached_venues', 1800, venues_json.encode('utf-8'))  

    return venues_json


@app.route("/adminVenues", methods=["GET"])
@jwt_required
def admin_venue():
    data = Venue.query.all()
    venues = []

    for venue in data:
        img_path = os.path.join('static', 'images', venue.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')  # Encode as Base64

        venue_dict = {
            'ID': venue.ID,
            'img': base64_encoded_data,  # Use the Base64-encoded image data
            'name': venue.name,
            'place': venue.place,
            'capacity': venue.capacity,
            'rating': venue.rating
        }
        venues.append(venue_dict)

    return jsonify(venues)
    

