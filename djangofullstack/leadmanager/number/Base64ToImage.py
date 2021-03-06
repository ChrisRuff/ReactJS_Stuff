from PIL import Image
from io import BytesIO
import os
import cv2
import base64
import tensorflow as tf
import numpy as np

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
myModel = tf.keras.models.load_model("./number/Neural/NeuralNetwork.h5")


def convert(base64Data):
    base64Data = base64Data[22:]
    im = Image.open(BytesIO(base64.b64decode(base64Data)))
    im.thumbnail((28, 28), Image.ANTIALIAS)
    im.save("./number/data/image.png", quality=95)


def predict(base64Data):
    convert(base64Data)
    data = cv2.imread("./number/data/image.png", cv2.IMREAD_UNCHANGED)
    data = data[:, :, 3]
    resized = cv2.resize(data, dsize=(28, 28))
    test_data = np.asarray(resized)
    for x in test_data:
        print(x)
    test_data = test_data.reshape((1, 28, 28, 1))
    # test_data = np.expand_dims(test_data, axis=0)
    # test_data = tf.image.decode_png(reshaped, dtype=tf.dtypes.float32)
    test_data = tf.dtypes.cast(test_data, dtype=tf.float32)
    predictions = myModel.predict(test_data)
    print(predictions)
    predictions_argmax = np.argmax(predictions, axis=-1)
    print(predictions_argmax)
    return predictions_argmax
