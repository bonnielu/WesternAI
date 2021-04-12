import time
from flask import Flask, jsonify, request
from keras.preprocessing.image import ImageDataGenerator

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/model', methods=['POST'])
def get_model():
    image_json = request.json
    if not image_json:
        return jsonify({'msg': "no image uploaded"})
    
    image = image_json.get('image')

    IMG_SIZE = (128, 128)
    core_idg = ImageDataGenerator(samplewise_center=True, 
            samplewise_std_normalization=True, 
            horizontal_flip = True, 
            vertical_flip = False, 
            height_shift_range= 0.05, 
            width_shift_range=0.1, 
            rotation_range=5, 
            shear_range = 0.1,
            fill_mode = 'reflect',
            zoom_range=0.15)

    return jsonify({'msg': "placeholder text"})
    