from label_preprocess import *


#  -------------------------------------------------------------统计数据集中每个类别的数量
# count_class(label_dir=r"E:\Download\smoke\smoke\labels")

# ------------------------------------------同一张照片不同类别被分开标注了,把标签合到一起
# merge_same_picture(label_dir = r'E:\Download\fire\labels',
#                    image_dir = r'E:\Download\fire\images',
#                    save_dir = r'E:\Download\fire\labels_new')

# ------------------------------------------------------------根据标签内容把正确的标签提出来
# get_right_label(label_dir=r"E:\Download\smoke\smoke\labels")


# # -----------------------------------------------------把某些类别index改成其他的
# replace_label(label_dir=r" labelimg E:\baiduyun\fall\FallDataset\images E:\baiduyun\fall\FallDataset\labels\classes.txt E:\baiduyun\fall\FallDataset\labels\labels",
#                   save_dir=r"E:\baiduyun\fall\FallDataset\l")


# --------------------------------------------------------------复制一个images文件夹里有的label文件
# copy_dir_need(need_dir=r"\\10.1.1.81\share\data\fire_smoke\labels", 
#               source_dir=r"\\10.1.1.81\share\data\smoke\images")

# --------------------------------------------------------------复制txt里有的文件
# copy_txt_need(image_dir=r'\\10.1.1.81\share\data\car_person\images',
#             need_txt=r'\\10.1.1.81\share\data\car_person\val.txt',
#             save_dir=r"\\10.1.1.81\share\data\car_person\val")


# --------------------------------------------------------------删除某些类别
# del_by_class(label_dir=r"E:\Download\mixed_fall\labels")


count_shuffle('/home/twc/aiqc_data/zzbu_combined/ding_test/fabric',
              train_ratio=0.8,
              val_ratio=0.1,
              test_ratio=0.1,
              extra_test=False)

