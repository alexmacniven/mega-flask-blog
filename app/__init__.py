from flask import Flask
from .config import Config

app = Flask(__name__)

# Load the Config class as the applications configuration
app.config.from_object(Config)

# Routes is going to import 'app' so putting the import here will avoid
# circular imports.
from app import routes

