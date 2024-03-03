import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

# Load the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Preprocess the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

checkpoint_path = "ClothingClassifierModelData/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Build the model
def create_model():
    """Create Model for ML
    Returns:
        NeuralNetwork
    """
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='sigmoid'),
        keras.layers.Dense(128, activation='sigmoid'),
        keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Train the model
    return model


if __name__=="__main__":
    print("Printing from Main")
    cp_callback = keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=10)
    model = create_model()
    model.fit(train_images, train_labels, epochs=10,callbacks=[cp_callback])