python train.py \
--project 'runs/cardnumber/yolov5s/train' \
--cfg models/yolov5s.yaml \
--data data/cardnumber.yaml \
--batch-size 64 \
--cache \
--amp



# --weights 'runs/cardnumber/yolov5s/train/exp2/weights/best.pt'  \

# --epochs 200 \
# --workers 8 \

# python train.py \
# --cfg models/yolov5s_C2f.yaml \
# --project 'runs/hand/yolov5s_C2f/train' \
# --epochs 300 \
# --batch-size 64 \
# --workers 8 \
# --cache \
# --amp  \

# python train.py \
# --cache \
# --amp \
# --cfg '/home/tomding/hdd/work/yoloair/configs/yolov5-transformer-Improved/yolov5scbam-swin-bifpn.yaml' \
# --project 'runs/hand/yolov5-transformer-Improved/train' \
# --weights 'runs/hand/yolov5s/train/exp/weights/best.pt';



# python train.py \
# --cache \
# --amp  \
# --cfg models/mobilecbam.yaml \
# --project 'runs/hand/mobilecbam/train' \
# --weights 'runs/hand/mobilecbam/train/exp/weights/best.pt';

# python train.py \
# --cache \
# --amp  \
# --cfg models/mobilenetv3small.yaml \
# --project 'runs/hand/mobilenetv3small/train' \
# --weights 'runs/hand/mobilenetv3small/train/exp/weights/best.pt';

# python train.py \
# --cache \
# --amp  \
# --cfg models/yolov5s.yaml \
# --project 'runs/hand/yolov5s/train' \
# --weights 'runs/hand/yolov5s/train/exp/weights/best.pt';

# python train.py \
# --cache \
# --amp  \
# --cfg models/cbamattention.yaml \ 
# --project 'runs/hand/cbamattention/train' \
# --weights 'runs/hand/cbamattention/train/exp/weights/best.pt';


# python val.py  \
# --task test \
# --weights 'data/hand/original/train/weights/best.pt'  \
# --data data/hand.yaml  \
# --workers 4 \
# --batch-size 80  \
# --name original \
# --augment 



