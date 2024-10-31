from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig

db = SQLAlchemy()  # Create an instance of SQLAlchemy

def create_app():
    app = Flask(__name__)  # Create an instance of the Flask class
    app.config.from_object(DevelopmentConfig)  # Load configuration from DevelopmentConfig

    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for the app

    from .routes import main as main_blueprint  # Import the main blueprint from routes
    app.register_blueprint(main_blueprint)  # Register the main blueprint with the app

    with app.app_context():  # Push the application context
        db.create_all()  # Create all database tables

    return app  # Return the Flask app instance