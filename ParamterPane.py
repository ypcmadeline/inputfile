# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from functools import partial

from PyQt5.QtWidgets import QButtonGroup

import WriteFile
import constPara, varyPara
from AddPane import *
import property
import ErrorPane


class parameter(object):

    def __init__(self, const, vary):
        self.const = const
        self.vary = vary
        self.constPara = []
        self.varyPara = []
        self.pp = []
        for i in range(vary):
            self.pp.append(property.property())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 16))
        self.label.setText("Parameter Setting")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 80, 1000, 700))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # list for vary paramter label
        self.name = []
        self.combo = []
        self.range = []
        self.rfield = []
        self.check = []
        self.add = []
        self.other = []
        self.othername = []

        # list for const paramter label
        self.cname = []
        self.ccombo = []
        self.cvalue = []
        self.crfield = []
        self.cadd = []
        self.cother = []
        self.cothername = []

        self.btn_grp = QButtonGroup()
        self.btn_grp.buttonClicked[int].connect(self.addSession)

        for i in range(self.vary):
            self.name.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.name[i].setText("Varying parameter" + str(i + 1))
            self.gridLayout.addWidget(self.name[i], i, 0, 1, 1)
            self.name[i].adjustSize()

            self.combo.append(QtWidgets.QComboBox(self.gridLayoutWidget))
            self.combo[i].setObjectName("comboBox")
            self.combo[i].addItem("Keithley 2440 cur (A)")
            self.combo[i].addItem("Keithley 6221 amp (A)")
            self.combo[i].addItem("Keithley 6221 fre (Hz)")
            self.combo[i].addItem("Angle")
            self.combo[i].addItem("MFLI - x")
            self.combo[i].addItem("MFLI - y")
            self.combo[i].addItem("Other")
            self.gridLayout.addWidget(self.combo[i], i, 1, 1, 1)
            self.combo[i].adjustSize()
            self.pp[i].savename = "Keithley 2440 cur (A)"
            self.combo[i].currentTextChanged.connect(partial(self.changetoother, i, True))

            self.other.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.other[i].setText("Other: ")
            self.gridLayout.addWidget(self.other[i], i, 2, 1, 1)
            self.other[i].adjustSize()

            self.othername.append(QtWidgets.QLineEdit(self.gridLayoutWidget))
            self.gridLayout.addWidget(self.othername[i], i, 3, 1, 1)
            self.othername[i].textChanged.connect(partial(self.savename, i))

            self.range.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.range[i].setText("Range")
            self.gridLayout.addWidget(self.range[i], i, 4, 1, 1)
            self.range[i].adjustSize()

            self.rfield.append(QtWidgets.QLineEdit(self.gridLayoutWidget))
            self.rfield[i].setText(self.pp[i].saverange[0])
            self.gridLayout.addWidget(self.rfield[i], i, 5, 1, 1)
            # save range property whenever text changed
            self.rfield[i].textChanged.connect(partial(self.saverfield, i))

            self.check.append(QtWidgets.QCheckBox(self.gridLayoutWidget))
            self.check[i].setText("sweep")
            self.check[i].setChecked(self.pp[i].savesweep[0])
            self.gridLayout.addWidget(self.check[i], i, 6, 1, 1)

            self.check[i].clicked.connect(partial(self.savescheck, i))

            self.add.append(QtWidgets.QPushButton(self.gridLayoutWidget))
            self.add[i].setText("Add")
            self.add[i].setObjectName(str(i))
            self.gridLayout.addWidget(self.add[i], i, 7, 1, 1)
            self.btn_grp.addButton(self.add[i], i)

        for i in range(self.const):
            self.cname.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.cname[i].setText("Constant parameter" + str(i + 1))
            self.gridLayout.addWidget(self.cname[i], i + self.vary, 0, 1, 1)
            self.cname[i].adjustSize()

            self.ccombo.append(QtWidgets.QComboBox(self.gridLayoutWidget))
            self.ccombo[i].setObjectName("comboBox")
            self.ccombo[i].addItem("Keithley 2440 cur (A)")
            self.ccombo[i].addItem("Keithley 6221 amp (A)")
            self.ccombo[i].addItem("Keithley 6221 fre (Hz)")
            self.ccombo[i].addItem("Angle")
            self.ccombo[i].addItem("MFLI - x")
            self.ccombo[i].addItem("MFLI - y")
            self.ccombo[i].addItem("Other")
            self.gridLayout.addWidget(self.ccombo[i], i + self.vary, 1, 1, 1)
            self.ccombo[i].adjustSize()

            self.cother.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.cother[i].setText("Other:")
            self.gridLayout.addWidget(self.cother[i], i + self.vary, 2, 1, 1)
            self.cother[i].adjustSize()

            self.cothername.append(QtWidgets.QLineEdit(self.gridLayoutWidget))
            self.gridLayout.addWidget(self.cothername[i], i + self.vary, 3, 1, 1)
            self.cothername[i].textChanged.connect(partial(self.changetoother, i, False))

            self.cvalue.append(QtWidgets.QLabel(self.gridLayoutWidget))
            self.cvalue[i].setText("Constant Value")
            self.gridLayout.addWidget(self.cvalue[i], i + self.vary, 4, 1, 1)
            self.cvalue[i].adjustSize()

            self.crfield.append(QtWidgets.QLineEdit(self.gridLayoutWidget))
            self.crfield[i].setText("const")
            self.gridLayout.addWidget(self.crfield[i], i + self.vary, 5, 1, 1)

        self.fname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fname.setText("File name: ")
        self.gridLayout.addWidget(self.fname, i + self.vary + 1, 0, 1, 1)

        self.filename = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.filename.setText("filename")
        self.gridLayout.addWidget(self.filename, i + self.vary + 1, 1, 1, 1)

        self.genBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.genBtn.setText("Generate")
        self.gridLayout.addWidget(self.genBtn, i + self.vary + 1, 4, 1, 1)
        self.genBtn.clicked.connect(lambda: self.generate_handler())

        for i in range(self.vary):
            self.pp[i].bind_to(self.update)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def generate_handler(self):
        # varying
        for i in range(self.vary):
            slist = self.pp[i].savesweep
            name = self.pp[i].savename
            list = self.pp[i].saverange
            check = self.checkrange(self.rfield[i].text(), i)
            if not check:
                return
            self.varyPara.append(varyPara.VaryPara(name, list, slist))

        # const
        for i in range(self.const):
            const = self.crfield[i].text()
            check = self.checknum(const, i, False)
            checkbound = self.checkboundary(const, i, False)
            if not (check and checkbound):
                return
            if self.ccombo[i].currentText() == "Other":
                name = self.cothername[i].text()
            else:
                name = self.ccombo[i].currentText()
            self.constPara.append(constPara.ConstPara(name, const))

        filename = self.filename.text()

        file = WriteFile.inputFile(filename, self.varyPara, self.constPara)

    def saverfield(self, i, text):
        self.pp[i].saverange[0] = text

    def savescheck(self, i, text):
        self.pp[i].savesweep[0] = text

    def savename(self, i, text):
        if self.combo[i].currentText() != "Other":
            self.combo[i].setCurrentText("Other")
        self.pp[i].savename = text
        self.pp[i].setname(text)
        print(self.pp[i].savename)

    def addSession(self, button_id):
        for btn in self.btn_grp.buttons():
            if btn is self.btn_grp.button(button_id):
                self.openwindow(self.pp[button_id])

    def changetoother(self, i, vary):
        if vary:
            if self.othername[i].text() != "":
                self.combo[i].setCurrentText("Other")
                self.pp[i].savename = self.othername[i].text()
            self.pp[i].setname(self.combo[i].currentText())
        else:
            if self.cothername[i].text() != "":
                self.ccombo[i].setCurrentText("Other")

    def openwindow(self, status):
        self.window = QtWidgets.QMainWindow()
        self.ui = add(status)
        self.ui.setupUi(self.window)
        self.window.show()

    def update(self):
        for i in range(self.vary):
            self.rfield[i].setText(self.pp[i].saverange[0])
            self.check[i].setChecked(self.pp[i].savesweep[0])

    def checkrange(self, text, i):
        try:
            numbers = text.split(",")
            num1 = numbers[0]
            num2 = numbers[1]
            check1 = self.checknum(num1, i, True)
            check2 = self.checknum(num2, i, True)
            check3 = numbers[2].isdigit()
            num3 = int(numbers[2])
            check4 = num3 >= 0
            checkbound1 = self.checkboundary(num1, i, True)
            checkbound2 = self.checkboundary(num2, i, True)
            if not (check1 and check2 and check3 and check4):
                self.popErrorWindow("Wrong input range format at " + str(i + 1) + "th vary item.")
            return check1 and check2 and check3 and checkbound1 and checkbound2
        except:
            self.popErrorWindow("Wrong input range format at " + str(i + 1) + "th vary item hh.")
            return False

    def checkboundary(self, num, index, vary):
        try:
            file1 = open("boundary.txt", "r+")
            text = file1.readlines()
            for i in range(len(text)):
                text[i] = text[i].replace('\n', '')
                x = re.split("<=|>=|<|>", text[i])
                y = re.findall("<=|>=|<|>", text[i])
                y = y[0]
                if vary:
                    name = self.pp[index].savename
                    if name == x[0]:
                        if y == ">":
                            if not float(num) > float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th vary item should > " + str(x[1]))
                                return False
                        if y == "<":
                            if not float(num) < float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th vary item should < " + str(x[1]))
                                return False
                        if y == ">=":
                            if not float(num) >= float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th vary item should >= " + str(x[1]))
                                return False
                        if y == "<=":
                            if not float(num) <= float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th vary item should <= " + str(x[1]))
                                return False
                else:
                    if self.ccombo[index].currentText() == "Other":
                        name = self.cothername[index].text()
                    else:
                        name = self.ccombo[index].currentText()
                    if name == x[0]:
                        if y == ">":
                            if not float(num) > float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th const item should > " + str(x[1]))
                                return False
                        if y == "<":
                            if not float(num) < float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th const item should < " + str(x[1]))
                                return False
                        if y == ">=":
                            if not float(num) >= float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th const item should >= " + str(x[1]))
                                return False
                        if y == "<=":
                            if not float(num) <= float(x[1]):
                                file1.close()
                                self.popErrorWindow(
                                    "Warning: Value at " + str(index + 1) + "th const item should <= " + str(x[1]))
                                return False
            file1.close()
            return True
        except:
            self.popErrorWindow("Fail to read boundary.txt")
            return False

    def checknum(self, text, i, vary):
        y = re.fullmatch("[0-9]*[.][0-9]*|[-][0-9]*[.][0-9]*|[0-9]*|[-][0-9]*", text)
        if y is None:
            if vary:
                self.popErrorWindow("Range must be integers/float at " + str(i + 1) + "th vary item.")
            if not vary:
                self.popErrorWindow("Constant value must be integers/float at " + str(i + 1) + "th const item.")
            return False
        return True

    def popErrorWindow(self, msg):
        self.window = QtWidgets.QMainWindow()
        self.ui = ErrorPane.error(msg)
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    setParameter = QtWidgets.QMainWindow()
    ui = parameter(3, 2)
    ui.setupUi(setParameter)
    setParameter.show()
    sys.exit(app.exec_())
