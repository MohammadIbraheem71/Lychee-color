#we first need to load the model, then we need to use it to colorize the image, followed by post processing

import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2

from .luminance_processing import luminance

MODEL_PATH = "pseudocolor\colorization_model.keras"
IMG_SIZE = 128

#we load the model here
def perceptual_loss(y_true, y_pred):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    return 0.7 * mse + 0.3 * mae

#this function does the actual colorizing, post processes the image with thee
#luminance function defined in luminance_processing.py

#to colorize the photo we first scale it down to 128 * 128 as that is what the model was trained on
#this is then scaled back up to the original image size
def colorize_image(image_path, model):
    
    img = Image.open(image_path)
    gray_img = img.convert('L')

    
    gray_resized = gray_img.resize((IMG_SIZE, IMG_SIZE), Image.Resampling.LANCZOS)
    gray_arr = np.array(gray_resized, dtype=np.float32) / 255.0
    gray_arr = np.expand_dims(gray_arr, axis=(0, -1))

    #
    pred = model.predict(gray_arr, verbose=0)[0]
    #this clips the values to between 0 and 1, the model sometimes outputs values slightly below
    #or above this range
    pred = np.clip(pred, 0, 1)
    color_img = Image.fromarray((pred * 255).astype(np.uint8))
    
    #we now resize it back to the original size
    color_img = color_img.resize(img.size, Image.Resampling.LANCZOS)


    enhanced_img = luminance(color_img, gray_img)

    return gray_img, color_img, enhanced_img
    
    
def main():
    #we first load the model
    model = keras.models.load_model(MODEL_PATH, custom_objects={'perceptual_loss': perceptual_loss})
    print("✅ Model loaded!")
    
    img_path = r"pseudocolor\test_images\greyscale_car_2.JPG"
    print("processing image")
    
    gray, color, enhanced = colorize_image(img_path, model)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    
    axes[0].imshow(gray, cmap='gray')
    axes[0].set_title('Original Grayscale', fontsize=14, fontweight='bold')
    axes[0].axis('off')

    axes[1].imshow(color)
    axes[1].set_title('Basic Colorization', fontsize=14, fontweight='bold')
    axes[1].axis('off')

    axes[2].imshow(enhanced)
    axes[2].set_title('Luminance Enhanced', fontsize=14, fontweight='bold')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()
# Only run main when this file is executed directly
if __name__ == "__main__":
    main()