from functools import wraps
from flask import jsonify, request, make_response
from routes import app
import jwt
import datetime
from models.users_data import *
from models.admin_data import *



def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        print(token)
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            # Decode the token and verify it with your secret key
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # You can use the username to perform further actions
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
    return decorated



def gen_token(username):
    
    ID = User.query.filter_by(UserName=username).first().ID
    token = jwt.encode({'ID': ID, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},app.config['SECRET_KEY'])
        
    return token 

def genrate_token(username):
    
    ID = Admin.query.filter_by(UserName=username).first().ID
    token = jwt.encode({'ID': ID, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},app.config['SECRET_KEY'])
        
    return token 