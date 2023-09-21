from tensorflow.keras.utils import img_to_array
import cv2
import numpy as np

def normalize(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (120, 120), cv2.INTER_CUBIC)
    img = img.astype('float32') / 255.0
    img_arr = img_to_array(img)
    return img_arr