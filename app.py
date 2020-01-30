'''import os
from flask import Flask, render_template, request
from flask import send_from_directory
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

import warnings
warnings.filterwarnings('ignore')

import pickle
from sklearn import preprocessing
import cv2
app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
# UPLOAD_FOLDER = dir_path + '/uploads'
# STATIC_FOLDER = dir_path + '/static'
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

global npimglist

graph = tf.get_default_graph()
with graph.as_default():
    # load model at very first
   model = load_model(STATIC_FOLDER + '/' + 'AlexNetModel.hdf5')


# call model to predict an image
def api(full_path):
    #data = image.load_img(full_path)
    #data = np.expand_dims(data, axis=0)
    #data = data * 1.0 / 255

#image_data = tf.gfile.FastGFile(image_dir, 'rb').read()

    imar = cv2.imread(full_path)
    #imar = cv2.resize(cv2.imread(full_path), (224,224)).astype(np.float32)
    #imar = tf.gfile.FastGFile(full_path, 'rb').read()
    #imar = cv2.resize(imar, (224,224)).astype(np.float32)

   # imar = np.expand_dims(imar, axis=0)
#im = cv2.resize(cv2.imread(os.path.join(train_dir,image_name)), (150, 150)).astype(np.float32)
    #npimagelist = np.array([imar], dtype=np.float16) / 225.0
    img3 = cv2.cvtColor(imar, cv2.COLOR_BGR2RGB)
    img3 = cv2.resize(img3,(224,224))
    img4 = np.reshape(img3,[1,224,224,3])
    with graph.as_default():
        predicted = model.predict(img4)
        return predicted


# home page
@app.route('/')
def home():
   return render_template('index.html')


# procesing uploaded file and predict it
@app.route('/upload', methods=['POST','GET'])
def upload_file():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        full_name = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(full_name)

        #indices = {0: 'Cat', 1: 'Dog', 2: 'Invasive carcinomar', 3: 'Normal'}
        result = api(full_name)

        #predicted_class = np.asscalar(np.argmax(result, axis=1))
        #accuracy = round(result[0][predicted_class] * 100, 2)
        #label = indices[predicted_class]
        #label_binarizer = preprocessing.LabelBinarizer()
        list1 = [
            'Pepper__bell___Bacterial_spot',
            'Pepper__bell___healthy',
            'Potato___Early_blight',
            'Potato___Late_blight',
            'Potato___healthy',
            'Tomato_Bacterial_spot',
            'Tomato_Early_blight',
            'Tomato_Late_blight',
            'Tomato_Leaf_Mold',
            'Tomato_Septoria_leaf_spot',
            'Tomato_Spider_mites_Two_spotted_spider_mite',
            'Tomato__Target_Spot',
            'Tomato__Tomato_YellowLeaf__Curl_Virus',
            'Tomato__Tomato_mosaic_virus',
            'Tomato_healthy',
            ]
        #image_labels = label_binarizer.fit_transform(list1)
        PREDICTEDCLASSES2 = model.predict_classes(img4)
        label1 = PREDICTEDCLASSES2[0]
        label = reverse_mapping[label1]
    return render_template('predict.html', image_file_name = file.filename, label = label)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)
    #app.debug = True'''

from flask import *
import pickle
import numpy as np
from sklearn import preprocessing
from keras.models import load_model
import cv2
app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('index.html')


@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        imgpath = f.filename
        #fileob = open('cnn_model.pkl', 'rb')
        #model = pickle.load(fileob)
        model = load_model('s3://ec2-13-233-85-177.ap-south-1.compute.amazonaws.com/cropdisease.h5')
        imar = cv2.imread(imgpath)
        #img3 = cv2.cvtColor(imar, cv2.COLOR_BGR2RGB)
        img3 = cv2.resize(imar,(256,256),3)
        img4 = np.reshape(img3,[1,256,256,3])
        #npimagelist = np.array([imar], dtype=np.float16) / 225.0
        #label_binarizer = preprocessing.LabelBinarizer()
        list1 = [
            'Pepper__bell___Bacterial_spot',
            'Pepper__bell___healthy',
            'Potato___Early_blight',
            'Potato___Late_blight',
            'Potato___healthy',
            'Tomato_Bacterial_spot',
            'Tomato_Early_blight',
            'Tomato_Late_blight',
            'Tomato_Leaf_Mold',
            'Tomato_Septoria_leaf_spot',
            'Tomato_Spider_mites_Two_spotted_spider_mite',
            'Tomato__Target_Spot',
            'Tomato__Tomato_YellowLeaf__Curl_Virus',
            'Tomato__Tomato_mosaic_virus',
            'Tomato_healthy',
            ]
        #image_labels = label_binarizer.fit_transform(list1)
	
        PREDICTEDCLASSES2 = model.predict_classes(img4)
        #label1 = list1[PREDICTEDCLASSES2[0]]
        label1 = list1[PREDICTEDCLASSES2[0]]
        #label = reverse_mapping[label1]
        return render_template('predict.html', name=label1)

if __name__ == '__main__':
 #app.run(debug=True)


 #fileob = open('models/cnn_model.pkl', 'rb')
 #model = pickle.load(fileob)
 app.run(debug=True)
