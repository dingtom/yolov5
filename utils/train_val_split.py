import random
import os
import shutil
import cv2


# --------------------------------------划分训练测试集
path = r'D:\data\Finaloutput\Finaloutput\images'
files = [os.path.join('./images/', i) for i in os.listdir(path)]
test = True
# random.shuffle(files)
t1 = int(len(files)*0.8)  # train percent
t2 = int(len(files)*0.05)   # test percent
trains = files[:t1]
if test:
    test = files[t1:t1+t2]
    vals = files[t1+t2:]
else:
    vals = files[t1:]
    
with open(os.path.join(path.replace('images', ''), 'train.txt'), 'w') as f:
    f.write('\n'.join(trains))
with open(os.path.join(path.replace('images', ''), 'val.txt'), 'w') as f:
    f.write('\n'.join(vals))
if test:
    with open(os.path.join(path.replace('images', ''), 'test.txt'), 'w') as f:
        f.write('\n'.join(test))
    test_copy_path = os.path.join(path.replace('images', ''), 'test')
    if not os.path.exists(test_copy_path): 
        os.mkdir(test_copy_path)
    for i in test:
        i = i.split('/')[-1]
        shutil.copy(os.path.join(path, i), os.path.join(test_copy_path, i))


# ------------------------------------------不同种类的标签都合并到一个txt
# for p in ["Fish", "HumanDivers", "Plant", "Robot", "Wreck"]:
#     path = r'D:\data\Finaloutput\Finaloutput\{}'.format(p)
#     files = [i for i in os.listdir(path) if i.endswith('txt')]
#     label_path = r'D:\data\Finaloutput\Finaloutput\labels'
#     labels = os.listdir(label_path)
#     for i in files:
#         with open(os.path.join(path, i), 'r') as f:
#                 content = f.read().strip()
#         if i not in labels:
#             with open(os.path.join(label_path, i), 'w') as f:
#                 f.write(content+'\n')
#         else:
#             with open(os.path.join(label_path, i), 'a') as f:
#                 f.write(content+'\n')



# --------------------------------------label,x1,x2,y1,y2转yolo格式
# def convert(size, box):
#     dw = 1. / size[0]
#     dh = 1. / size[1]
#     x = (box[0] + box[1]) / 2.0
#     y = (box[2] + box[3]) / 2.0
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x * dw
#     w = w * dw
#     y = y * dh
#     h = h * dh
#     return (x, y, w, h)

# label = ['Fish/vertebrates', 'HumanDivers', 'Plant/sea-grass', 'Robots', 'Wrecks/ruins']
# path = r'D:\data\Finaloutput\Finaloutput\lab'
# files = os.listdir(path)
# for i in files:
#     with open(os.path.join(r'D:\data\Finaloutput\Finaloutput\labels', i), 'w') as f:
#         with open(os.path.join(path, i), 'r') as f1:
#             ls = f1.read().strip().splitlines()
#             im = cv2.imread(os.path.join(path.replace('lab', 'images'), i.replace('txt', 'bmp')))
#             height, width, _ = im.shape
#             for l in ls:
#                 cl, x1, y1, x2, y2 = l.split(',')
#                 x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
#                 bb = convert((height, width), (x1,x2,y1,y2))
#                 f.write(str(label.index(cl)) + " " + " ".join([str(a) for a in bb]) + '\n')


