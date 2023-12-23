import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/database')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSV_IMAGE_DATA_PATH = os.getenv('CSV_IMAGE_DATA_PATH', 'data.csv')
