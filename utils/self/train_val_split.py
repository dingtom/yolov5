import random
import os
import shutil
import cv2
# path = r'D:\data\fire\json'
# files = [i.replace('json', 'txt') for i in os.listdir(path)]
# with open(os.path.join(path, 'all.txt'), 'w') as f:
#     f.write('\n'.join(files))

# --------------------------------------划分训练测试集
is_test = True
extra_test = False # 把测试图片提出来
path = r'/srv/samba/dingwenchao/hdd/SeaShips/images'
files = [os.path.join('./images/', i) for i in os.listdir(path)]
random.shuffle(files)
t1 = int(len(files)*0.8)  # train percent
t2 = int(len(files)*0.05)   # test percent
trains = files[:t1]
if is_test:
    test = files[t1:t1+t2]
    vals = files[t1+t2:]
else:
    vals = files[t1:]
with open(os.path.join(path.replace('images', ''), 'train.txt'), 'w') as f:
    f.write('\n'.join(trains))
with open(os.path.join(path.replace('images', ''), 'val.txt'), 'w') as f:
    f.write('\n'.join(vals))
if is_test:
    with open(os.path.join(path.replace('images', ''), 'test.txt'), 'w') as f:
        f.write('\n'.join(test))
    if extra_test:
        test_copy_dir = os.path.join(path.replace('images', ''), 'test')
        if not os.path.exists(test_copy_dir): 
            os.mkdir(test_copy_dir)
        for i in test:
            i = i.split('/')[-1]
            shutil.copy(os.path.join(path, i), os.path.join(test_copy_dir, i))


# ------------------------------------------不同种类的标签都合并到一个txt
# for p in ["Fish", "HumanDivers", "Plant", "Robot", "Wreck"]:
#     path = r'D:\data\Finaloutput\Finaloutput\{}'.format(p)
#     files = [i for i in os.listdir(path) if i.endswith('txt')]
#     label_dir = r'D:\data\Finaloutput\Finaloutput\labels'
#     labels = os.listdir(label_dir)
#     for i in files:
#         with open(os.path.join(path, i), 'r') as f:
#                 content = f.read().strip()
#         if i not in labels:
#             with open(os.path.join(label_dir, i), 'w') as f:
#                 f.write(content+'\n')
#         else:
#             with open(os.path.join(label_dir, i), 'a') as f:
#                 f.write(content+'\n')
