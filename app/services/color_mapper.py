import cv2
import numpy as np

def apply_color_map(image_data, colormap=cv2.COLORMAP_JET):
    image = np.frombuffer(image_data, dtype=np.uint8).reshape((1, -1, 1))
    colored_image = cv2.applyColorMap(image, colormap)
    return colored_image
