import numpy as np

## Image Options
aspectratio = 16 / 9
imwidth = 800
imheight = np.ceil(imwidth / aspectratio).astype(int)
image = np.zeros(shape=(imheight, imwidth, 3))

## Render
for i in range(imwidth):
    for j in range(imheight):
        r = i/(imwidth-1)
        g = (imheight - j)/(imheight-1)
        b = .25
        image[j, i, :] = np.array([r, g, b])
        
save('rendered/fig1.png', image)