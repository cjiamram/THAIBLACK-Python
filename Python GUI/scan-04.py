# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QTScan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from imutils import paths
import os
import cv2
import paramiko
import time
import datetime 
import requests, json
import pytesseract
import PIL.Image
import imgOperate
#import jsonify


class Ui_frmOperation(object):
    imageFolder=""
    
    def setupUi(self, frmOperation):
        imageFolder=""
        frmOperation.setObjectName("frmOperation")
        frmOperation.resize(1030, 627)
        frmOperation.setMinimumSize(QtCore.QSize(780, 300))
        frmOperation.setMaximumSize(QtCore.QSize(1500, 1200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Capture48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmOperation.setWindowIcon(icon)
        frmOperation.setStyleSheet("background-color:rgb(75, 60, 119);\n"
"color: rgb(255, 255, 255);")
        frmOperation.setIconSize(QtCore.QSize(48, 48))
        frmOperation.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(frmOperation)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 0, 1000, 491))
        self.frame.setMinimumSize(QtCore.QSize(0, 399))
        self.frame.setMaximumSize(QtCore.QSize(1000, 1200))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.prgCapture = QtWidgets.QProgressBar(self.frame)
        self.prgCapture.setGeometry(QtCore.QRect(170, 60, 831, 41))
        self.prgCapture.setProperty("value", 0)
        self.prgCapture.setObjectName("prgCapture")
        self.lblScan = QtWidgets.QLabel(self.frame)
        self.lblScan.setGeometry(QtCore.QRect(20, 60, 141, 41))
        self.lblScan.setStyleSheet("font: 60 18pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lblScan.setObjectName("lblScan")
        self.lblScan_2 = QtWidgets.QLabel(self.frame)
        self.lblScan_2.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.lblScan_2.setStyleSheet("font: 60 18pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lblScan_2.setObjectName("lblScan_2")
        self.txtBeefNo = QtWidgets.QTextEdit(self.frame)
        self.txtBeefNo.setEnabled(False)
        self.txtBeefNo.setGeometry(QtCore.QRect(170, 10, 791, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 158, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 131, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 52, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 70, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 52, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 158, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 131, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 52, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 70, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 52, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 158, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 131, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 52, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 70, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 105, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.txtBeefNo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.txtBeefNo.setFont(font)
        self.txtBeefNo.setAutoFillBackground(True)
        self.txtBeefNo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.txtBeefNo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txtBeefNo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txtBeefNo.setObjectName("txtBeefNo")
        self.gview = QtWidgets.QGraphicsView(self.frame)
        self.gview.setGeometry(QtCore.QRect(10, 160, 961, 321))
        self.gview.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gview.setObjectName("gview")
        self.comboImage = QtWidgets.QComboBox(self.frame)
        self.comboImage.setEnabled(True)
        self.comboImage.setGeometry(QtCore.QRect(170, 110, 791, 41))
        self.comboImage.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.comboImage.setObjectName("comboImage")
        self.lblScan_3 = QtWidgets.QLabel(self.frame)
        self.lblScan_3.setGeometry(QtCore.QRect(20, 110, 141, 41))
        self.lblScan_3.setStyleSheet("font: 60 18pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lblScan_3.setObjectName("lblScan_3")
        self.pushProcess = QtWidgets.QPushButton(self.centralwidget)
        self.pushProcess.setGeometry(QtCore.QRect(10, 500, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushProcess.setFont(font)
        self.pushProcess.setStyleSheet("color: rgb(255,255, 255);\n"
"background-image: url(:/Green/Img/Button.png);\n"
"font: 12pt \"Algerian\";\n"
"\n"
"\n"
"")
        self.pushProcess.setObjectName("pushProcess")
        self.pushUpload = QtWidgets.QPushButton(self.centralwidget)
        self.pushUpload.setGeometry(QtCore.QRect(210, 500, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushUpload.setFont(font)
        self.pushUpload.setStyleSheet("color: rgb(255,255, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 12pt \"Algerian\";\n"
"\n"
"")
        self.pushUpload.setObjectName("pushUpload")
        frmOperation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmOperation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 26))
        self.menubar.setObjectName("menubar")
        frmOperation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmOperation)
        self.statusbar.setObjectName("statusbar")
        frmOperation.setStatusBar(self.statusbar)

        self.retranslateUi(frmOperation)
        self.pushProcess.clicked.connect(self.prgCapture.reset)
        self.pushProcess.clicked.connect(self.process)
        self.comboImage.currentIndexChanged['QString'].connect(self.readImgClassify)
        self.pushUpload.clicked.connect(self.upload)
        QtCore.QMetaObject.connectSlotsByName(frmOperation)
        self.listPicture("Test")

    def retranslateUi(self, frmOperation):
        _translate = QtCore.QCoreApplication.translate
        frmOperation.setWindowTitle(_translate("frmOperation", "Operation Capture"))
        self.lblScan.setText(_translate("frmOperation", "Scaning"))
        self.lblScan_2.setText(_translate("frmOperation", "Beef No"))
        self.comboImage.setItemText(0, _translate("frmOperation", "1 img 1"))
        self.comboImage.setItemText(1, _translate("frmOperation", "2 img 2"))
        self.lblScan_3.setText(_translate("frmOperation", "Image List"))
        self.pushProcess.setText(_translate("frmOperation", "Process"))
        self.pushUpload.setText(_translate("frmOperation", "Upload"))
#*****************************************************
#----------------Process------------------------------
    
    def getFileConfig(self):
        f = open('config.json',)
        data = json.load(f)
        return data["fileConfig"]
      
    def getHostConfig(self):
        f = open('config.json',)
        data = json.load(f)
        return data["hostConfig"]
    
    def getConfig(self):
        f = open('config.json',)
        data = json.load(f)
        return data
    
    def listPicture(self,folder):
        imagePaths = list(paths.list_images(folder))
     
        for (i, imagePath) in enumerate(imagePaths):
           strItem =str(i+1)+" "+imagePath   
           self.comboImage.addItem(strItem)  
        return 0



    


    
    def process(self):
       self.comboImage.clear()
       camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
       parent_dir=""
       x = str(datetime.datetime.now())
       x=x.replace(".","_")
       x=x.replace(":","_")
       x=x.replace(" ","_")
       self.imageFolder=x

       path = os.path.join(parent_dir, x)
       os.mkdir(path) 
       for i in range(1,11):
         return_value, image = camera.read()
         cv2.imwrite(x+"/"+'PIC-'+format(i, '02d')+'.png', image)
         self.prgCapture.setProperty("value", i*10) 
         time.sleep(0.10)
       del(camera)
       self.listPicture(x)
       return x
    
    
    def readImgClassify(self):
        self.txtBeefNo.clear
        text = self.comboImage.currentText()
        x = text.split()
        l=len(x)
        if (l>0):
                image = cv2.imread(x[1])  # Read image
        else:
                image = cv2.imread('Img/TB-9.jpg')  # Read image  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (900, 400))
        hImg, wImg, _ = image.shape

        myconfig=r"--psm 11 --oem 3"
        boxes = pytesseract.image_to_boxes(image)
        str=""

        for b in boxes.splitlines():
                b = b.split(' ')
              
                str =str+ b[0]
                x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                cv2.rectangle(image, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
                cv2.putText(image, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

        
        self.txtBeefNo.setText(str)
        

        height, width = image.shape[:2]
        image_disp = QtGui.QImage(image.data, width, height, QtGui.QImage.Format_RGB888)

        height, width = image.shape[:2]
       
        scene1 = QtWidgets.QGraphicsScene()
        pixMap = QtGui.QPixmap.fromImage(image_disp)
        scene1.addPixmap(pixMap)
        self.gview.setScene(scene1)
        return 0



    def upload(self):

        data=self.getConfig()
        folder= self.imageFolder        
        print("[INFO] describing images...")
        if(self.txtBeefNo.text()==""):
                uploadFolder=folder
        else:
                uploadFolder=self.txtBeefNo.text()
        
        imagePaths = list(paths.list_images(folder))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(data["hostConfig"]["ip"], username=data["hostConfig"]["user"], password=data["hostConfig"]["password"])
        
        url = requests.get(data["fileConfig"]["urlUpload"]+uploadFolder)
        text = url.text
        data = json.loads(text)
        for (i, imagePath) in enumerate(imagePaths):
            sftp = ssh.open_sftp()
            localpath = imagePath
            fn = imagePath.split(os.path.sep)[-1].split(".")[0]
            ext=imagePath.split(os.path.sep)[-1].split(".")[1]
            fileName=fn+"."+ext
            remotepath = data["fileConfig"]["pathUpload"]+uploadFolder+"/"+fileName
            sftp.put(localpath, remotepath)  
            sftp.close()
        ssh.close()

    def createFolder(self,folder):
        data=self.getConfig()
        url = requests.get(data["fileConfig"]["urlUpload"]+folder)
        text = url.text
        data = json.loads(text)
        return data['flag']

#*****************************************************


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmOperation = QtWidgets.QMainWindow()
    ui = Ui_frmOperation()
    ui.setupUi(frmOperation)
    frmOperation.show()
    sys.exit(app.exec_())