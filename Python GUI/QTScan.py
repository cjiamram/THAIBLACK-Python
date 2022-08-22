# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QTScan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import paramiko
import time
import datetime 
import requests, json
import pytesseract
import PIL.Image 


class Ui_frmOperation(object):
    def setupUi(self, frmOperation):
        frmOperation.setObjectName("frmOperation")
        frmOperation.resize(1000, 826)
        frmOperation.setMinimumSize(QtCore.QSize(780, 300))
        frmOperation.setMaximumSize(QtCore.QSize(1000, 1200))
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
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(10, 0, 991, 621))
        self.frame.setMinimumSize(QtCore.QSize(0, 399))
        self.frame.setMaximumSize(QtCore.QSize(1000, 1200))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.prgCapture = QtWidgets.QProgressBar(self.frame)
        self.prgCapture.setGeometry(QtCore.QRect(190, 510, 801, 91))
        self.prgCapture.setProperty("value", 0)
        self.prgCapture.setObjectName("prgCapture")
        self.lblScan = QtWidgets.QLabel(self.frame)
        self.lblScan.setGeometry(QtCore.QRect(20, 520, 141, 41))
        self.lblScan.setStyleSheet("font: 75 22pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lblScan.setObjectName("lblScan")
        self.lblScan_2 = QtWidgets.QLabel(self.frame)
        self.lblScan_2.setGeometry(QtCore.QRect(20, 420, 151, 41))
        self.lblScan_2.setStyleSheet("font: 75 22pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lblScan_2.setObjectName("lblScan_2")
        self.txtBeefNo = QtWidgets.QTextEdit(self.frame)
        self.txtBeefNo.setEnabled(False)
        self.txtBeefNo.setGeometry(QtCore.QRect(190, 410, 761, 87))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 60, 119))
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
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.txtBeefNo.setFont(font)
        self.txtBeefNo.setAutoFillBackground(True)
        self.txtBeefNo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txtBeefNo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txtBeefNo.setObjectName("txtBeefNo")
        self.gview = QtWidgets.QGraphicsView(self.frame)
        self.gview.setGeometry(QtCore.QRect(10, 10, 941, 391))
        self.gview.setObjectName("gview")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 650, 191, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255,255, 255);\n"
"background-image: url(:/Green/Img/Button.png);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        frmOperation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmOperation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        frmOperation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmOperation)
        self.statusbar.setObjectName("statusbar")
        frmOperation.setStatusBar(self.statusbar)

        self.retranslateUi(frmOperation)
        self.pushButton.clicked.connect(self.prgCapture.reset)
        self.pushButton.clicked.connect(self.readImgClassify)
        QtCore.QMetaObject.connectSlotsByName(frmOperation)

    def retranslateUi(self, frmOperation):
        _translate = QtCore.QCoreApplication.translate
        frmOperation.setWindowTitle(_translate("frmOperation", "Operation Capture"))
        self.lblScan.setText(_translate("frmOperation", "Scaning"))
        self.lblScan_2.setText(_translate("frmOperation", "Beef No"))
        self.pushButton.setText(_translate("frmOperation", "Process"))
    
    
    def process(self):
       camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
       parent_dir=""
       x = str(datetime.datetime.now())
       x=x.replace(".","_")
       x=x.replace(":","_")
       x=x.replace(" ","_")
       print(x)
       path = os.path.join(parent_dir, x)
       os.mkdir(path) 
       for i in range(1,11):
         return_value, image = camera.read()
         cv2.imwrite(x+"/"+'BEEF-'+str(i)+'.png', image)
         self.prgCapture.setProperty("value", i*10) 
         time.sleep(0.10)
       del(camera)
       self.upload(x)
       return x
    
    
    def readImgClassify(self):
        self.txtBeefNo.clear
        image = cv2.imread('Img/TB-9.jpg')  # Read image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(image.shape)
        image = cv2.resize(image, (900, 390))
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

        
        #str=pytesseract.image_to_string(PIL.Image.open('img/TB-9.jpg'),config=myconfig)
       
        print(str)
        self.txtBeefNo.setText(str)
        

        height, width = image.shape[:2]
        image_disp = QtGui.QImage(image.data, width, height, QtGui.QImage.Format_RGB888)

        height, width = image.shape[:2]
        #print(height,width)
       
        scene1 = QtWidgets.QGraphicsScene()
        pixMap = QtGui.QPixmap.fromImage(image_disp)
        scene1.addPixmap(pixMap)
        self.gview.setScene(scene1)



    def upload(self,folder):
        # grab the list of images that we'll be describing
        print("[INFO] describing images...")
        imagePaths = list(paths.list_images(folder))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('202.29.4.240', username="root", password="Nrruspare@2017")
        
        url = requests.get("http://nrruapp.nrru.ac.th/NRRUCredential/remoteCreateDIR.php?folder="+folder)
        text = url.text
        data = json.loads(text)
        for (i, imagePath) in enumerate(imagePaths):
            sftp = ssh.open_sftp()
            localpath = imagePath
            fn = imagePath.split(os.path.sep)[-1].split(".")[0]
            ext=imagePath.split(os.path.sep)[-1].split(".")[1]
            fileName=fn+"."+ext
            remotepath = '/var/www/html/beefUpload/'+folder+"/"+fileName
            sftp.put(localpath, remotepath)  
            sftp.close()
        ssh.close()

    def createFolder(folder):
        url = requests.get("http://nrruapp.nrru.ac.th/NRRUCredential/remoteCreateDIR.php?folder="+folder)
        text = url.text
        data = json.loads(text)
        return data['flag']
    
import imgOperate


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmOperation = QtWidgets.QMainWindow()
    ui = Ui_frmOperation()
    ui.setupUi(frmOperation)
    frmOperation.show()
    sys.exit(app.exec_())