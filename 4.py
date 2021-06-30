import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont, QPalette,QIcon,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QMenuBar,QAction,QFileDialog,QTextEdit,QWidget,QVBoxLayout,QTabWidget

class MyTableWidget(QWidget):
    
    def __init__(win, parent=None):
        super(QWidget, win).__init__(parent)
        win.layout = QVBoxLayout(win)
        
        # Initialize tab screen
        win.tabs = QTabWidget()
        win.tab1 = QWidget()
        win.tab2 = QWidget()
        win.tabs.resize(200,200)
        win.tabs.setFixedSize(720,480)
        
        
        # Add tabs
        win.tabs.addTab(win.tab1,"Tab 1")
        #win.tabs.addTab(win.tab2,"Tab 2")
        
        # Create first tab
        win.tab1.layout = QVBoxLayout(win)
        win.myTextBox = QTextEdit(win)
        win.myTextBox.move(10,120)  
        win.myTextBox.resize(620,350)
        win.myTextBox.setStyleSheet("border: 1px solid white;") 
        win.tab1.layout.addWidget(win.myTextBox)
        win.tab1.setLayout(win.tab1.layout)
        
        # Add tabs to widget
        win.layout.addWidget(win.tabs)
        win.setLayout(win.layout)     

class MainWindow(QMainWindow):
    def __init__(win):
        super().__init__()


        win.setMinimumSize(QSize(300, 100))    
        win.setWindowTitle("Notepadiv") 
        win.setFixedSize(740, 580)
        win.setWindowIcon(QIcon('img/icon2.png'))
        # Add button widget
        
        button = QPushButton(win)
        button.setText("This is a button")
        win.setStyleSheet("QPushButton { margin: 40ex;}")
        button.resize(160, 50)
        button.move(470, 40)      
        button.setToolTip('Foarte misto.') 
        button.clicked.connect(win.clickMethod)

        #Add lcd widget+label
        win.lcdNumber = QtWidgets.QLCDNumber(win)
        win.lcdNumber.setGeometry(QtCore.QRect(180, 50, 64, 23))
        win.lcdNumber.setObjectName("win.lcdNumber")
        win.label = QtWidgets.QLabel(win)
        win.label.setGeometry(QtCore.QRect(260, 50, 116, 19))
        win.label.setObjectName("label")
        win.label.setText("Change text size")
        win.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        #add a slider
        win.horizontalSlider = QtWidgets.QSlider(win)
        win.horizontalSlider.setGeometry(QtCore.QRect(10, 50, 160, 20))
        win.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        win.horizontalSlider.setObjectName("win.horizontalSlider")
        win.horizontalSlider.valueChanged.connect(win.valuechange)
        win.horizontalSlider.setTickInterval(5)
        #win.lcdNumber.display(val)
        

        # Create new action
        newAction = QAction(QIcon('new.png'), '&New', win)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New document')
        newAction.triggered.connect(win.newCall)

        # Create new action
        openAction = QAction(QIcon('img/open.png'), '&Open', win)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(win.openCall)

        # Create exit action
        exitAction = QAction(QIcon('img/exit.png'), '&Exit', win)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(win.exitCall)

        # Create save action
        saveAction = QAction(QIcon('img/save.png'), '&Save', win)        
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save document')
        saveAction.triggered.connect(win.saveCall)

        # Create menu bar and add action
        menuBar = win.menuBar()
        fileMenu0 = menuBar.addMenu('&Notepadiv')
        fileMenu = menuBar.addMenu('&File')
        fileMenu0.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction) 
        fileMenu.addAction(exitAction)
        #create text edit 
        win.myTextBox = QTextEdit(win) 
        win.myTextBox.move(10,120)  
        win.myTextBox.resize(620,350)
        win.myTextBox.setStyleSheet("border: 1px solid white;")
        win.table_widget = MyTableWidget(win)
        win.table_widget.move(0,80)
        win.table_widget.setFixedSize(740, 480)
        win.table_widget.myTextBox.setText('ashdjfhjdsg')
        # win.setCentralWidget(win.table_widget)
       
        
    def openCall(win):
        print('Open')
        path = QFileDialog.getOpenFileName(win, 'Open a file', '','All Files (*.*)')
        if path != ('', ''):
            print("File path : "+ path[0])
            fileName=path[0]
        if path[0]:    
            file = open(fileName,'r')
            with file:
                text=file.read()
                win.myTextBox.setText(text)
                win.myTextBox.setFont(QFont('Helvetica',15))

    def newCall(win):
        print('New')
        win.w = MainWindow()
        win.w.show()

    def saveCall(win):    
        print("Save")
        path = QFileDialog.getSaveFileName(win, 'Save a file', '','All Files (*.*)')
        if path[0]:
            file = open(path[0],'w')
            text=win.myTextBox.toPlainText()
            file.write(text)
            file.close()
            print(text)

    def exitCall(win):
        print('Exit app')
        sys.exit()
    def clickMethod(win):
        win.table_widget.tabs.addTab(win.table_widget.tab2,"Tab 2")
    def valuechange(win):
        size = win.horizontalSlider.value()
        win.lcdNumber.display(size)
        win.myTextBox.setFont(QFont('Helvetica',size))
        print(size)
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
    palette.setColor(QtGui.QPalette.Highlight,QtGui.QColor(255,255,255).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    palette.setColor(palette.Light, QtGui.QColor(255, 255, 255))
    app.setPalette(palette)
    mainWin.show()
    sys.exit( app.exec_() )