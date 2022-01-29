import json

f = open('../data/labels/labels.json')
'''
label = json.load(f)
f_name = input()
for i in range(len(label)):
    if label[i]['name'] == f_name:
        for j in range(len(label[i]['labels'])):
            if 'box2d' in label[i]['labels'][j]:
                print(label[i]['labels'][j]['category'], end="")
                print(label[i]['labels'][j]['box2d'])
        break
'''
labels = json.load(f)
file_name = input()
for label in labels:
    if label['name'] == file_name:
        for l in label['labels']:
            if 'box2d' in l:
                print(l['category'], l['box2d'])
                print(l['box2d']['x1'],l['box2d']['y1'],l['box2d']['x2'],l['box2d']['y2'])