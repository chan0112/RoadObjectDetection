import tensorflow as tf
import cv2
import numpy as np

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_date/',
    image_size=(224, 224),
    label_mode='categorical',
)
model = tf.keras.models.load_model('../models/classification_model_traines.h5')
model.summary()

class_names = train_dataset.class_names

class_name = input()
file_name = input()

image = cv2.imread('../classification_date/'+ class_name+ '/'+ file_name)
resize_image = cv2.resize(image,(224,224))
data = np.array([resize_image])

predict = model.predict(data)
print(predict
      )
index = np.argmax(predict)
print(index)

print(class_name[index])

cv2.imshow('image',image)
cv2.waitKey(0)