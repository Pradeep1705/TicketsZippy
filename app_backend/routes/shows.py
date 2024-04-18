from routes import app
from tokensJWT import *
from models.shows_data import *
import base64
import os


@app.route("/getShows/<ID>/", methods=["GET"])
@jwt_required
def user_show(ID):
    data=Show.query.filter_by(venueID=ID).all()
    shows=[]
    for show in data:
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
            'tickets_available' : show.tickets_available
        }
        shows.append(show_dict)
    return jsonify(shows)