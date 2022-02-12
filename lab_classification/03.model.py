import tensorflow as tf

model = tf.keras.applications.MobileNet( #여러 알고리즘 중 applications에 있는 mobilenet 사용
    input_shape=(224, 224, 3),
    include_top=False, #output classes 삭제
    weights='imagenet' #imagenet으로 학습된 것을 가져옴
)
#마지막 튜닝값만 바꾸겠다.

model.trainable = False #trainable params 가 0이됨

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(), #평균내서 변환
    tf.keras.layers.Dense(9), #1024개를 내가 원하는 다른 개수로 변환해주는 층 , params 생김 , 완전연결계층(신경망)
    tf.keras.layers.Softmax() #Dense를 이용해 만든 9개의 총합을 1로 만듦.
])

model.summary()
