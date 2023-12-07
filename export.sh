python export.py  \
--data data/fabric.yaml \
--weights runs/fabric/yolov5s/train/exp/weights/best.pt  \
--include onnx \
--simplify \
--dynamic
# --half \
# --int8  \



