from PIL import Image
# image = imageage.open("ayy.jpg") #Can be many different formats.

# pix = image.load()


FILENAME = 'image.jpg'  # image can be in gif jpeg or png format
image = Image.open(FILENAME).convert('RGB')

width = image.size[0]
height = image.size[1]
print(image.size)
size = 150, 128  # this size works good with excel
image2 = image.resize(size, Image.ANTIALIAS)
image2.save('resize.jpg')
width = image2.size[0]
height = image2.size[1]
print(image2.size)
pixels = image2.load()

file = open('output.txt', 'w')  # the file with the RGB values
for j in range(height):
    for t in range(0, 3):
        for i in range(width):
            file.write('%d  \t' % pixels[i, j][t])
        file.write(' \n')
    # file.write(' \n')
file.close()
