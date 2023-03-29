#first
python train.py \
--cfg models/swintransformer.yaml \
--data data/hand.yaml \
--epochs 100 \
--batch-size 32 \
--workers 4 \
--project '../drive/MyDrive/yolov5/cbamattention/train' \
--cache \
# --patience 10 \
# --resume \
# --weights '/content/yolov5/content/drive/MyDrive/mobilenetv3small/train/exp/weights/last.pt' \
# --weights 'content/drive/My Drive/yolov5/mobilenetv3small/train/exp/last.pt' \
# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'
