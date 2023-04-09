import cv2
import sys
import torch
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer

from ui_main_window import Ui_MainWindow


def convert2QImage(img):
    """图片转换成qt格式"""
    height, width, channel = img.shape
    return QImage(img, width, height, width * channel, QImage.Format_RGB888)

# 继承Ui_MainWindow里面是pyside生成的界面配置
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口参数
        self.setupUi(self)  
        # 设置模型地址
        # self.model = torch.hub.load("./", "custom", path=r"hand\train\original\weights\best.pt", source="local")
        # self.model = torch.hub.load("./", "custom", path="runs/train/exp/weights/best.pt", source="local")
        self.model = torch.hub.load("./", "custom", path="yolov5s.pt", source="local")
        # 设置计时器刷新时间
        self.timer = QTimer()
        self.timer.setInterval(1)
        # 设置视频对象，后面传给他图像，用计时器刷新
        self.video = None
        # 按键绑定方法
        self.bind_slots()

    def image_pred(self, file_path):
        """图片预测"""
        # 模型预测
        results = self.model(file_path)
        # 格式转换
        image = results.render()[0]
        return convert2QImage(image)

    def open_image(self):
        print("点击了检测图片！")
        # 把之前的显示关掉，因为之前可能打开了视频
        self.timer.stop()
        # 读取路径
        file_path = QFileDialog.getOpenFileName(self, dir="./data/images", filter="*.jpg;*.png;*.jpeg")
        if file_path[0]:
            # 获取路径
            file_path = file_path[0]
            # 图片预测
            qimage = self.image_pred(file_path)
            # 图像传给输入、输出组件，用来显示
            self.input.setPixmap(QPixmap(file_path))
            self.output.setPixmap(QPixmap.fromImage(qimage))

    def video_pred(self):
        """视频预测"""
        # 读取视频
        ret, frame = self.video.read()
        if not ret: # 没视频就不刷新了
            self.timer.stop()
        else: # 开始预测刷新
            # 颜色空间转换
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 图像传给输入，输出组件用来显示
            self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
            results = self.model(frame)
            image = results.render()[0]
            self.output.setPixmap(QPixmap.fromImage(convert2QImage(image)))

    def open_video(self):
        print("点击了检测视频！")
        # 获取视频地址
        file_path = QFileDialog.getOpenFileName(self, dir="./datasets", filter="*.mp4")
        if file_path[0]:
            file_path = file_path[0]
            # 把视频读出来传给视频对象
            self.video = cv2.VideoCapture(file_path)
            # 开始刷新
            self.timer.start()
                
    def bind_slots(self):
        """按键绑定方法"""
        self.det_image.clicked.connect(self.open_image)
        self.det_video.clicked.connect(self.open_video)
        # 定时器绑定视频预测，按设置的时间刷新
        self.timer.timeout.connect(self.video_pred)


if __name__ == "__main__":
    # 加载配置
    app = QApplication(sys.argv)
    # 显示窗口
    window = MainWindow()
    window.show()
    app.exec()