#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tqdm import tqdm
import xml.etree.ElementTree as ET
import os
from tqdm import tqdm

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


def convert_annotation(img_xml, xml_dir, txt_dir):
    in_file = open(os.path.join(xml_dir, img_xml))

    out_file = open(os.path.join(txt_dir, img_xml.replace('xml', 'txt')), 'w')  # 生成txt格式文件
    try:
        tree = ET.parse(in_file)
    except:
        print(xml_dir)
        return None    
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        # print(cls)
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        try:
            bb = convert((w, h), b)
        except:
            return
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def get_class(path):
    classs = {}
    for i in tqdm(os.listdir(path)):
        in_file = open(os.path.join(path, i))
        try:
            tree = ET.parse(in_file)
        except:
            print(xml_dir)
            continue
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classs: 
                classs[cls] = 1
            else:
                classs[cls] += 1

    return classs


xml_dir = r'/home/twc/aiqc_data/zzbu_combined/ding_test/Annotations'
txt_dir = xml_dir.replace('Annotations', 'labels')
if not os.path.exists(txt_dir): os.makedirs(txt_dir)
classes = get_class(xml_dir)  # 类别
print(classes)
classes = list(classes.keys())
with open(os.path.join(txt_dir, 'classes.txt'), 'w') as f:
    for i in classes:
        f.writelines(i+'\n')
# # xml list
img_xmls = os.listdir(xml_dir)
for img_xml in tqdm(img_xmls):
    convert_annotation(img_xml, xml_dir, txt_dir)



