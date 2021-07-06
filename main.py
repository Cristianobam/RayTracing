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

# Color Function
def raycolor(ray:Ray):
    t = 0.5 * (ray.dir.y + 1)
    return (1-t) * RGB(1, 1, 1) + t * RGB(0.5, 0.7, 1)

## Render
for i in tqdm(range(imwidth)):
    for j in range(imheight):
        u = (i - 1) / (imwidth - 1)
        v = 1 - (j - 1) / (imheight - 1)
        dir = lowerleft + u*horizontal + v*vertical - origin
        ray = Ray(origin, dir)
        for n, color in enumerate(raycolor(ray)):
            image[j][i][n] = color
        
save('rendered/fig2.png', image)