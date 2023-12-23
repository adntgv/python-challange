import cv2
import numpy as np
import pandas as pd
from ..database.models import Image
from ..database import db

def process_and_store_images(csv_file):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        depth = row['depth']
        image = np.array(row[1:], dtype=np.uint8).reshape((1, -1))
        resized_image = cv2.resize(image, (150, 1), interpolation=cv2.INTER_AREA)
        new_image = Image(depth=depth, image_data=resized_image.tobytes())
        db.session.add(new_image)
    db.session.commit()
