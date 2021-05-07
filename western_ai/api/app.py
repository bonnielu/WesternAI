import time
from flask import Flask, jsonify, request
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.models import Sequential, load_model
import base64
import numpy as np 
import io 
import os
from PIL import Image 
import tensorflow as tf
import json



app = Flask(__name__)

def get_model():
    global model 
    # ISSUE — SavedModel file does not exist at:
    model = load_model('../../mobilenet_trained.h5')
    # model = tf.lite.TFLiteConverter.from_keras_model('../mobilenet_trained.h5')

    # model=tf.keras.models.load_model('../mobilenet_trained.h5')
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.experimental_new_converter = True
    tflite_model = converter.convert()


def preprocess_image(image):
    IMG_SIZE = (128, 128)

    image = image.convert("LA")
    image = image.resize(IMG_SIZE)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


print("Model loading...")
get_model()


@app.route('/model', methods=['POST'])
def predict():
    image_json = request.get_json()
    if not image_json:
        return jsonify({'msg': "no image uploaded"})
    
    image = image_json.replace('data:image/png;base64,','')
    decoded = base64.b64decode(image)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image)

    prediction = tflite_model.predict(processed_image)

    print(prediction)

    return jsonify({'msg': "placeholder text"})
    