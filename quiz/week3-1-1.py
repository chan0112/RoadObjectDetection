import json
import cv2
import os

f = open('../data/labels/labels.json')
labels = json.load(f)

if not os.path.exists('../classification_date'):
    os.mkdir('../classification_date')

file_name = input()
image = cv2.imread('../data/images/' + file_name)
cnt = 0
for label in labels:
    if label['name'] == file_name:
        for l in label['labels']:
            if 'box2d' in l:
                x1 = int(l['box2d']['x1'])
                y1 = int(l['box2d']['y1'])
                x2 = int(l['box2d']['x2'])
                y2 = int(l['box2d']['y2'])

                crop_image = image[y1:y2 + 1, x1:x2 + 1]
                # resize_image = cv2.resize(crop_image, (224, 224))

                if not os.path.exists('../classification_date/' + l['category']):
                    os.mkdir('../classification_date/' + l['category'])

                if os.path.exists('../classification_date/' + l['category']):
                    cv2.imwrite('../classification_date/' + l['category'] + '/' + str(cnt) + '.jpg', crop_image)

                cnt += 1