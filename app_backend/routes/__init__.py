from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_uploads import UploadSet, IMAGES, configure_uploads
import redis

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'prad1705'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticket.db"
app.config["UPLOAD_FOLDER"] = "static/images"
# photos = UploadSet('photos', IMAGES)
# redis_cli = redis.Redis(host="localhost", port=6379, password="", decode_responses=True)

# configure_uploads(app, photos)


from routes import admin
from routes import bookTicket
from routes import crudShow
from routes import crudVenue
from routes import search
from routes import shows
from routes import user
from routes import venues
from models import admin_data
from models import shows_data
from models import tickets_data
from models import users_data
from models import venues_data

with app.app_context():
    db.init_app(app)
    # db.create_all()