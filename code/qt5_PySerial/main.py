from PyQt5 import QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QStringListModel
from design import Ui_MainWindow
import matplotlib.pyplot as plt

import sys
import datetime

class Ui_MainWindow_cust(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.serial = QSerialPort()
        # self.serial.setBaudRate(230400)
        self.serial.setBaudRate(115200)
        self.portList = []
        self.val_coef = 0
        self.val_offset = 0
        self.x_list = []
        self.y_list = []
        # self.now_start = datetime.datetime.now()

    def up_comboBoxList(self, ):
        ports = QSerialPortInfo().availablePorts()
        self.portList = []
        self.comboBoxList.clear()
        for port in ports:
            self.portList.append(port.portName())
        self.comboBoxList.addItems(self.portList)

    def onRead(self):
        # text = self.ArduinoSerial.readline()
        # text = bytes(self.serial.readLine()).decode('utf8')
        text = bytes(self.serial.readAll()).decode('utf8')
        self.x_list.append(text)
        if text[0] == '!':
            # print('!qweqwe')
            self.infoPort(text)
            # return text
        # print(text, end='')
        self.writeTextBrowser(text.rstrip())
        return text

    # def drawGraf(self, text):


    def onOpen(self):
        self.serial.setPortName(self.comboBoxList.currentText())
        self.serial.open(QIODevice.ReadWrite)
        self.clearTextBrowser()

    def onClose(self):
        self.serial.close()
        all_text = ''.join(x for x in self.x_list).split('\n')[1:-1]
        x_param = [x for x in range(len(all_text))]
        print(all_text)
        all_text = [float(x[7:]) for x in all_text]
        plt.plot(x_param, all_text, label='test')
        plt.legend()
        plt.show()
        self.x_list = 0

    def writeTextBrowser(self, text):
        self.textBrowser.append(str(text))

    def clearTextBrowser(self):
        self.textBrowser.clear()

    def lineEditCoefSend(self):
        text = self.lineEdit_coef.text()
        self.lineEdit_coef.clear()
        try:
            text = float(text)
            self.val_coef = text
            self.set_param_label()
        except:
            pass
        # print(f"type:{type(text)}, text: {text}")
        # print((self.textBrowser.toPlainText())) получить содержимое
        return text

    def lineEditValSend(self):
        text = self.lineEdit_value_affset.text()
        self.lineEdit_value_affset.clear()
        try:
            text = float(text)
            self.val_offset = text
            self.set_param_label()
        except:
            pass
        # print(f"type:{type(text)}, text: {text}")
        # print((self.textBrowser.toPlainText())) получить содержимое
        return text

    def set_param_label(self):
        self.label_coef.setText(f"coef: {str(self.val_coef)}")
        self.label_val.setText(f"val: {str(self.val_offset)}")
        # self.serialSend()

    def serialSend(self):
        # text = '1'
        text = f"!{str(self.val_coef)};{str(self.val_offset)}\n"
        # print(text.encode())
        self.serial.write(text.encode())

    def infoPort(self, text):
        param = list(map(float, text[1:].split(';')))
        self.val_coef = param[0]
        self.val_offset = param[1]
        self.set_param_label()
        print(param)

    def start(self):
        self.up_comboBoxList()
        self.openButton.clicked.connect(self.onOpen)
        self.closeButton.clicked.connect(self.onClose)
        self.reloadButton.clicked.connect(self.up_comboBoxList)
        self.serial.readyRead.connect(self.onRead)
        self.lineEdit_coef.returnPressed.connect(self.lineEditCoefSend)
        self.lineEdit_value_affset.returnPressed.connect(self.lineEditValSend)
        # self.set_param_label()
        # self.infoButton.clicked.connect(self.set_param_label)


def application():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_cust()
    ui.setupUi(MainWindow)
    ui.start()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
