#we first need to load the model, then we need to use it to colorize the image, followed by post processing

import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2


from .luminance_processing import luminance
from .saturation_Processing import boost_saturation
from .advanced_Processing import advanced_Postprocess
from .advanced_Processing import guided_color_refine

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

    # ---------- NEW: Ensemble variants ----------
    def preprocess(pil_img):
        """Resize to model size and convert to normalized array."""
        g = pil_img.resize((IMG_SIZE, IMG_SIZE), Image.Resampling.LANCZOS)
        g = np.array(g, dtype=np.float32) / 255.0
        g = np.expand_dims(g, axis=(0, -1))
        return g

    variants = []

    # 1. Original grayscale
    variants.append(preprocess(gray_img))

    # 2. Horizontally flipped grayscale
    variants.append(preprocess(gray_img.transpose(Image.FLIP_LEFT_RIGHT)))

    # 3. Gamma-corrected grayscale (adds texture variation)
    arr = np.array(gray_img).astype(np.float32) / 255.0
    gamma = np.clip((arr ** 0.9) * 255, 0, 255).astype(np.uint8)
    variants.append(preprocess(Image.fromarray(gamma)))

    # ---------- Run model on all variants ----------
    preds = []
    for v in variants:
        p = model.predict(v, verbose=0)[0]
        p = np.clip(p, 0, 1)
        preds.append(p)

    # ---------- NEW: Average LAB a/b channels ----------
    lab_list = []
    for p in preds:
        rgb = (p * 255).astype(np.uint8)
        lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
        lab_list.append(lab)

    lab_avg = np.mean(lab_list, axis=0)       # smoother, richer colors
    rgb_avg = cv2.cvtColor(lab_avg.astype(np.uint8), cv2.COLOR_LAB2RGB)
    color_img = Image.fromarray(rgb_avg)
    # --------- end of ensemble --------------

    # Resize back to original resolution
    color_img = color_img.resize(img.size, Image.Resampling.LANCZOS)

    # Post-processing steps
    enhanced_img = luminance(color_img, gray_img)
    enhanced_img = boost_saturation(enhanced_img, factor=1.2)
    enhanced_img1 = advanced_Postprocess(enhanced_img)

    guided_filter = guided_color_refine(enhanced_img)

    return gray_img, color_img, guided_filter

    
    
    
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