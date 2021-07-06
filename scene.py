import numpy as np
from vector import Vec3D 
from PIL import Image

class Sphere:
    def __init__(self, origin:Vec3D, radius:float):
        self.origin = origin
        self.r = radius

def save(name:str, image:np.ndarray):
    Image.fromarray(np.asarray(np.array(image) * 255, dtype='uint8')).save(name)