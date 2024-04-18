from routes import app, db 
from flask import Flask, request, jsonify
import os
import base64
from tokensJWT import *
from models.venues_data import *
from models.shows_data import *


@app.route("/createVenue", methods=["GET", "POST"])
@jwt_required
def add_venue():
    if request.method == "GET":
        return jsonify({"message": "create_venue"})
    if request.method == "POST":
        if 'upload_image' not in request.files:
            return jsonify({"message": "No file selected."}), 400
        
        upload_image = request.files['upload_image']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
        upload_image.save(filepath)

        new_venue = Venue(
            img = upload_image.filename,
            name = request.form['venueName'],
            place = request.form['place'],
            capacity = int(request.form['capacity']),
            rating = int(request.form['rating'])
        )
        db.session.add(new_venue)
        db.session.commit()
        
        img_path = os.path.join('static', 'images', new_venue.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
        venue_dict = {
            'img': base64_encoded_data,
            'name': new_venue.name,
            'place': new_venue.place,
            'capacity': new_venue.capacity,
            'rating': new_venue.rating
        }
            
        return jsonify(venue_dict)

@app.route("/updateVenue/<int:ID>/", methods=["GET", "POST"])
@jwt_required
def update_venue(ID):
    if request.method=="GET":
        venue = Venue.query.filter_by(ID=ID).one()
        venue_data={
            "ID" : venue.ID,
            "img": venue.img,
            "name": venue.name,
            "place": venue.place,
            "capacity": venue.capacity,
            "rating": venue.rating
        }
        return jsonify(venue_data)
    if request.method == "POST":
        venue = Venue.query.filter_by(ID=ID).one_or_none()
        if venue is not None:
            upload_image = request.files['upload_image']
            if upload_image:
                # filepath = os.path.join('static', 'images', )
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
                upload_image.save(filepath)

                venue.img = upload_image.filename

            name = request.form['venueName']
            place = request.form['place']
            capacity = request.form['capacity']
            rating = request.form['rating']

            # Update venue attributes
            venue.name = name
            venue.place = place
            venue.capacity = capacity
            venue.rating = rating
            db.session.add(venue)
            db.session.commit()

            img_path = os.path.join('static', 'images', venue.img)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')

            venue_dict = {
                'img': base64_encoded_data,
                'name': venue.name,
                'place': venue.place,
                'capacity': venue.capacity,
                'rating': venue.rating
            }
            return jsonify(venue_dict)
        else:
            return jsonify({"error": "Venue not found"}), 404

@app.route("/deleteVenue/<int:ID>/", methods=["GET", "POST"])
def delete_venue(ID):
    data = Venue.query.filter_by(ID=ID).one()
    shows = Show.query.filter_by(venueID = ID).all()
    
    if request.method == "POST":
        if shows != "" :
            for show in shows:
                db.delete(show)
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"venue deleted succesfully"})
    return jsonify({"message":"deleteVenue"})
