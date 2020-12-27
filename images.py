from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('Blur.png', 'png')
print('Done')