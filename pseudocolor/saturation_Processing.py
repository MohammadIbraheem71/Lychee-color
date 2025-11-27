import numpy as np
from PIL import Image
import cv2

def boost_saturation(color_img, factor=1.25):
    #change image into array and scale it between 0 and 1
    img = np.array(color_img).astype(np.float32) / 255.0

    #convert image from rgb to hsv color
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    #make the saturation stronger
    s = np.clip(s * factor, 0, 1)

    #put h s v back together
    hsv_boosted = cv2.merge([h, s, v])

    #change hsv back to rgb image
    boosted = cv2.cvtColor(hsv_boosted, cv2.COLOR_HSV2RGB)

    #give final image back
    return Image.fromarray((boosted * 255).astype(np.uint8))
