import os
import cv2
import shutil
from tqdm import tqdm
import random
# ----------------------------------------------------------------删除无效图片
# path = 'd:/data/mask'
# for i in os.listdir(path):
#     full_dir = os.path.join(path, i)
#     image = cv2.imread(full_dir)
#     if image is None:
#         print(full_dir)
#         os.remove(full_dir)

# --------------------------------------------------------------复制一个images文件夹里有的label文件


def copy_dir_need(need_dir, source_dir):
    need_list = os.listdir(need_dir)
    need_list = [i.replace('txt', 'jpg') for i in need_list]

    save_dir = need_dir.replace('labels', 'images1')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in tqdm(need_list):
        try:
            shutil.copy(os.path.join(source_dir, i), os.path.join(save_dir, i))
        except:
            print(i)
            continue

# --------------------------------------------------------------复制txt里有的文件


def copy_txt_need(image_dir, need_txt, save_dir):
    with open(need_txt) as f:
        need_list = f.read().strip().split()
    need_list = [i.split('/')[-1] for i in need_list]

    # need_dir = r'D:\data\UA-DETRAC-G2\1'
    # need_list = os.listdir(need_dir)
    # need_list = [i.replace('jpg', 'txt') for i in need_list]

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in tqdm(os.listdir(image_dir)):
        if i in need_list:
            shutil.copy(os.path.join(image_dir, i), os.path.join(save_dir, i))
            # os.remove(os.path.join(path, i))


# --------------------------------------------------------------删除多余文件
def del_reduent():
    label_dir = r"E:\Download\fire\labels"
    label_list = os.listdir(label_dir)

    image_dir = r'E:\Download\fire\images'
    image_list = os.listdir(image_dir)
    # main_list = [i.replace('.txt', '') for i in main_list]
    # 把没有标签的图片删掉
    for i in image_list:
        if i.replace('jpg', 'txt') not in label_list:
            os.remove(os.path.join(image_dir, i))

# --------------------------------------------------------------删除某些类别
def del_by_class(label_dir):
    # {'person': 20810, 'falling': 26, 'fall': 10620, '10+': 1790, 'dog': 1}
    not_need = ['falling', 'dog', '10+']
    label_list = os.listdir(label_dir)
    image_dir = label_dir.replace('labels', 'images')
    with open(os.path.join(label_dir, 'classes.txt')) as f:
        classes = f.read().strip().split()

    for i in tqdm(label_list):
        if i == 'classes.txt':
            continue
        labels = ''
        with open(os.path.join(label_dir, i), 'r') as f:
            content = f.readlines()
            for line in content:
                if not line.isspace():
                    lxywh = line.split(" ")
                    cls = lxywh[0]
                    if classes[int(cls)] in not_need:
                        continue
                    labels += ' '.join(lxywh) + '\n'
        if len(labels) == 0:
            os.remove(os.path.join(label_dir, i))
            os.remove(os.path.join(image_dir, i.replace('txt', 'jpg')))
        else:
            with open(os.path.join(label_dir, i), "w") as f:
                f.write(labels)


#  -------------------------------------------------------------统计数据集中每个类别的数量
def count_class(label_dir):
    label_list = os.listdir(label_dir)
    class_dic = {}
    for i in label_list:
        with open(os.path.join(label_dir, i), 'r') as f:
            content = f.readlines()
            for line in content:
                cls = line.strip().split()[0]
                if cls in list(class_dic.keys()):
                    class_dic[cls] += 1
                else:
                    class_dic[cls] = 1
    class_dic = sorted(class_dic.items(), key=lambda item: item[0])
    print(class_dic)

# # ------------------------------------------------------------根据标签内容把正确的标签提出来


def get_right_label(label_dir):
    label_list = os.listdir(label_dir)
    # save_dir = r"d:/data/labels"
    # if not os.path.exists(save_dir): os.mkdir(save_dir)
    for i in label_list:
        if i == 'classes.txt':
            continue
        with open(os.path.join(label_dir, i), 'r') as f:
            content = f.readlines()
            for line in content:
                cls = line.strip().split()[0]
                if cls != '0':
                    print(i)
                    return
            # if len(content)>3:
            #     continue
            # else:
            #     shutil.copy(os.path.join(label_dir, i), os.path.join(save_dir, i))


# # -----------------------------------------------------把某些类别index改成其他的
def replace_label(label_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i in tqdm(os.listdir(label_dir)):
        labels = ''
        f = open(os.path.join(label_dir, i), 'r', encoding='utf-8')
        for line in f.readlines():
            if not line.isspace():
                lxywh = line.split(" ")
                if lxywh[0] == '4':
                    lxywh[0] = '0'
                labels += ' '.join(lxywh) + '\n'
        with open(os.path.join(save_dir, i), "w") as f:
            f.write(labels)


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# ------------------------------------------不同种类的标签都合并到一个txt
def merge_txt():
    for p in ["Fish", "HumanDivers", "Plant", "Robot", "Wreck"]:
        path = r'D:\data\Finaloutput\Finaloutput\{}'.format(p)
        files = [i for i in os.listdir(path) if i.endswith('txt')]
        label_dir = r'D:\data\Finaloutput\Finaloutput\labels'
        labels = os.listdir(label_dir)
        for i in files:
            with open(os.path.join(path, i), 'r') as f:
                content = f.read().strip()
            if i not in labels:
                with open(os.path.join(label_dir, i), 'w') as f:
                    f.write(content+'\n')
            else:
                with open(os.path.join(label_dir, i), 'a') as f:
                    f.write(content+'\n')


# --------------------------------------label,x1,x2,y1,y2转yolo格式
def labelxy2yolo():
    label = ['Fish/vertebrates', 'HumanDivers',
             'Plant/sea-grass', 'Robots', 'Wrecks/ruins']
    path = r'D:\data\Finaloutput\Finaloutput\lab'
    files = os.listdir(path)
    for i in files:
        with open(os.path.join(r'D:\data\Finaloutput\Finaloutput\labels', i), 'w') as f:
            with open(os.path.join(path, i), 'r') as f1:
                ls = f1.read().strip().splitlines()
                im = cv2.imread(os.path.join(path.replace(
                    'lab', 'images'), i.replace('txt', 'bmp')))
                height, width, _ = im.shape
                for l in ls:
                    cl, x1, y1, x2, y2 = l.split(',')
                    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
                    bb = convert((height, width), (x1, x2, y1, y2))
                    f.write(str(label.index(cl)) + " " +
                            " ".join([str(a) for a in bb]) + '\n')


# ------------------------------------------同一张照片不同类别被分开标注了,把标签合到一起
def merge_same_picture(label_dir, image_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    fires = [i for i in os.listdir(label_dir) if i.startswith('fire')]
    smokes = [i for i in os.listdir(label_dir) if i.startswith('smoke')]
    print('label num：{} : {}'.format(len(smokes), len(fires)))
    for i in fires:
        if i.replace('fire', 'smoke') in smokes:
            with open(os.path.join(label_dir, i), 'r') as f:
                content = f.read()
            with open(os.path.join(label_dir, i.replace('fire', 'smoke')), 'r') as f:
                content += f.read()
            with open(os.path.join(save_dir, i), 'w') as f:
                f.write(content)
        else:
            shutil.move(os.path.join(label_dir, i), os.path.join(save_dir, i))


# ------------------------------------------save same classes label to one txt
def merge_txt(label_dir):
    label_list = os.listdir(label_dir)
    with open(os.path.join(label_dir, 'classes.txt')) as f:
        classes = f.read().strip().split()
    classes_files = {key : [] for key in classes}
    for i in label_list:
        if i == 'classes.txt':
            continue
        with open(os.path.join(label_list, i), 'r') as f:
            content = f.read().strip()
    
            with open(os.path.join(label_dir, i), 'a') as f:
                f.write(content+'\n')

def count_shuffle(root_dir, train_ratio=0.8, val_ratio=0.2, test_ratio=0, extra_test=True):
    """统计类别标签数，把数量比较少类别的文件名保存一下方便后面看效果，并shuffle数据，生成训练测试集
    Args:
        root_dir (_type_): 数据根目录，下有images,labels文件夹
        train_ratio (float, optional): _description_. Defaults to 0.8.
        val_ratio (float, optional): _description_. Defaults to 0.2.
        test_ratio (int, optional): _description_. Defaults to 0.
        extra_test (bool, optional): 把测试集图片拿出来放在一个test文件夹. Defaults to False.
        extra_test (bool, optional): . Defaults to False.
    """
    label_dir = os.path.join(root_dir, 'labels')
    label_list = os.listdir(label_dir)
    with open(os.path.join(label_dir, 'classes.txt')) as f:
        classes = f.read().strip().split()
    classes_files = {key : [] for key in classes}
    for i in tqdm(label_list):
        if i == 'classes.txt':
            continue
        with open(os.path.join(label_dir, i), 'r') as f:
            content = f.readlines()
            for line in content:
                if not line.isspace():
                    lxywh = line.split(" ")
                    cls = int(lxywh[0])
                    classes_files[classes[cls]].append('./images/' + i.replace('txt', 'jpg'))
    sorted_dict = dict(sorted(classes_files.items(), key=lambda x: len(x[1])))
    classes_num = {k : len(v) for k, v in sorted_dict.items()}
    print('-'*50+ 'classes label num count' + '-'*50)
    print(classes_num)

    train_list, val_list, test_list, include_list = [], [], [], []

    for k, v in tqdm(sorted_dict.items()):
        samples = [i for i in v if i not in include_list]
        include_list.extend(samples)
        random.shuffle(samples)
        num = len(samples)
        train_num = int(num*train_ratio)  
        val_num = int(num*val_ratio)   
        if test_ratio > 0:
            val_list.extend(samples[train_num:train_num+val_num])
            test_list.extend(samples[train_num+val_num:])
        else:
            val_list.extend(samples[train_num:])
        train_list.extend(samples[:train_num])
    with open(os.path.join(root_dir, 'few.txt'), 'w') as f:
        f.write('\n'.join(classes_num))
        for k, l in classes_num.items():
            if l < 100:   #  标签数小于100的类别，标签文件名保存一下
                f.write('\n' + '-'*10 + k + '-'*10+'\n')
                f.write('\n'.join(sorted_dict[k]))
    with open(os.path.join(root_dir, 'train.txt'), 'w') as f:
        f.write('\n'.join(train_list))
    with open(os.path.join(root_dir, 'val.txt'), 'w') as f:
        f.write('\n'.join(val_list))
    if test_ratio > 0:
        with open(os.path.join(root_dir, 'test.txt'), 'w') as f:
            f.write('\n'.join(test_list))
        if extra_test:
            test_copy_dir = os.path.join(root_dir, 'test')
            if not os.path.exists(test_copy_dir): 
                os.mkdir(test_copy_dir)
            for i in test_list:
                i = i.split('.')[-1]
                shutil.copy(os.path.join(root_dir, i), os.path.join(test_copy_dir, i))
