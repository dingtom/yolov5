#first
python train.py \
--data data/hand.yaml \
--weights 'runs/train/original/last.pt' \
--epochs 150 \
--patience 5 \
--batch-size 14 \
--workers 4 \
--name original \
--resume

# -weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt'
