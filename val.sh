# python val.py  \
# --weights 'data/fall/original/train/exp2/weights/best.pt'  \
# --data data/fall.yaml  \
# --workers 2 \
# --batch-size 16  \
# --name fall \
# --augment \



python val.py  \
--task test \
--weights 'runs/train/exp21/weights/best.pt'  \
--data data/zhongliu.yaml  \
--workers 2 \
--batch-size 16  \
--name original \
--augment \


# python val.py  \
# --weights 'runs\train\exp21\weights\best.pt'  \
# --data data/test.yaml  \
# --workers 2 \
# --augment \


#--device cpu

