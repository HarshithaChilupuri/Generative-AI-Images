# Generative-AI-Images

This repository contains code and resources for generating and enhancing images using generative AI techniques.

# Folder Structure ~ [Ensure all necessary files are in place and paths are correctly specified]
1. background_images: Contains all the backgrounds and the elements in the form of jpg, jpeg, or png.
2. fonts: Contains all the fonts used during the project which have a .txt extension.
3. outputs: Contains all the final outputs of each product with 5 different backgrounds. So, in total, there are 25 images present in the outputs folder.
4. masked: Contains all the product images that are under the process and yet to be finalized with a few changes to be made.
5. original: Contains all the input products provided and in this project a total of 5 product images are taken in the jpg format, which are to be converted into png format



Follow these steps to get started with the project:

1. Clone the Repository:
 > git clone <repository_url>

2. Install Dependencies:
  Before running the code, make sure you have Python installed along with the required libraries. You can install them using pip:
 > pip install rembg Pillow

3. Download Necessary Files:
Ensure you have the necessary images (product3.jpg, background_images/3.jpg, van2.png, 5.jpeg, 10.jpg, etc.) are placed in the appropriate directories as mentioned in the code.

4. Open the Notebook:
Open the provided Jupyter Notebook or Python script in Google Colab or any Python environment that supports Jupyter Notebook or Google Colab.

## Running the Code - [Adjust parameters and values as needed to achieve desired results]

Execute the code cells in the provided notebook or Python script sequentially.
Follow these steps to run the code and generate/enhance images:

# 1. Background Removal:
The `rembg` library is used to remove the background from the product image (`product3.jpg`).Run the code cells sequentially to generate and enhance the images. The resulting image is saved in the `masked` directory.

```
> img3_url = "/content/original/product4.jpg"

> img_name = img_url.split('/')[-1]

> img = Image.open("/content/original/product4.jpg")

> img.save('original/' +img_name, format = 'jpeg')

> with open(output_pATH, 'wb') as f:
> input = open('original/' +img_name, 'rb').read()
> subject = remove(input)
> f.write(subject)
```

# 2. Image Composition and Enhancement:
   
Different product images and background images are composited together using the paste method in Pillow. Angles and positions are adjusted for realism.
For this various image composition and enhancement techniques are applied using the Pillow library.
# Code for image composition and enhancement

```
background_img = Image.open("/content/background_images/blackpedal.jpg")
background_img = background_img.resize((img.width, img.height))

foreground_img = Image.open(output_pATH)
background_img.paste(foreground_img,(440,-70),foreground_img)
background_img.save('masked/background.jpg',format = 'jpeg')


from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import PIL

foreground_img = Image.open(output_pATH)
foreground_img1 = Image.open('/content/background_images/van2.png')
foreground_img2 = Image.open('/content/background_images/van2.png')
background_img = Image.open("/content/background_images/blackpedal.jpg")

new_width1 = 110
new_height2=  110

new_width11 = 110
new_height22=  110

new_width = 370
new_height = 370

foreground_img = foreground_img.resize((new_width, new_height))
foreground_img1 = foreground_img1.resize((new_width1, new_height2))
foreground_img2 = foreground_img2.resize((new_width11, new_height22))

angle = 0
anglee = 4
angleee = 323

foreground_img = foreground_img.rotate(angle, expand = True)
background_img.paste(foreground_img, (275,5), foreground_img)

foreground_img1 = foreground_img1.rotate(anglee, expand = True)
background_img.paste(foreground_img1, (468,248), foreground_img1)

foreground_img2 = foreground_img2.rotate(angleee, expand = True)
background_img.paste(foreground_img2, (100,214), foreground_img2)

background_img.save('masked/background1.jpg',format = 'JPEG')

image = Image.open('/content/masked/background1.jpg')
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
brighterr.save('/content/outputs/background1.jpg',format = 'JPEG')
#brighterr.save('background.jpg')
```

# 3. Saving Images:
The final enhanced images are saved in the outputs directory.
#Save or display the resulting image
```
> image.show()  # Display the image with the added text
> image.save("/content/outputs/background2.jpg")  #Save the image with the added text

# 4. Additional Image Enhancement:
Further enhancements such as brightness and contrast adjustments, text addition, etc., can be applied.

> from PIL import Image, ImageEnhance

#Load the image
> image_path = "masked/background2.jpg"  #Replace with the path to your image
> image = Image.open(image_path)

#Adjust brightness
> brightness_factor = 1  #Increase or decrease as needed (1.0 means no change)
> enhancer_brightness = ImageEnhance.Brightness(image)
> image = enhancer_brightness.enhance(brightness_factor)

#Adjust contrast
> contrast_factor = 1.2  #Increase or decrease as needed (1.0 means no change)
> enhancer_contrast = ImageEnhance.Contrast(image)
> image = enhancer_contrast.enhance(contrast_factor)

#Save or display the resulting image
> image.show()  #Display the image
> image.save("output_image.jpg")  #Save the image

#for font
#Load the image
> image = Image.open('/content/output_image.jpg')

#Define the text to be added
> text = "TEXT TO ADD"

#Define the font size and font type
> font_size = 40
> font = ImageFont.truetype("/content/fonts/calibri-italic.ttf",font_size)
#Determine the position to place the text
> text_position = (299, 50)  #Adjust the coordinates as needed

#Define text color
> text_color = (102, 51, 0)  #White color in RGB format

#Add the text to the image
> draw.text(text_position, text, fill=text_color, font=font)
#Save or display the resulting image
> image.show()  #Display the image with the added text
> image.save("/content/outputs/background2.jpg") #Save the image with the added text
```

# 5. Approach Details
This section describes the approach used in the project for generating and enhancing images.

# Background Removal
The rembg library is utilized to remove the background from the product image.

# Image Composition and Enhancement
Various techniques are applied using the Pillow library for image composition and enhancement, including resizing, rotating, and pasting images onto backgrounds.

# Saving Images
The final enhanced images are saved in the outputs directory.

# Additional Image Enhancement
Further enhancements such as brightness and contrast adjustments, text addition, etc., can be applied to the images.
