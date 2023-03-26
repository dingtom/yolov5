#first
python train.py --data data/food.yaml --epochs 200 --patience 5  --batch-size 64 --workers 12 --name original --cache
#retrain
# !python train.py --weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/last.pt' --data data/food.yaml --epochs 200 --patience 5  --batch-size 200 --workers 12 --name mobilenet --cache
# resume
# !python train.py --weights '/content/drive/My Drive/yolov5/runs/train/mobilenet/weights/last.pt' --data data/food.yaml  --epochs 200 --patience 5  --batch-size 200 --workers 12 --name mobilenet --cache --resume
#--device cpu

#!python val.py --weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/best.pt' --data data/food.yaml --workers 12 --batch-size 200 --name original --augment
#!python val.py --weights '/content/drive/My Drive/yolov5/runs/train/exp3/weights/best.pt' --data data/food.yaml --workers 4 --batch-size 64 --name original --augment