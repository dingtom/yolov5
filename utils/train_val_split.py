import random
import os
import shutil

# path = r'D:\sale\DeepLearningSlideCaptcha2\data\captcha\images'
# files = [os.path.join('./images/', i) for i in os.listdir(path)]
# test = False
# # random.shuffle(files)
# t1 = int(len(files)*0.8)  # train percent
# t2 = int(len(files)*0.05)   # test percent
# trains = files[:t1]
# if test:
#     test = files[t1:t1+t2]
#     vals = files[t1+t2:]
# else:
#     vals = files[t1:]
    
# with open(os.path.join(path.replace('images', ''), 'train.txt'), 'w') as f:
#     f.write('\n'.join(trains))
# with open(os.path.join(path.replace('images', ''), 'val.txt'), 'w') as f:
#     f.write('\n'.join(vals))
# if test:
#     with open(os.path.join(path.replace('images', ''), 'test.txt'), 'w') as f:
#         f.write('\n'.join(test))
#     test_copy_path = os.path.join(path.replace('images', ''), 'test\images')
#     if not os.path.exists(test_copy_path): 
#         os.mkdir(test_copy_path)
#     for i in test:
#         i = i.split('/')[-1]
#         shutil.copy(os.path.join(path, i), os.path.join(test_copy_path, i))


# import os

# import shutil
# import random

# random.seed(0)


# def split_data(file_path,xml_path, new_file_path, train_rate, val_rate, test_rate):
#     each_class_image = []
#     each_class_label = []
#     for image in os.listdir(file_path):
#         each_class_image.append(image)
#     for label in os.listdir(xml_path):
#         each_class_label.append(label)
#     data=list(zip(each_class_image,each_class_label))
#     total = len(each_class_image)
#     random.shuffle(data)
#     each_class_image,each_class_label=zip(*data)
#     train_images = each_class_image[0:int(train_rate * total)]
#     val_images = each_class_image[int(train_rate * total):int((train_rate + val_rate) * total)]
#     test_images = each_class_image[int((train_rate + val_rate) * total):]
#     train_labels = each_class_label[0:int(train_rate * total)]
#     val_labels = each_class_label[int(train_rate * total):int((train_rate + val_rate) * total)]
#     test_labels = each_class_label[int((train_rate + val_rate) * total):]

#     for image in train_images:
#         print(image)
#         old_path = file_path + '/' + image
#         new_path1 = new_file_path + '/' + 'train' + '/' + 'images'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + image
#         shutil.copy(old_path, new_path)

#     for label in train_labels:
#         print(label)
#         old_path = xml_path + '/' + label
#         new_path1 = new_file_path + '/' + 'train' + '/' + 'labels'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + label
#         shutil.copy(old_path, new_path)

#     for image in val_images:
#         old_path = file_path + '/' + image
#         new_path1 = new_file_path + '/' + 'val' + '/' + 'images'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + image
#         shutil.copy(old_path, new_path)

#     for label in val_labels:
#         old_path = xml_path + '/' + label
#         new_path1 = new_file_path + '/' + 'val' + '/' + 'labels'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + label
#         shutil.copy(old_path, new_path)

#     for image in test_images:
#         old_path = file_path + '/' + image
#         new_path1 = new_file_path + '/' + 'test' + '/' + 'images'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + image
#         shutil.copy(old_path, new_path)

#     for label in test_labels:
#         old_path = xml_path + '/' + label
#         new_path1 = new_file_path + '/' + 'test' + '/' + 'labels'
#         if not os.path.exists(new_path1):
#             os.makedirs(new_path1)
#         new_path = new_path1 + '/' + label
#         shutil.copy(old_path, new_path)


# if __name__ == '__main__':
#     file_path = "E:\Download\dataset\images"
#     xml_path = 'E:\Download\dataset\labels'
#     new_file_path = "e:\Download\dataset\data"
#     split_data(file_path,xml_path, new_file_path, train_rate=0.7, val_rate=0.1, test_rate=0.2)

