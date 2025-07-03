# app.py

from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model("rice_model.h5")
class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded!"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file!"

    filepath = os.path.join('static', file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    return render_template('result.html', prediction=predicted_class, user_image=filepath)

if __name__ == '__main__':
    app.run(debug=True)
