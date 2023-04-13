# python train.py \
# --cfg models/yolov5s.yaml \
# --data data/fall.yaml \
# --epochs 100 \
# --batch-size 16 \
# --workers 2 \
# --project 'data/fall/original/train' \
# --cache \

# python train.py \
# --cfg models/yolov5s.yaml \
# --data data/test.yaml \
# --epochs 100 \
# --batch-size 16 \
# --workers 2 \
# --cache \


python train.py \
--cfg models/yolov5s.yaml \
--data data/zhongliu.yaml \
--epochs 100 \
--batch-size 16 \
--workers 2 \
--project 'data/zhongliu/original/train' \
--cache \
# --amp \


# --patience 10 \
# --resume \
# --weights '/content/yolov5/content/drive/MyDrive/mobilenetv3small/train/exp/weights/last.pt' \
# --weights 'content/drive/My Drive/yolov5/mobilenetv3small/train/exp/last.pt' \
# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'


# --project '../drive/MyDrive/yolov5/data/hand/mobilecbam/train' \
