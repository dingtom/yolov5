python detect.py       \
--data data/fabric.yaml \
--weights runs/fabric/yolov5s/train/exp26/weights/best.pt  \
--source  /srv/samba/dingwenchao/hdd/fabric/data/FlawImg3   \
--conf-thres  0.25 \
--iou-thres   0.2   \
--device  0