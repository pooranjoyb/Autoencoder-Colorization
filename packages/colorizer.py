import tensorflow as tf
from tensorflow.keras.models import load_model

AutoEncoder = load_model('./model/AutoEncoder.h5')


def predict(arr):
    colorized_img = AutoEncoder.predict(arr)
    return colorized_img