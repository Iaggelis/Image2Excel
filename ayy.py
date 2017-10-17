from PIL import Image
# im = Image.open("ayy.jpg") #Can be many different formats.

# pix = im.load()




FILENAME='ay.jpg' #image can be in gif jpeg or png format 
im=Image.open(FILENAME).convert('RGB')

w=im.size[0]
h=im.size[1]
print im.size
size = 200,128
im2=im.resize(size,Image.ANTIALIAS)
im2.save('test1.jpg')
w=im2.size[0]
h=im2.size[1]
print im2.size
pix=im2.load()

file = open('out2.txt','w')
for j in range(h):
	for t in range(0,3):
		for i in range(w):			
			file.write('%d  \t' %pix[i,j][t])
		file.write(' \n')
	# file.write(' \n')
file.close()
