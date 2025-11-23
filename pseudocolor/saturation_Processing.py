import numpy as np
from PIL import Image
import cv2

def boost_saturation(color_img, factor=1.25):
    img = np.array(color_img).astype(np.float32) / 255.0

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    s = np.clip(s * factor, 0, 1)

    hsv_boosted = cv2.merge([h, s, v])
    boosted = cv2.cvtColor(hsv_boosted, cv2.COLOR_HSV2RGB)

    return Image.fromarray((boosted * 255).astype(np.uint8))
