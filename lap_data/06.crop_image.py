import cv2

file_name = '9b975a41-1b150816.jpg'
image = cv2.imread('../data/images/'+file_name)

crop_image = image[10:500, 10:500]

cv2.imshow('image', image)
cv2.imshow('crop image', crop_image)
cv2.waitKey(0)