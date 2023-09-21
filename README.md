# Image Colorization: Autoencoder

Image colorization using autoencoders is an innovative approach that infuses grayscale images with vibrant hues. Autoencoders, a type of neural network, learn to encode and decode images, forming an internal representation of input data.

## Table of Contents

- [Introduction](#image-colorization-autoencoder)
- [Project Overview](#project-overview)
- [Data Preparation](#data-preparation)
- [Model Architecture](#model-architecture)
- [Model Training](#model-training)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Project Overview

The aim of this project is to automatically add color to grayscale images using an autoencoder architecture. The process involves several steps, including data preparation, defining the model architecture, training the model, and deploying it for practical use.

## Data Preparation

For this project, a suitable dataset of grayscale images and their corresponding color versions is required. The dataset should be preprocessed to ensure compatibility with the model architecture. This process may include resizing, normalization, and splitting into training and validation sets.

## Model Architecture

The autoencoder architecture consists of an encoder and a decoder. The encoder reduces the dimensionality of the input grayscale image, extracting essential features. The decoder then uses these features to reconstruct the colorized version of the image. The specific architecture details, such as layer sizes, activation functions, and loss functions, are defined in the code.

## Model Training

The training phase involves optimizing the model's parameters to minimize the difference between the predicted colorized images and the ground truth color images. This is achieved by feeding the grayscale images into the autoencoder and adjusting the weights.

## Dependencies

- Python 3.10.6
- Tensorflow
- NumPy
- Pillow
- Streamlit

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```
## Usage

This project uses Streamlit for deployment. Streamlit is a web application framework that allows for easy integration of machine learning models into web applications. To run the Streamlit application script and follow the instructions provided.

```bash
streamlit run app.py
```

## License 

Distributed under the MIT License. 
[MIT](LICENSE)