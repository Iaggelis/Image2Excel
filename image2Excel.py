from PIL import Image
import numpy as np
import xlsxwriter


FILENAME = 'image.jpg'  # image can be in gif jpeg or png format
image = Image.open(FILENAME).convert('RGB')

width = image.size[0]
height = image.size[1]
# print(image.size)
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
file.close()


workbook = xlsxwriter.Workbook('test1.xlsx')
worksheet = workbook.add_worksheet()

pix = np.array(image2)


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


pix = pix.transpose(0, 2, 1).reshape(-1, pix.shape[1])

for row in range(0, pix.shape[0]):
    for col in range(pix.shape[1]):
        worksheet.write(row, col, pix[row, col])
        # format1 = workbook.add_format({'bg_color': rgb2hex})
        # worksheet.conditional_format(row, col, row, col, {'type': 'cell',
        #                                                   'criteria': '==',
        #                                                   'value': pix[row, col],
        #                                                   'format': format1})


workbook.close()


