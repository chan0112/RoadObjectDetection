import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('../models/mymodel.h5')
model.summary()

a = input()
file_name = input()
image = cv2.imread('../data/images/' + file_name)

data = np.array(image)

predict = model.predict(data)

index = np.argmax(predict)
print(index)

#print([index])