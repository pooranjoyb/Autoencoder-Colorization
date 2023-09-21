"""
This is the main script for the streamlit app of Image Colorization using Autoencoders.
The script is written in Python 3.10
Author: Pooranjoy Bhattacharya
Topic : Autoencoders
"""


import streamlit as st
import pandas as pd
import streamlit as st
from PIL import Image
from packages.normalizer import normalize
from packages.colorizer import predict
import numpy as np

st.set_page_config(page_title='Image Colorizer')

button_color = """
    <style>
        .edgvbvh10 {
            background-color: #FFE6C7;
        }

        .edgvbvh10:hover{
            background-color: #FF6000;
            color: #FFE6C7;
            border: none;
        }
        
    </style>
"""

# Apply the custom CSS
st.markdown(button_color, unsafe_allow_html=True)

def main():
    st.markdown("# Landscape Image Colorizer")
    st.markdown("Welcome to Landscape Image Colorizer using Autoencoders ! \
                \n You can upload any Grayscale or Black & White image and get its corresponding Colorized Version. \
                \n #### Enjoy!")


    uploaded_file = st.file_uploader("Choose an Image", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name)

        if st.button('Colorize Image'):
            data = normalize(image)
            data = np.reshape(data, (1, 120, 120, 3))  
            predicted_array = predict(data)  
            predicted_image = Image.fromarray((predicted_array[0] * 255).astype('uint8'))

            st.image(predicted_image.resize(image.size), caption='Colorized Image')

            st.markdown("#### I could only train the model with 120 x 120 pixels due to hardware issues \
                \n Please consider this project as a demonstration of the use of Autoencoders :) \
                The Accurary of the Autoencoder model is ~60% with 20 epochs.")

            st.markdown("[Click here to checkout Kaggle Notebook](https://www.kaggle.com/code/pooranjoyb/image-colorization-autoencoder/notebook)")

            st.markdown("#### Thanks for Checking in! 😊")




if __name__ == "__main__":
    main()