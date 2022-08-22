import os

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 761, 561))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.scene.installEventFilter(self)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "lena.jpg")

        image = cv2.imread(filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = image.shape
        image_disp = QtGui.QImage(
            image.data, width, height, QtGui.QImage.Format_Grayscale8
        )
        pixMap = QtGui.QPixmap.fromImage(image_disp)
        self.pixmap_item = self.scene.addPixmap(pixMap)

    def eventFilter(self, obj, event):
        if obj is self.scene and event.type() == QtCore.QEvent.GraphicsSceneMousePress:
            spf = event.scenePos()
            lpf = self.pixmap_item.mapFromScene(spf)
            brf = self.pixmap_item.boundingRect()
            if brf.contains(lpf):
                lp = lpf.toPoint()
                print(lp)
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())