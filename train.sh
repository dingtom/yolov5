#first
python train.py \
--cfg models/mobilenetv3small.yaml \
--data data/hand.yaml \
--epochs 150 \
--patience 5 \
--batch-size 16 \
--workers 4 \
--project /content/drive/My Drive/yolov5/mobilenetv3small/train \
--cache
#--resume

# --project '/content/drive/My Drive/yolov5/mobilenetv3small/train' \
# --weights 'runs/train/original/last.pt' \
# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'
