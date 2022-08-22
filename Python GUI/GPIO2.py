Tmp = datetime.datetime(2000,12,14) 
Start = Tmp.today()
print str(Start)
print "houla"

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.lcdNumber.display(10.1)
        self.label.setText("Essai de texte")
        
        
    def closeEvent(self, event):
        print("event")
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Etes vous sur de vouloir quitter?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            GPIO.cleanup()       # clean up GPIO on CTRL+C exit
            GPIO.cleanup()           # clean up GPIO on normal exit
            event.accept()
        else:
            event.ignore()

    def my_Start(self, channel): #Interrupt 18
       
       Tmp = datetime.datetime(2000,12,14) 
       Start = Tmp.today() 

    def my_Stop(self, channel): #Interrupt 24
        Tmp = datetime.datetime(2000,12,14)
        Stop = Tmp.today()   
        print str(Stop-Start)
        self.label.setText(str(Stop-Start))

 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    GPIO.add_event_detect(18, GPIO.FALLING, callback=window.my_Start, bouncetime=2000)
    GPIO.add_event_detect(24, GPIO.RISING, callback=window.my_Stop, bouncetime=2000)
    window.show()
    sys.exit(app.exec_())
    print "houla2"