from PIL import Image
import numpy as np
import xlsxwriter


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


FILENAME = 'image.jpg'  # image can be in gif jpeg or png format
image = Image.open(FILENAME).convert('RGB')

width, height = image.size
aspect_ratio = width/height
resized_height = 150
resized_width = int(round(resized_height*aspect_ratio))
size = resized_width, resized_height
image2 = image.resize(size, Image.ANTIALIAS)
image2.save('resize.jpg')
pixels = image2.load()

file = open('output.txt', 'w')  # the file with the RGB values
for j in range(resized_height):
    for t in range(0, 3):
        for i in range(resized_width):
            file.write('%d  \t' % pixels[i, j][t])
        file.write(' \n')
file.close()


workbook = xlsxwriter.Workbook('image_ex.xlsx')
worksheet = workbook.add_worksheet()

pix = np.array(image2)


pix = pix.transpose(0, 2, 1).reshape(-1, pix.shape[1])

list_red = np.arange(0, pix.shape[0], 3)
list_green = np.arange(1, pix.shape[0]-1, 3)
# list_blue = np.arange(2, pix.shape[0]-2, 3)

for row in range(0, pix.shape[0]):
    for col in range(pix.shape[1]):
        worksheet.write(row, col, pix[row, col])
        if row in list_red:
            col_hex = rgb2hex(pix[row, col], 0, 0)
        elif row in list_green:
            col_hex = rgb2hex(0, pix[row, col], 0)
        else:
            col_hex = rgb2hex(0, 0, pix[row, col])

        format1 = workbook.add_format({'bg_color': col_hex})
        worksheet.conditional_format(row, 0, row, pix.shape[1], {'type': 'cell',
                                                                 'criteria': '==',
                                                                 'value': pix[row, col],
                                                                 'format': format1})
workbook.close()
