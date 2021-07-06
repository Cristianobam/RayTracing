from numbers import Number
import numpy as np

class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def unit(self):
        norm = self.norm
        return Vec3D(self.x/norm, self.y/norm, self.z/norm)
    
    @property
    def norm(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def __mul__(self, other):
        if isinstance(other, (Number, np.number)):
            x = other * self.x
            y = other * self.y
            z = other * self.z
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = other[0] * self.x
            y = other[1] * self.y
            z = other[2] * self.z
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __matmul__(self, other):
        if isinstance(other, (list, tuple, np.ndarray, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            return self.x * other[0] + self.y * other[1] + self.z * other[2]

        else:
            NotImplemented
            
    def __add__(self, other):
        if isinstance(other, (Number, np.number)):
            x = other + self.x
            y = other + self.y
            z = other + self.z
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = other[0] + self.x
            y = other[1] + self.y
            z = other[2] + self.z
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
            
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (Number, np.number)):
            x = self.x - other
            y = self.y - other
            z = self.z - other
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = self.x - other[0]
            y = self.y - other[1]
            z = self.z - other[2]
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
        
    def __rsub__(self, other):
        if isinstance(other, (Number, np.number)):
            x = other - self.x
            y = other - self.y
            z = other - self.z
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = other - self.x
            y = other - self.y
            z = other - self.z
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
        
    def __truediv__(self, other):
        if isinstance(other, (Number, np.number)):
            x =  self.x / other
            y =  self.y / other
            z =  self.z / other
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = self.x / other[0]
            y = self.y / other[1]
            z = self.z / other[2]
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
            
    def __rtruediv__(self, other):
        if isinstance(other, (Number, np.number)):
            x =  other / self.x
            y =  other / self.y
            z =  other / self.z
            return Vec3D(x, y, z)
        
        elif isinstance(other, (list, tuple, Vec3D)):
            assert len(other) == 3, "The array length is freater than 3"
            x = other[0] / self.x
            y = other[1] / self.y
            z = other[2] / self.z
            return Vec3D(x, y, z)
        
        else:
            NotImplemented
        
    def __getitem__(self, key):
        return [self.x, self.y, self.z][key]
    
    def __len__(self):
        return 3
    
    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'
    
class Ray:
    def __init__(self, origin:Vec3D, direction:Vec3D):
        self.origin = origin
        self.dir = direction.unit()
        
class RGB(Vec3D):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        
    def __repr__(self):
        return f'R:{self.x}, G:{self.y}, B:{self.z}'