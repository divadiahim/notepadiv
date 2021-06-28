import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont, QPalette,QIcon,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QMenuBar,QAction,QFileDialog,QTextEdit

class MainWindow(QMainWindow):
    def __init__(win):
        QMainWindow.__init__(win)

        win.setMinimumSize(QSize(300, 100))    
        win.setWindowTitle("PyQt Test App") 
        win.setFixedSize(640, 480)
        
        # Add button widget
        
        button = QPushButton(win)
        button.setText("This is a button")
        win.setStyleSheet("QPushButton { margin: 40ex;}")
        button.resize(160, 50)
        button.move(470, 40)      
        button.setToolTip('Foarte misto.')  

        #Add lcd widget
        lcdNumber = QtWidgets.QLCDNumber(win)
        lcdNumber.setGeometry(QtCore.QRect(180, 50, 64, 23))
        lcdNumber.setObjectName("lcdNumber")

        #add a slider
        horizontalSlider = QtWidgets.QSlider(win)
        horizontalSlider.setGeometry(QtCore.QRect(10, 50, 160, 20))

        horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        horizontalSlider.setObjectName("horizontalSlider")

        # Create new action
        newAction = QAction(QIcon('new.png'), '&New', win)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New document')
        newAction.triggered.connect(win.newCall)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', win)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(win.openCall)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', win)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(win.exitCall)

        # Create menu bar and add action
        menuBar = win.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction) 
        #create text edit 
        win.myTextBox = QTextEdit(win) 
        win.myTextBox.move(10,120)  
        win.myTextBox.resize(620,350)

    def openCall(win):
        print('Open')
        path = QFileDialog.getOpenFileName(win, 'Open a file', '','All Files (*.*)')
        if path != ('', ''):
            print("File path : "+ path[0])
            fileName=path[0]
        file = open(fileName,'r')
        with file:
            text=file.read()
            win.myTextBox.setText(text)
            win.myTextBox.setFont(QFont('Helvetica',15))

    def newCall(win):
        print('New')

    def exitCall(win):
        print('Exit app')

    def clickMethod(win):
        print('PyQt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight,
                     QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    mainWin.show()
    sys.exit( app.exec_() )