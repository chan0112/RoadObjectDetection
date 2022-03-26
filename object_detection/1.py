import yolov3
import retinanet
import cv2

model = yolov3.YOLO_V3()
#model = retinanet.RetinaNet() #원본 이미지를 바꿔서 그게 싫다면 copy를 이용하여 원본이미지를 보존.
model.build()
model.load()

path = '../data/images/b001a7ce-5cbc6e0b.jpg'
img = cv2.imread(path)
result = model.predict(img)
cv2.imshow('image', img)
cv2.imshow('result', result)
cv2.waitKey(0)