# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 377, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBoxList = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxList.setObjectName("comboBoxList")
        self.horizontalLayout_2.addWidget(self.comboBoxList)
        self.openButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_2.addWidget(self.openButton)
        self.reloadButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout_2.addWidget(self.reloadButton)
        self.closeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(401, 4, 291, 148))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_coef_name = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_coef_name.setFont(font)
        self.label_coef_name.setObjectName("label_coef_name")
        self.horizontalLayout.addWidget(self.label_coef_name)
        self.label_coef = QtWidgets.QLabel(self.layoutWidget1)
        self.label_coef.setObjectName("label_coef")
        self.horizontalLayout.addWidget(self.label_coef)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_coef = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_coef.setEnabled(True)
        self.lineEdit_coef.setObjectName("lineEdit_coef")
        self.horizontalLayout_6.addWidget(self.lineEdit_coef)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_val_name = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_val_name.setFont(font)
        self.label_val_name.setObjectName("label_val_name")
        self.horizontalLayout_7.addWidget(self.label_val_name)
        self.label_val = QtWidgets.QLabel(self.layoutWidget1)
        self.label_val.setObjectName("label_val")
        self.horizontalLayout_7.addWidget(self.label_val)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_value_affset = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_value_affset.setObjectName("lineEdit_value_affset")
        self.horizontalLayout_8.addWidget(self.lineEdit_value_affset)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.infoButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.infoButton.setObjectName("infoButton")
        self.verticalLayout_5.addWidget(self.infoButton)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 230, 381, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.image_label = QtWidgets.QLabel(self.widget)
        self.image_label.setObjectName("image_label")
        self.verticalLayout_6.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(self.widget)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout_6.addWidget(self.control_bt)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Window"))
        self.openButton.setText(_translate("MainWindow", "OPEN"))
        self.reloadButton.setText(_translate("MainWindow", "RELOAD"))
        self.closeButton.setText(_translate("MainWindow", "CLOSE"))
        self.label_coef_name.setText(_translate("MainWindow", "coefficient"))
        self.label_coef.setText(_translate("MainWindow", "coef:"))
        self.label_val_name.setText(_translate("MainWindow", "value offset"))
        self.label_val.setText(_translate("MainWindow", "val:"))
        self.infoButton.setText(_translate("MainWindow", "INFO"))
        self.image_label.setText(_translate("MainWindow", "TextLabel"))
        self.control_bt.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
