import requests
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
# Function to classify an image from URL
import ClothingClassifierModelData.init as ClothingC

ImageClassifier=ClothingC.create_model()
ImageClassifierDataPath="ClothingClassifierModelData/cp.ckpt"
ImageClassifier.load_weights(ImageClassifierDataPath)


def typeclassify_image_from_url(image_url):
    """Classifies type of clothing from image

    Args:
        image_url (str): link to image url

    Returns:
        str: Prediction of type of clothing
    """
    # Download the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert("L")  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28 (same as the Fashion MNIST images)
    image_array = np.array(image) / 255.0  # Normalize pixel values
    
    # Reshape and predict
    
    image_array = np.expand_dims(image_array, axis=0)
    prediction = ImageClassifier.predict(image_array)
    
    # Get the predicted class
    #The model thinks a shirt is a "bag" so we have 2 indices for "shirt"
    type_class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Shirt', 'Ankle boot']
    class_index = np.argmax(prediction)
    predicted_class = type_class_names[class_index]
    
    return predicted_class

#Test Use
#image_url = "https://myer-media.com.au/wcsstore/MyerCatalogAssetStore/images/40/354/3642/302/7/154846840/154846840_1_360x464.webp"  # Replace this with the URL of your image
#predicted_class = typeclassify_image_from_url(image_url)
#print("Predicted class:", predicted_class)

