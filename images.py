from PIL import Image, ImageFilter

# img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('Blur.png', 'png')
# filtered_img2 = img.convert('L')
# filtered_img2.save('grey.png', 'png')
# # filtered_img2.show()#open the file
# resize = filtered_img2.resize((300, 300))
# resize.save("grey-resize.png", 'png')
# resize.show()
img = Image.open('./pokedex/astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
img.show
print('Done')