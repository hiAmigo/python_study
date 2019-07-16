from PIL import Image, ImageFilter

im = Image.open('./basic/module/test.jpg')

w, h = im.size
print('Original image size: %s,%s', (w, h))
im.thumbnail((w//2, h//2))

im2 = im.filter(ImageFilter.BLUR)
im2.save('./basic/module/thumbnail.jpg', 'jpeg')



