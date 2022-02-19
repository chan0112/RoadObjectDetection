import tensorflow as tf
import os

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_date/',
    image_size=(224, 224),
    label_mode='categorical',
)

model = tf.keras.models.load_model('../models/mymodel.h5')

if not os.path.exists('../logs'):
    os.mkdir('../logs')

tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')

learning_rate = 1 #너무 높이면 loss값이 줄지 않는다. loss값이 낮아지면 낮아질수록 학습값이 느려진다.
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
    metrics=['accuracy']
)
model.fit(train_dataset, epochs=5, callbacks=[tensorboard])

if not os.path.exists('../models'):
    os.mkdir('../models')

model.save('../models/classification_model_trained.h5')
