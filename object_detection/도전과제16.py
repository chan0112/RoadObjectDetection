import cv2
import yolov3



path = '../data/videos/cabc30fc-e7726578.mov'
cap = cv2.VideoCapture(path)
model = yolov3.YOLOV3()
model.build()
model.load()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('../outputs/output2.wmv',fourcc,fps,(width,height))

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    result = model.predict(image)
    cv2.imshow('result', result)
    out.write(result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()