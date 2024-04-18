from routes import app
from flask import Flask, request,jsonify
import os
import base64
from models.users_data import *
from models.tickets_data import *
from tokensJWT import *
import datetime

@app.route("/login", methods=[ "POST"])
def user_login():
    
    username= request.json['username']
    password= request.json['password']
    try:
        user = User.query.filter_by(UserName = username).first()
        if not user:
            return jsonify({'message':'Invalid'})
        if user.Password == password:
            token = gen_token(username)
            log_check = loggedIn.query.filter_by(userName = username).one()
            cur_time=datetime.datetime.now()
            log_check.time = cur_time.timestamp()
            db.session.add(log_check)
            db.session.commit()
            return jsonify({'token':token, 'userType': 'user'})
        else:
            return jsonify({'message':'Invalid'})
    except:
        return jsonify({'message':'Invalid'})

@app.route("/register", methods=["POST"])
def Signin():
    if request.method=="POST":
        print(request.json)
        data=request.json
        new_user = User(UserName= data['username'], Email=data['email'], Password=data['password'])
        cur_time=datetime.datetime.now()
        new_log = loggedIn(userName = data['username'], time = cur_time.timestamp())
        print(new_user)
        db.session.add(new_user)
        db.session.add(new_log)
        db.session.commit()
        user_data = {
            "username": new_user.UserName,
            "email": new_user.Email,
            "password": new_user.Password
        }
        return jsonify(user_data)

@app.route("/userProfile", methods=["GET"])
@jwt_required
def user_profile():
    

    token = request.headers.get('Authorization')  
    payload = jwt.decode(token, 'prad1705', algorithms=['HS256']) 
    user_id = payload.get('ID')  
    usr_name = User.query.filter_by(ID=user_id).one() 
    
    get_ticket = Ticket.query.filter_by(userName = usr_name.UserName).order_by(Ticket.ID.desc()).all()  
    print(get_ticket)
    
    if get_ticket == []:
            return jsonify({"message":"No_tickets"})
    user_data = {
            "username": usr_name.UserName,
            "email": usr_name.Email,
            "password": usr_name.Password
        }
    view_ticket=[]
    for data in get_ticket:
        img_path = os.path.join('static', 'images', data.img)
        with open(img_path, 'rb') as f:
            img_data = f.read()
            base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
        ticket_info={
            "userName":data.userName,
            "venueName":data.venueName,
            "showName":data.showName,
            "date":data.date,
            "seats":data.seats,
            "price":data.price,
            "img": base64_encoded_data
        }
        view_ticket.append(ticket_info)
    
    resData = {
        "userData": user_data,
        "ticketList": view_ticket
    }
    
    return jsonify(resData)