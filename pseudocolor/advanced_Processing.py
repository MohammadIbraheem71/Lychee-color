import cv2
import numpy as np
from PIL import Image
import pywt 
from scipy.stats import zscore


def color_Harmonize_Lab(color_img):
    
    # This step fixes unnatural or uneven colors produced by the model.
    # We move the image into LAB space and normalize only the color channels
    # (A and B). This makes the overall color palette more consistent.
    

    # Convert to LAB (better for color manipulation than RGB)
    lab = cv2.cvtColor(np.array(color_img), cv2.COLOR_RGB2LAB).astype(np.float32)
    L, a, b = cv2.split(lab)

    # Standardize color channels (remove weird color cast)
    a_z = zscore(a, axis=None)
    b_z = zscore(b, axis=None)

    # Bring values back into valid LAB range (128 = neutral midpoint)
    # Multiplying by 10 gives stronger but natural color contrast
    a_h = np.clip((a_z * 10 + 128), 0, 255)
    b_h = np.clip((b_z * 10 + 128), 0, 255)

    # Put LAB image back together and convert to RGB
    lab_h = cv2.merge([L, a_h, b_h])
    rgb_h = cv2.cvtColor(lab_h.astype(np.uint8), cv2.COLOR_LAB2RGB)
    
    return Image.fromarray(rgb_h)


def wavelet_Enhance(color_img, wave='db1', level=2, gain=1.2):
    
    # Enhances fine texture and details using Wavelet transforms.
    # The idea:
    # - Break image into low-frequency (smooth) and high-frequency (details)
    # - Boost only high-frequency parts to make the image sharper and more realistic
    # Without causing noise like traditional sharpening filters.
    

    img_arr = np.array(color_img).astype(np.float32)

    # Process each color channel separately
    channels = cv2.split(img_arr)
    enhanced_Channels = []

    for ch in channels:
        # Multi-level wavelet decomposition (splits smooth + detailed areas)
        coeffs = pywt.wavedec2(ch, wave, level=level)

        # First element is the smooth part — leave it unchanged
        coeffs_mod = [coeffs[0]]

        # Enhance all detail layers
        for detail in coeffs[1:]:
            cH, cV, cD = detail

            # Boost horizontal, vertical, diagonal details
            cH *= gain
            cV *= gain
            cD *= gain

            coeffs_mod.append((cH, cV, cD))

        # Reconstruct enhanced channel
        ch_enh = pywt.waverec2(coeffs_mod, wave)
        ch_enh = np.clip(ch_enh, 0, 255)
        enhanced_Channels.append(ch_enh.astype(np.uint8))

    # Combine enhanced RGB channels back into a single image
    image_Enhanced = cv2.merge(enhanced_Channels)
    return Image.fromarray(image_Enhanced)


def advanced_Postprocess(color_Image):
    
    # Full enhancement pipeline:
    # 1. Fixes inconsistent colors (harmonization)
    # 2. Sharpens fine details without creating noise (wavelet enhancement)
    # Result: More realistic, smooth, and visually appealing output.
    

    # Step 1: Make color distribution more natural
    harmonized_Image = color_Harmonize_Lab(color_Image)

    # Step 2: Bring back texture and realism
    enhanced_Image = wavelet_Enhance(harmonized_Image)

    return enhanced_Image