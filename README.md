# Generative-AI-Images

1. Clone the Repository:
 > git clone <repository_url>

2. Install Dependencies:
  Before running the code, make sure you have Python installed along with the required libraries. You can install them using pip:
 > pip install rembg Pillow

3. Download Necessary Files:
   Ensure you have the necessary images (product3.jpg, background_images/3.jpg, van2.png, 5.jpeg, 10.jpg, etc.) are placed in the appropriate directories as mentioned in the      code.
4. Open the Notebook:
Open the provided Jupyter Notebook or Python script in Google Colab or any Python environment that supports Jupyter Notebook or Google Colab.

5. Run the Code:
Run the code cells sequentially to generate and enhance the images.

6. Approach Details
   1.Background Removal:
The rembg library is used to remove the background from the product image (product3.jpg). The resulting image is saved in the masked directory.
   2. Image Composition:
Different product images and background images are composited together using the paste method in Pillow. Angles and positions are adjusted for realism.
   3. Image Enhancement:
Various enhancements such as color enhancement, sharpness adjustment, brightness, and contrast enhancement are applied to the composited images to improve their appearance.
   4. Saving Images:
The final enhanced images are saved in the outputs directory with appropriate names (background1.jpg, background2.jpg, background3.jpg, etc.).
   5. Running the Code
~ Execute the code cells in the provided notebook or Python script sequentially.
~ Ensure all necessary files are in place and paths are correctly specified.
~ Adjust parameters and values as needed to achieve desired results.
  

