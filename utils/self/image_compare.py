import cv2
import os
from tqdm import tqdm
import numpy as np
from collections import Counter

class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hexs = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
                '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        self.palette = [self.hex2rgb(f'#{c}') for c in hexs]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))
colors = Colors()  # create instance for 'from utils.plots import colors'

# 把label画到图像上和预测的图像对比
pre_path = r'runs/detect/exp2'
images_path = r'/home/tomding/hdd/data/hand/test'

save_path = pre_path + '/compare'
if not os.path.exists(save_path): os.mkdir(save_path) 

with open(os.path.join(images_path.replace('test', 'labels'), 'classes.txt'), "r") as f:
        classes = f.read().splitlines()

for i in tqdm(os.listdir(images_path)):
    class_ids = []
    pre_ids = []  # 收集预测值用来对比
    img = cv2.imread(os.path.join(images_path, i))
    with open(os.path.join(images_path.replace('test', 'labels'), i.replace('jpg', 'txt')), "r") as f:
        labels = f.read().splitlines()
    for label in labels:
        label_parts = label.split()
        try:
            x, y, w, h = map(float, label_parts[1:])
            class_id = int(label_parts[0])
            class_ids.append(class_id)
        except:
            print(i, label)
        left, top, right, bottom = int((x - w / 2) * img.shape[1]), int((y - h / 2) * img.shape[0]), int((x + w / 2) * img.shape[1]), int((y + h / 2) * img.shape[0])
        c = colors(int(class_id), True)  # 颜色
        cv2.rectangle(img, (left, top), (right, bottom), c, 3, cv2.LINE_AA)
        cv2.putText(img, str(classes[class_id]), (left, int(top - 5)), cv2.FONT_HERSHEY_SIMPLEX, 3, c, thickness=3, lineType=cv2.LINE_AA)
        cv2.putText(img, 'label', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)

    pre_img = cv2.imread(os.path.join(pre_path, i))
    cv2.putText(pre_img, 'predict', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)

    try:
        with open(os.path.join(pre_path, 'labels', i.replace('jpg', 'txt')), "r") as f:
            pres = f.read().splitlines()
    except:
        print('no such file', i)
    for pre in pres:
        pre_parts = pre.split()
        try:
            x, y, w, h = map(float, pre_parts[1:])
            pre_id = int(pre_parts[0])
            pre_ids.append(pre_id)
        except:
            print(i, pre)
        pre_left, pre_top, pre_right, pre_bottom = int((x - w / 2) * img.shape[1]), int((y - h / 2) * img.shape[0]), int((x + w / 2) * img.shape[1]), int((y + h / 2) * img.shape[0])

    if Counter(class_ids) != Counter(pre_ids):
        merged_img = np.concatenate((img, pre_img), axis=1)
        cv2.imwrite(os.path.join(save_path, i), merged_img)
