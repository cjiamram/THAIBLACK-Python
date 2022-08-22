#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import random
import datetime
import sys
from threading import Thread

from PyQt4 import QtCore, QtGui, uic


qtCreatorFile = "form.ui" # Enter file here.
global Ui_MainWindow, QtBaseClass 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print "Ici"
global Start

Tmp = datetime.datetime(2000,12,14)  #on est oblige de donner une date dans les arguments, mais ca n'a aucune incidence pour la suite
Start = Tmp.today()   #jour.today() renvoie la date au moment ou on l'appelle au format Annee mois jour,heure,minute,seconde,microseconde
print str(Start)

def my_Start(channel): #Interrupt 18
	
	Tmp = datetime.datetime(2000,12,14)  #on est oblige de donner une date dans les arguments, mais ca n'a aucune incidence pour la suite
	Start = Tmp.today()   #jour.today() renvoie la date au moment ou on l'appelle au format Annee mois jour,heure,minute,seconde,microseconde



def my_Stop(channel): #Interrupt 24
    Tmp = datetime.datetime(2000,12,14)
    Stop = Tmp.today()   
    print str(Stop-Start)
    self.label.setText(str(Stop-Start))




print "houla"
GPIO.add_event_detect(18, GPIO.FALLING, callback=my_Start,bouncetime=2000)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_Stop,bouncetime=2000)
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

 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    print "houla2"

    
 
    


