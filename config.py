import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
app = Flask(__name__)


# Get the underlying Flask app instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://anonymous:@ensembldb.ensembl.org/ensembl_website_97'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

