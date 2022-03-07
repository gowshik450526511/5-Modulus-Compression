import numpy as np
from PIL import Image

img = Image.open('gray.png')
img_gray = img.convert('L')
#pixels = list(img_gray.getdata())
pixels = np.array(img_gray)
#print(pixels)
img_gray.show()

max2=0

for i in range(len(pixels)):
    for j in range(len(pixels[i])):
        max2 = max(max2,pixels[i][j])
        
print("maximum2",max2)

for i in range(len(pixels)):
    for j in range(len(pixels[0])):
        
        if pixels[i][j] % 5 == 4:
            pixels[i][j] = pixels[i][j] + 1
        
        elif pixels[i][j] % 5 == 3:
            pixels[i][j] = pixels[i][j] + 2
        
        elif pixels[i][j] % 5 == 2:
            pixels[i][j] = pixels[i][j] - 2
    
        elif pixels[i][j] % 5 == 1:
            pixels[i][j] = pixels[i][j] - 1
        
#print(pixels)

min1= 1000
max1= 0

for i in range(len(pixels)):
    for j in range(len(pixels[0])):
        pixels[i][j] = pixels[i][j]//5
        min1 = min(min1,pixels[i][j])
    

print("minimum",min1)

for i in range(len(pixels)):
    for j in range(len(pixels[0])):
        pixels[i][j] = pixels[i][j]-min1
        max1 = max(max1,pixels[i][j])


print("maximum",max1)
data = Image.fromarray(pixels)
data.save(r'compressed_image',format="png")
data.show()