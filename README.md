# Image Colorization: Autoencoder

Image colorization using autoencoders is an innovative approach that infuses grayscale images with vibrant hues. Autoencoders, a type of neural network, learn to encode and decode images, forming an internal representation of input data. The aim of this project is to automatically add color to grayscale images using an autoencoder architecture. The process involves several steps, including data preparation, defining the model architecture, training the model, and deploying it for practical use.

## Data Preparation

![training dataset](https://github.com/pooranjoyb/Autoencoder-Colorization/blob/master/data/images/dataset.png)

For this project, a suitable dataset of grayscale images and their corresponding color versions is required. The dataset should be preprocessed to ensure compatibility with the model architecture. This process may include resizing, normalization, and splitting into training and validation sets.

## Model Architecture

<img src="https://github.com/pooranjoyb/Autoencoder-Colorization/blob/master/data/images/architecture.png" width="50%" alt="Architecture"></img>

- **The Encoder architecture** is a convolutional neural network segment designed for image feature extraction.
- It begins with an input layer accommodating (120, 120, 3) images. Each convolutional layer is accompanied by batch normalization and max pooling.
- Sequentially, the number of filters increases (64, 128, 256, 512), enabling hierarchical feature capture.
- This architecture progressively abstracts image features for image colorization, providing efficient information encapsulation through its layers.
- Then, **Decoder**, a pivotal component of the Autoencoder, reconstructs images from a compact  representation. Initiated by an input layer shaped to match the Encoder's output, the architecture 
unfolds with batch normalization. Conv2DTranspose layers reverse convolution, expanding the representation with strides of 2 and batch normalization.

## Model Training
The training phase involves optimizing the model's parameters to minimize the difference between the predicted colorized images and the ground truth color images. This is achieved by feeding the grayscale images into the autoencoder and adjusting the weights. 

<img src="https://github.com/pooranjoyb/Autoencoder-Colorization/blob/master/data/images/train.png" width="50%" />

- The model was trained with an optimal 14 epochs and with 120 x 120 grayscale and color landscape image sets.

### Sample Output

![output](https://github.com/pooranjoyb/Autoencoder-Colorization/blob/master/data/images/output.png)

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

**You can also click [here](https://image-colorizer.onrender.com/) to view the deployment**

## License 

Distributed under the MIT License. 
[MIT](LICENSE)
