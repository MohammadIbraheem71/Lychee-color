import numpy as np
from PIL import Image
import cv2

def luminance(color_Image, gray_Image):
   
    # Convert both images to arrays so we can edit the pixels
    color_Array = np.array(color_Image, dtype=np.float32)

    # Make sure the grayscale image matches size of the color image
    gray_Array = np.array(
        gray_Image.resize(color_Image.size, Image.Resampling.LANCZOS),
        dtype=np.float32
    )

    # Convert the color image into LAB color space
    # LAB splits the image into:
    # L  == brightness
    # A/B == color components
    bgr_Color = cv2.cvtColor(color_Array.astype(np.uint8), cv2.COLOR_RGB2BGR)
    lab_Color = cv2.cvtColor(bgr_Color, cv2.COLOR_BGR2LAB).astype(np.float32)

    # Replace the brightness channel with our grayscale brightness
    lab_Color[:, :, 0] = gray_Array
    # Convert the LAB image back into a normal RGB image
    bgr_result = cv2.cvtColor(lab_Color.astype(np.uint8), cv2.COLOR_LAB2BGR)
    rgb_result = cv2.cvtColor(bgr_result, cv2.COLOR_BGR2RGB)

    # Return as a PIL image
    return Image.fromarray(rgb_result)