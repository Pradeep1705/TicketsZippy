from routes import app, db 
from flask import Flask, request, jsonify
import os
from tokensJWT import *
from models.venues_data import *
from models.shows_data import *
import base64

@app.route("/createShow/<int:ID>/", methods=["GET", "POST"])
@jwt_required
def add_show(ID):
    if request.method=="GET":
        return jsonify({"message":"create show"})
    if request.method=="POST":
        venue= Venue.query.filter_by(ID=ID).one()

        if 'upload_image' not in request.files:
            return jsonify({"message": "No file selected."}), 400

        upload_image = request.files['upload_image']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
        upload_image.save(filepath)

        new_show = Show(
            img=upload_image.filename,
            name=request.form['name'],
            tags=request.form['tags'],
            date=request.form['date'],
            ticket=int(request.form['ticket']),
            rating=int(request.form['rating']),
            tickets_booked = 0,
            tickets_available= venue.capacity,
            venueID = ID
        )
        db.session.add(new_show)
        db.session.commit()

        img_path = os.path.join('static', 'images', new_show.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')

        show_dict = {
            'img':  base64_encoded_data,
            'name': new_show.name,
            'tags': new_show.tags,
            'date': new_show.date,
            'ticket': new_show.ticket,
            'rating': new_show.rating,
            'tickets_booked': new_show.tickets_booked,
            'tickets_available': new_show.tickets_available,
            'venueID': new_show.venueID
        }
        return jsonify(show_dict)

@app.route("/updateShow/<int:ID>/", methods=["GET", "POST"])
@jwt_required
def update_show(ID):
    if request.method == 'GET':
        show= Show.query.filter_by(ID=ID).one()
        show_dict = {
            'img': show.img,
            'name': show.name,
            'tags': show.tags,
            'date': show.date,
            'ticket': show.ticket,
            'rating': show.rating,
            'tickets_booked': show.tickets_booked,
            'tickets_available': show.tickets_available,
            'venueID': show.venueID
        }
        return jsonify(show_dict)
        
    if request.method == "POST":
        show = Show.query.filter_by(ID=ID).one_or_none()
        if show is not None:
            upload_image = request.files['upload_image']
            if upload_image:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
                upload_image.save(filepath)

                show.img = upload_image.filename

            name = request.form['name']
            tags = request.form['tags']
            date = request.form['date']
            ticket = request.form['ticket']
            rating = request.form['rating']

            show.name = name
            show.tags=tags
            show.date = date
            show.ticket = ticket
            show.rating = rating
            db.session.add(show)
            db.session.commit

            img_path = os.path.join('static', 'images', show.img)
            with open(img_path, 'rb') as f:
                img_data = f.read() 
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')

            show_dict = {
            'img': base64_encoded_data,
            'name': show.name,
            'tags': show.tags,
            'date': show.date,
            'ticket': show.ticket,
            'rating': show.rating,
            }
            return jsonify(show_dict)
        else:
            return jsonify({"error": "Show not found"}), 404

@app.route("/deleteShow/<int:ID>/", methods=["GET", "POST"])

def delete_show(ID):
    data = Show.query.filter_by(ID=ID).one()
    
    if request.method == "POST":
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"show deleted succesfully"})
    return jsonify({"message":"deleteShow"})      
