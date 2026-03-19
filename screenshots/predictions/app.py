from flask import Flask, render_template, request, redirect
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load the 15-class CNN model
model = load_model('model/vegetable_model.h5')

# CRITICAL: Labels MUST be in alphabetical order to match Keras training
classes = [
    'Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 
    'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 
    'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files: return redirect('/')
    file = request.files['file']
    if file.filename == '': return redirect('/')
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 1. Load image with standard target size
    img = image.load_img(filepath, target_size=(150, 150))
    
    # 2. Convert to array and Normalize (1./255)
    # This is the most common reason for 'Wrong Results'
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  
    
    # 3. Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # 4. Generate Prediction
    prediction_scores = model.predict(img_array)
    prediction_index = np.argmax(prediction_scores)
    confidence = np.max(prediction_scores) * 100
    
    result_label = classes[prediction_index]
    
    return render_template('prediction.html', 
                           label=result_label, 
                           confidence=round(confidence, 2), 
                           img_name=file.filename)

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)