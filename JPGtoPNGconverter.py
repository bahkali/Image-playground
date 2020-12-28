import sys
import os 
from PIL import Image

#grab frist and second argument
argument = sys.argv

dest = './'+ argument[2]
org = argument[1]
#check is new/exist, if not create
if not(os.path.exists(dest)):
    os.mkdir(dest)

#loop through pokedex
for file in os.listdir(org):
    img_jpg = Image.open(org + file)
    listImg = file.split('.')
    imgName = listImg[0]
    #save to the new folder
    img_jpg.save(f'{dest}/{imgName}.png', 'png')



