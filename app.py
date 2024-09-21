import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('my_model.h5')

# Define class labels based on your model
class_labels = ['Alstonia Scholaris', 'Arjun', 'Basil', 'Chinar', 'Gauva', 'Jamun', 'Jatropha', 'Lemon', 'Mango', 'Pomegranate', 'Pongamia Pinnata']  

def preprocess_image(img):
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img = img.resize((224, 224))  # Update this size to match your model's input size
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize if required
    return img_array

st.title("Plant Identidfication by Batch 45")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    img_array = preprocess_image(img)
    
    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    
    st.write(f"Prediction: {class_labels[predicted_class]}")
