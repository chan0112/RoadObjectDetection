import json
import cv2
import os

cnt = 0
f = open('../data/labels/labels.json')
labels = json.load(f)

if not os.path.exists('../classification_date'):
    os.mkdir('../classification_date')


file_names = os.listdir('../data/images')

for j in range(len(file_names)):
    image = cv2.imread('../data/images/' + file_names[j])

    for label in labels:
        if label['name'] in file_names:
            for l in label['labels']:

                if 'box2d' in l:
                    x1 = int(l['box2d']['x1'])
                    y1 = int(l['box2d']['y1'])
                    x2 = int(l['box2d']['x2'])
                    y2 = int(l['box2d']['y2'])

                    crop_image = image[y1:y2, x1:x2]
                    #resize_image = cv2.resize(crop_image, (224, 224))

                    if not os.path.exists('../classification_date/'+l['category']):
                        os.mkdir('../classification_date/'+l['category'])

                    if os.path.exists('../classification_date/'+l['category']):
                        cv2.imwrite(f'../classification_date/{l["category"]}/{str(cnt)}.jpg', crop_image)

                cnt += 1



