python val.py  \
--project 'runs/fabric/yolov5s/val' \
--data data/fabric.yaml  \
--weights runs/fabric/best.pt  \
--task test     \
--device 0 \
--batch-size 200  \
--workers 8 

# iou=0.1
# conf=0.4
# --weights 'runs/car_person/yolov5s/train/exp/weights/best.pt'  \



# python val.py  \
# --project 'runs/hand/yolov5s/val' \
# --weights 'runs/hand/yolov5s/train/exp2/weights/best.pt'  \
# --iou-thres 0.1 \
# --conf-thres 0.4 \
# --half \
# --save-txt \
# --plot-compare \

# python val.py  \
# --project 'runs/hand/cbamattention/val' \
# --weights 'runs/hand/cbamattention/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/coorattention/val' \
# --weights 'runs/hand/coorattention/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/mobilecbam/val' \
# --weights 'runs/hand/mobilecbam/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/mobilenetv3small/val' \
# --weights 'runs/hand/mobilenetv3small/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/yolov5s/val' \
# --weights 'runs/hand/yolov5s/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/yolov5-transformer-Improved/val' \
# --weights 'runs/hand/yolov5-transformer-Improved/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;

# python val.py  \
# --project 'runs/hand/yolov5s_C2f/val' \
# --weights 'runs/hand/yolov5s_C2f/train/exp/weights/best.pt'  \
# --iou-thres ${iou} \
# --conf-thres ${conf} \
# --half ;


# python val.py  \
# --weights 'runs\train\exp21\weights\best.pt'  \
# --data data/test.yaml  \
# --workers 2 \
#--device cpu

