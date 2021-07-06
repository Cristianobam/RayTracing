from scene import *
from vector import *
from tqdm import tqdm

## Image Options
aspectratio = 16 / 9
imwidth = 800
imheight = int(imwidth / aspectratio)
image = [[[0 for _ in range(3)] for _ in range(imwidth)] for _ in range(imheight)]

# Camera Options
viewportheight = 2
viewportwidth = viewportheight * aspectratio
horizontal = Vec3D(viewportwidth, 0, 0)
vertical = Vec3D(0, viewportheight, 0)
focallength = Vec3D(0, 0, 1)
origin = Vec3D(0, 0, 0)
lowerleft = origin - horizontal/2 - vertical/2 - focallength

# Objetcs
s1 = Sphere(Vec3D(0,0,-1), 0.5)

def hitSphere(sphere:Sphere, ray:Ray):
    oc = ray.origin - sphere.origin
    a = ray.dir @ ray.dir
    b = 2 * (oc @ ray.dir)
    c = (oc @ oc) - sphere.r * sphere.r
    delta = b*b - 4*a*c
    if delta < 0:
        return -1
    else:
        return (-b - delta**.5)/(2*a)
# Color Function
def raycolor(sphere:Sphere, ray:Ray):
    t = hitSphere(sphere, ray)
    if t > 0:
        N = (ray.at(t) - Vec3D(0,0,-1)).unit()
        return .5 * RGB(N.x+1, N.y+1, N.z+1)
    t = 0.5 * (ray.dir.y + 1)
    return (1-t) * RGB(1, 1, 1) + t * RGB(0.5, 0.7, 1)

## Render
for i in tqdm(range(imwidth)):
    for j in range(imheight):
        u = (i - 1) / (imwidth - 1)
        v = 1 - (j - 1) / (imheight - 1)
        dir = lowerleft + u*horizontal + v*vertical - origin
        ray = Ray(origin, dir)
        bla = raycolor(s1, ray)
        for n, color in enumerate(bla):
            image[j][i][n] = color
        
save('rendered/fig4.png', image)