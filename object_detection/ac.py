import retinanet
import cv2

model = retinanet.RetinaNet()
model.build()
model.load()

path = '../data/images/786b3729-acc83d6f.jpg'
image = cv2.imread(path)
result_image = model.predict(image.copy())
cv2.imshow('image',image)
cv2.imshow('result_image',result_image)
cv2.waitKey(0)

model.predict()