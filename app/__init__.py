from flask import Flask
from .config.config import Config
from .database import db
from .database.models import Image
from .services.image_processor import process_and_store_images

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    with app.app_context():
        db.create_all()  
        # Check if the database is empty
        if Image.query.first() is None:
            process_and_store_images(Config.CSV_IMAGE_DATA_PATH)

    return app
