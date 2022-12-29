# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 238)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("* {\n"
"    font-family: \"Nirmala UI\";\n"
"}\n"
"\n"
"QLineEdit, QListWidget {\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 1px solid #888;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    background: steelblue;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #396b94;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    padding-left: 3px;\n"
"    padding-bottom: 3px;    \n"
"}\n"
"\n"
"QListWidget {\n"
"    padding: 5px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #888;\n"
"    background: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.pais = QtWidgets.QLineEdit(self.frame)
        self.pais.setMinimumSize(QtCore.QSize(0, 30))
        self.pais.setAlignment(QtCore.Qt.AlignCenter)
        self.pais.setObjectName("pais")
        self.gridLayout_2.addWidget(self.pais, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(27, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(self.frame)
        self.btn_agregar.setMinimumSize(QtCore.QSize(80, 35))
        self.btn_agregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout_2.addWidget(self.btn_agregar, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.lista = QtWidgets.QListWidget(self.frame_2)
        self.lista.setObjectName("lista")
        self.gridLayout.addWidget(self.lista, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.btn_eliminar = QtWidgets.QPushButton(self.frame_2)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_eliminar.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_eliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_eliminar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/basura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lista de países con PyQt5"))
        self.pais.setPlaceholderText(_translate("MainWindow", "Nombre del país"))
        self.btn_agregar.setText(_translate("MainWindow", "Agregar"))
        self.btn_eliminar.setToolTip(_translate("MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
