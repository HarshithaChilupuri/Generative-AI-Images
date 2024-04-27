# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gKLvnSYUJEj6QwoE6J9Ynn4VsEuuJm7r
"""

!pip install rembg

from rembg import remove
import requests
from PIL import Image
from io import BytesIO
import os

os.makedirs("original",exist_ok = True)
os.makedirs("masked",exist_ok = True)

img_url = "/content/original/product3.jpg"

img_name = img_url.split('/')[-1]

img = Image.open("/content/original/product3.jpg")

img.save('original/' +img_name, format = 'jpeg')

output_pATH = 'masked/' + img_name

output_pATH

with open(output_pATH, 'wb') as f:
  input = open('original/' +img_name, 'rb').read()
  subject = remove(input)
  f.write(subject)

background_img = "/content/background_images/3.jpg"

background_img = Image.open("/content/background_images/3.jpeg")

background_img = background_img.resize((img.width, img.height))

foreground_img = Image.open(output_pATH)
background_img.paste(foreground_img,(440,-70),foreground_img)
background_img.save('masked/background.jpg',format = 'jpeg')

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import PIL

foreground_img = Image.open(output_pATH)
background_img = Image.open("/content/background_images/3.jpeg")
new_width = 370
new_height = 370
foreground_img = foreground_img.resize((new_width, new_height))
angle = 0
foreground_img = foreground_img.rotate(angle, expand = True)
background_img.paste(foreground_img, (270,5), foreground_img)
background_img.save('masked/background.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

i1 = Image.open('/content/masked/product3.jpg')
i2 = Image.open('/content/background_images/3.jpeg')
print(i1.size,i1.mode)
print(i2.size,i2.mode)
if i1.size[0] < i2.size[0] and i1.size[1] < i2.size[1]:
    i1 = i1.resize(i2.size)
else:
    i2 = i2.resize(i1.size)

i2 = i2.convert(i1.mode)

print(i1.size,i1.mode)
print(i2.size,i2.mode)

image = Image.open('/content/masked/background.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1.5)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

#background2/5.jpg

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATH)
background_img2 = Image.open("/content/background_images/5.jpeg")
new_width = 445
new_height = 445
foreground_img = foreground_img.resize((new_width, new_height))
angle = 0
foreground_img = foreground_img.rotate(angle, expand = True)
background_img2.paste(foreground_img, (159,89), foreground_img)
background_img2.save('masked/background2.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

i1 = Image.open('/content/masked/product3.jpg')
i2 = Image.open('/content/background_images/5.jpeg')
print(i1.size,i1.mode)
print(i2.size,i2.mode)
if i1.size[0] < i2.size[0] and i1.size[1] < i2.size[1]:
    i1 = i1.resize(i2.size)
else:
    i2 = i2.resize(i1.size)

i2 = i2.convert(i1.mode)

print(i1.size,i1.mode)
print(i2.size,i2.mode)

image = Image.open('/content/masked/background2.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1.5)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background2.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background2.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1.2  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save("output_image.jpg")  # Save the image

#for font
# Load the image
#image_path = "your_image.jpg"  # Replace with the path to your image
image = Image.open('/content/outputs/output_image.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "Aftershave Lavanille"

# Define the font size and font type
font_size = 40
font = ImageFont.truetype("/content/fonts/calibri-regular.ttf",font_size)
# Determine the position to place the text
text_position = (240, 680)  # Adjust the coordinates as needed

# Define text color
text_color = (102, 51, 0)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
image.save("/content/outputs/background2.jpg")  # Save the image with the added text

from PIL import Image

# Load the shampoo bottle image with a transparent backgr  # Replace with the path to your shampoo bottle image
bottle_image = Image.open('/content/masked/reflection.png')
bottle_image = bottle_image.convert("RGBA")

# Display the image properties
print("Image mode:", bottle_image.mode)  # Should display "RGBA" for an image with transparency
print("Image size:", bottle_image.size)  # Display the dimensions of the image



#background3

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATH)
foreground_imgg = Image.open(output_pATH)
foreground_img1 = Image.open('/content/background_images/vanilla-flower-png-3.png')
#foreground_img2 = Image.open('/content/background_images/9.png')
background_img2 = Image.open("/content/background_images/10.jpg")
new_width = 1900
new_height = 1900

new_widthh = 2000
new_heightt = 2000

new_widthkh = 2000
new_heightit = 2000

new_widthhh = 900
new_heighttt = 900

foreground_img = foreground_img.resize((new_width, new_height))
foreground_imgg = foreground_imgg.resize((new_widthh, new_heightt))
foreground_img1 = foreground_img1.resize((new_widthhh, new_heighttt))
#foreground_img2 = foreground_img2.resize((new_widthkh, new_heightit))
angle = 0
anglee = 358
foreground_img = foreground_img.rotate(angle, expand = True)
foreground_imgg = foreground_imgg.rotate(angle, expand = True)
foreground_img1 = foreground_img1.rotate(anglee, expand = True)
#foreground_img2 = foreground_img2.rotate(angle, expand = True)



background_img2.paste(foreground_img, (1100,450), foreground_img)
background_img2.paste(foreground_imgg, (1560,541), foreground_imgg)
background_img2.paste(foreground_img1, (1375,1530), foreground_img1)
#background_img2.paste(foreground_img2, (1400,200), foreground_img2)

background_img2.save('masked/background3.jpg',format = 'JPEG')

#2190,1570

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

#background 4

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATH)
foreground_img2 = Image.open('/content/background_images/9.png')
foreground_img3 = Image.open('/content/background_images/van.png')
background_img4 = Image.open("/content/background_images/unfinished-wood-tray-1.jpg")
new_width = 1000
new_height = 950

wid = 500
hi = 500

wee = 300
hee = 300
foreground_img = foreground_img.resize((new_width, new_height))
foreground_img2 = foreground_img2.resize((wid, hi))
foreground_img3 = foreground_img3.resize((wee, hee))
angle = 0
anglee = 35
angleee = 4
foreground_img = foreground_img.rotate(angle, expand = True)
foreground_img2 = foreground_img2.rotate(anglee, expand = True)
foreground_img3 = foreground_img3.rotate(angleee, expand = True)
background_img4.paste(foreground_img2, (740,100), foreground_img2)
background_img4.paste(foreground_img, (400,-135), foreground_img)
background_img4.paste(foreground_img3, (590,460), foreground_img3)
background_img4.save('masked/background4.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background4.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background4.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background4.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('outputs/background4.jpg',format = 'JPEG')  # Save the image



#background 5

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATH)
background_img5 = Image.open("/content/background_images/17.jpg")
new_width = 500
new_height = 500
foreground_img = foreground_img.resize((new_width, new_height))
angle = 0
foreground_img = foreground_img.rotate(angle, expand = True)
background_img5.paste(foreground_img, (62,92), foreground_img)
background_img5.save('masked/background5.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background5.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1.5)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background5.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background5.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('masked/background5.jpg',format = 'JPEG')  # Save the image

#for font
# Load the image
#image_path = "your_image.jpg"  # Replace with the path to your image
image = Image.open('masked/background5.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "LAVANILLE"

# Define the font size and font type
font_size = 30
font = ImageFont.truetype("/content/fonts/arial.ttf",font_size)
# Determine the position to place the text
text_position = (250, 576)  # Adjust the coordinates as needed

# Define text color
text_color = (245, 2545, 220)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
image.save("/content/outputs/background5.jpg")  # Save the image with the added text



#product 1/ Background 1

img2_url = "/content/original/product1.jpg"

img_name = img2_url.split('/')[-1]

img = Image.open("/content/original/product1.jpg")

img.save('original/' +img_name, format = 'jpeg')

output_pATHH = 'masked/' + img_name

with open(output_pATHH, 'wb') as f:
  input = open('original/' +img_name, 'rb').read()
  subject = remove(input)
  f.write(subject)

background_img = Image.open("/content/background_images/3.jpeg")

background_img = background_img.resize((img.width, img.height))

foreground_img = Image.open(output_pATHH)
background_img.paste(foreground_img,(440,-70),foreground_img)
background_img.save('masked/background.jpg',format = 'jpeg')

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import PIL


background_img = Image.open("/content/background_images/dirt.jpg")
foreground_img = Image.open(output_pATHH)
foreground_img1 = Image.open('/content/background_images/hand.png')


new_width = 1000
new_height = 1000
new_w = 1279
new_h = 517


foreground_img = foreground_img.resize((new_width, new_height))
foreground_img1 = foreground_img1.resize((new_w, new_h))

angle = 0
anglee = 0

foreground_img1 = foreground_img1.rotate(anglee, expand = True)
background_img.paste(foreground_img1, (325,900), foreground_img1)

foreground_img = foreground_img.rotate(angle, expand = True)
background_img.paste(foreground_img, (160,280), foreground_img)





background_img.save('masked/background11.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background11.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1.5)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background11.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

#for font
# Load the image
#image_path = "your_image.jpg"  # Replace with the path to your image
image = Image.open('masked/background11.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "SEVILLE"

# Define the font size and font type
font_size = 30
font = ImageFont.truetype("/content/fonts/arial.ttf",font_size)
# Determine the position to place the text
text_position = (185, 570)  # Adjust the coordinates as needed

# Define text color
text_color = (102, 51, 0)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
image.save("/content/outputs/background11.jpg")  # Save the image with the added text

#background 22/1 product.jpg

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATHH)
foreground_img2 = Image.open('/content/background_images/poll.png')
background_img2 = Image.open("/content/background_images/white.jpg")
new_width = 1200
new_height = 1200
newwid =  1568
newhei =  700
foreground_img = foreground_img.resize((new_width, new_height))
foreground_img2 = foreground_img2.resize((newwid, newhei))
angle = 2
anglee = 7
foreground_img2 = foreground_img2.rotate(anglee, expand = True)
background_img2.paste(foreground_img2, (200,250), foreground_img2)

foreground_img = foreground_img.rotate(angle, expand = True)
background_img2.paste(foreground_img, (400,10), foreground_img)


background_img2.save('masked/background22.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background22.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background22.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background22.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('masked/backgroun22.jpg',format = 'JPEG')  # Save the image

#for font
# Load the image
#image_path = "your_image.jpg"  # Replace with the path to your image
image = Image.open('masked/background22.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "SEVILLE"

# Define the font size and font type
font_size = 90
font = ImageFont.truetype("/content/fonts/calibri-bold.ttf",font_size)
# Determine the position to place the text
text_position = (950, 1100)  # Adjust the coordinates as needed

# Define text color
text_color = (255, 69, 0)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
image.save("/content/outputs/background22.jpg")  # Save the image with the added text

#background 33

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops, ImageDraw, ImageFont
import PIL

foreground_img = Image.open(output_pATHH)
foreground_img2 = Image.open('/content/background_images/soapp.png')
background_img2 = Image.open("/content/background_images/orange.jpg")
new_width = 2500
new_height = 2500
newwid = 4900
newhei =  4900
foreground_img = foreground_img.resize((new_width, new_height))
foreground_img2 = foreground_img2.resize((newwid, newhei))
angle = 2
anglee = 5
foreground_img2 = foreground_img2.rotate(anglee, expand = True)
background_img2.paste(foreground_img2, (2000,-100), foreground_img2)

foreground_img = foreground_img.rotate(angle, expand = True)
background_img2.paste(foreground_img, (2500,10), foreground_img)


background_img2.save('masked/background33.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background33.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background33.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background33.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('masked/backgroun33.jpg',format = 'JPEG')  # Save the image

#for font
# Load the image
#image_path = "your_image.jpg"  # Replace with the path to your image
image = Image.open('masked/background33.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "SEVILLE"

# Define the font size and font type
font_size = 500
font = ImageFont.truetype("/content/fonts/calibri-bold.ttf",font_size)
# Determine the position to place the text
text_position = (550, 1100)  # Adjust the coordinates as needed

# Define text color
text_color = (105, 105, 105)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
image.save("/content/outputs/background33.jpg")  # Save the image with the added text

#background 44

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import PIL


background_img = Image.open("/content/background_images/abstarct.jpg")
foreground_img = Image.open(output_pATHH)
foreground_img1 = Image.open('/content/background_images/poll.png')


new_width = 1000
new_height = 1000
new_w = 1279
new_h = 517


foreground_img = foreground_img.resize((new_width, new_height))
foreground_img1 = foreground_img1.resize((new_w, new_h))

angle = 7
anglee = 9

foreground_img1 = foreground_img1.rotate(anglee, expand = True)
background_img.paste(foreground_img1, (350,300), foreground_img1)

foreground_img = foreground_img.rotate(angle, expand = True)
background_img.paste(foreground_img, (400,-10), foreground_img)





background_img.save('masked/background44.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background44.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(1)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(0.9)

brighterr.show()
brighterr.save('masked/background44.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background44.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('outputs/backgroun44.jpg',format = 'JPEG')  # Save the image

#background 55

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import PIL


background_img = Image.open("/content/background_images/6.jpeg")
foreground_img = Image.open(output_pATHH)
foreground_img1 = Image.open('/content/background_images/pud.png')


new_width = 350
new_height = 350
new_w = 100
new_h = 100


foreground_img = foreground_img.resize((new_width, new_height))
foreground_img1 = foreground_img1.resize((new_w, new_h))

angle = 7
anglee = 9

foreground_img1 = foreground_img1.rotate(anglee, expand = True)
background_img.paste(foreground_img1, (350,300), foreground_img1)

foreground_img = foreground_img.rotate(angle, expand = True)
background_img.paste(foreground_img, (190,35), foreground_img)





background_img.save('masked/background55.jpg',format = 'JPEG')

#backgroundd = foreground_img.rotate(270, PIL.Image.NEAREST, expand = 1)
#vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.show()

image = Image.open('/content/masked/background55.jpg')
image_detail = image.filter(ImageFilter.DETAIL)
#image_sharp = image_detail.filter(ImageFilter.SHARPEN)
image_smooth = image_detail.filter(ImageFilter.SMOOTH)
image_detailed = image_smooth.filter(ImageFilter.DETAIL)
image_detailedd = image_detailed.filter(ImageFilter.DETAIL)
#image_contour = image.filter(ImageFilter.SMOOTH_MORE)
#image_edge = image_detailedd.filter(ImageFilter.EDGE_ENHANCE)
#image_find_edges = image_sharp.filter(ImageFilter.FIND_EDGES)
color_enhancer = ImageEnhance.Color(image_detailedd)
sharpness_enhancer = ImageEnhance.Sharpness(image_detailedd)
enhanced_image = color_enhancer.enhance(1)

brightness_enhancer = ImageEnhance.Brightness(enhanced_image) # contrast
brighter = brightness_enhancer.enhance(0.7)

contrast_enhancer = ImageEnhance.Contrast(brighter) # contrast
brighterr = contrast_enhancer.enhance(1)

brighterr.show()
brighterr.save('masked/background55.jpg',format = 'JPEG')
#brighterr.save('background.jpg')

from PIL import Image, ImageEnhance

# Load the image
image_path = "masked/background55.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Adjust brightness
brightness_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_brightness = ImageEnhance.Brightness(image)
image = enhancer_brightness.enhance(brightness_factor)

# Adjust contrast
contrast_factor = 1  # Increase or decrease as needed (1.0 means no change)
enhancer_contrast = ImageEnhance.Contrast(image)
image = enhancer_contrast.enhance(contrast_factor)

# Save or display the resulting image
image.show()  # Display the image
image.save('masked/backgroun55.jpg',format = 'JPEG')  # Save the image

from PIL import Image, ImageDraw, ImageFont

# Load the image # Replace with the path to your image
image = Image.open('masked/background55.jpg')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the text to be added
text = "SERVILLE"

# Define the font size and font type
font_size = 40
font = ImageFont.truetype("/content/fonts/calibri-bold.ttf", font_size)  # You can specify the path to your desired font file

# Determine the position to place the text
text_position = (340, 440)  # Adjust the coordinates as needed

# Define text color
text_color = (0, 0, 0)  # White color in RGB format

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save or display the resulting image
image.show()  # Display the image with the added text
# image.save("output_image_with_text.jpg")
image.save('/content/outputs/background55.jpg') # Save the image with the added text



#product 3 background 111

img3_url = "/content/original/product1.jpg"

















































































































































#shadow



























ref_img = Image.open('/content/masked/reflection.png')
new_image = Image.new("RGBA", ref_img.size, (0, 0, 0, 0))
for x in range(ref_img.width):
    for y in range(ref_img.height):
        pixel_color = ref_img.getpixel((x, y))
        if len(pixel_color) == 4 and pixel_color[3] > 0:
            new_image.putpixel((x, y), pixel_color)

new_image.save("image_without_background.png")

original_image = Image.open("/content/masked/background2.jpg")
reflection_image = Image.open("/content/masked/reflection.png")

reflection_image = reflection_image.resize((200, 200))
reflection_position = (original_image.width - reflection_image.width, original_image.height - reflection_image.height)
original_image.paste(reflection_image, reflection_position, reflection_image)

reflection_image = reflection_image.resize((original_image.width, int(original_image.height / 4)))
#reflection_image = reflection_image.transpose(Image.FLIP_LEFT_RIGHT)
original_image.paste(reflection_image, (0, original_image.height - reflection_image.height), reflection_image)
original_image.save("/content/masked/result_image.jpg")























