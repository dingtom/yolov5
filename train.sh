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
--data data/hand.yaml \
--epochs 100 \
--batch-size 80 \
--workers  4 \
--project 'data/hand/original/train' \
--cache \
--amp;

python val.py  \
--task test \
--weights 'data/hand/original/train/weights/best.pt'  \
--data data/hand.yaml  \
--workers 4 \
--batch-size 80  \
--name original \
--augment 


# --patience 10 \
# --resume \
# --weights '/content/yolov5/content/drive/MyDrive/mobilenetv3small/train/exp/weights/last.pt' \
# --weights 'content/drive/My Drive/yolov5/mobilenetv3small/train/exp/last.pt' \
# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'


# --project '../drive/MyDrive/yolov5/data/hand/mobilecbam/train' \
