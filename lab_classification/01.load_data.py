import tensorflow as tf

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_date/',
    image_size=(224, 224),
    label_mode='categorical',
)

data = train_dataset.take(1) #dataset에서 1덩어리를 가져오겠다
for images,labels in data:
    print(images.shape)

print(train_dataset.class_names)