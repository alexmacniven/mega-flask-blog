from flask import Flask

app = Flask(__name__)

# routes is going to import 'app' so putting the import here will avoid
# circular imports.
from app import routes

