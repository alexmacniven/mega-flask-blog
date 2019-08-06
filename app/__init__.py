from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


app = Flask(__name__)

# Load the Config class as the applications configuration
app.config.from_object(Config)

# Initialise the SQLAlchemy database.
db = SQLAlchemy(app)

# Initialise the Migrate object.
migrate = Migrate(app, db)

# Routes is going to import 'app' so putting the import here will avoid
# circular imports.
from app import routes

