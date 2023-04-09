#first
python train.py \
--cfg models/cbamattention.yaml \
--data data/car.yaml \
--epochs 100 \
--batch-size 10 \
--workers 2 \
--project 'data/car/cbamattention/train' \
--cache \
# --amp \
# --patience 10 \
# --resume \
# --weights '/content/yolov5/content/drive/MyDrive/mobilenetv3small/train/exp/weights/last.pt' \
# --weights 'content/drive/My Drive/yolov5/mobilenetv3small/train/exp/last.pt' \
# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'


# --project '../drive/MyDrive/yolov5/data/hand/mobilecbam/train' \
