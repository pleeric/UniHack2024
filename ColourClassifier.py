import requests
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
import ColourClassifier as ColourC

ColourClassifier=ColourC.create_model()
ColourClassifierDataPath="ColourClassifierModelData/cp.ckpt"
ColourClassifier.load_weights(ColourClassifierDataPath)


def colourclassify_image_from_url(image_url):
    """Determines main/average/most prominent colour of image

    Args:
        image_url (str): link to image

    Returns:
        str: colour guess
    """
    # Download the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert("L")  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image_array = np.array(image) / 255.0
    
    # Reshape
    
    image_array = np.expand_dims(image_array, axis=0)
    
    # Predict (The model thinks a shirt is a "bag" so we have 2 indices for "shirt")
    type_class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Shirt', 'Ankle boot']
    
    prediction = ColourClassifier.predict(image_array)
    class_index = np.argmax(prediction)
    predicted_class = type_class_names[class_index]
    
    return predicted_class
