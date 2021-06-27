from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette,QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QMenuBar,QAction

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
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



win = QMainWindow()
win.setGeometry(400, 400, 500, 300)
win.setWindowTitle("Test App")

    # Create new action
newAction = QAction(QIcon('new.png'), '&New', win)
newAction.setShortcut('Ctrl+N')
newAction.setStatusTip('New document')


# Create new action
openAction = QAction(QIcon('open.png'), '&Open', win)
openAction.setShortcut('Ctrl+O')
openAction.setStatusTip('Open document')

# Create exit action
exitAction = QAction(QIcon('exit.png'), '&Exit', win)
exitAction.setShortcut('Ctrl+Q')
exitAction.setStatusTip('Exit application')
#exitAction.triggered.connect(win.exitCall)

button = QPushButton(win)
button.setText("This is a button")
win.setStyleSheet("QPushButton { margin: 40ex;}")
button.resize(150, 50)
button.move(10, 30)
button.show()
menu = QMenuBar(win)
fileMenu = menu.addMenu("&File")
fileMenu.addAction(newAction)
fileMenu.addAction(openAction)
fileMenu.addAction(exitAction)
label = QLabel()
win.show()
sys.exit(app.exec_())
