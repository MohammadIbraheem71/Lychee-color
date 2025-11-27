import numpy as np
from PIL import Image
import cv2

def luminance(color_Image, gray_Image):
   
    #convert both images to arrays so we can change the pixels
    color_Array = np.array(color_Image, dtype=np.float32)

    #make sure gray image has same size as color image
    gray_Array = np.array(
        gray_Image.resize(color_Image.size, Image.Resampling.LANCZOS),
        dtype=np.float32
    )

    #change color image from rgb to lab color
    #lab means l is light and a b are colors
    bgr_Color = cv2.cvtColor(color_Array.astype(np.uint8), cv2.COLOR_RGB2BGR)
    lab_Color = cv2.cvtColor(bgr_Color, cv2.COLOR_BGR2LAB).astype(np.float32)

    #put gray image into the light channel of lab
    lab_Color[:, :, 0] = gray_Array

    #change lab back to normal rgb image
    bgr_result = cv2.cvtColor(lab_Color.astype(np.uint8), cv2.COLOR_LAB2BGR)
    rgb_result = cv2.cvtColor(bgr_result, cv2.COLOR_BGR2RGB)

    #give final image back
    return Image.fromarray(rgb_result)
