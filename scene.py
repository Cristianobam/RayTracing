import numpy as np
from PIL import Image

def save(name:str, image:np.ndarray):
    Image.fromarray(np.asarray(np.array(image) * 255, dtype='uint8')).save(name)