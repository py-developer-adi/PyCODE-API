'''PyCODE | @_py.code'''

# ? Importing Libraries
from flask import Flask
from models import *
from routes import *

# ! Server Configs
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pycode5.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ! Server Inits
db.init_app(server)
server.register_blueprint(api)

# ! DB Inits
with server.app_context():
    db.create_all()