# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_15 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 4, 1, 1, 1)
        self.pushButton_2 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_12 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 0, 1, 1)
        self.pushButton_11 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_9 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_17 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 5, 2, 1, 1)
        self.pushButton_16 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 4, 0, 1, 1)
        self.pushButton_13 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 2, 1, 1)
        self.pushButton_14 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 3, 1, 1)
        self.pushButton = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_7 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_6 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.pushButton_18 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 5, 3, 1, 1)
        self.pushButton_3 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_10 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 3, 1, 1)
        self.pushButton_5 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_8 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_20 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 5, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)
        self.pushButton_4 = CalculatorBtn(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.retranslateUi(Form)
        self.pushButton.key_pressed.connect(Form.get_key)
        self.pushButton_2.key_pressed.connect(Form.get_key)
        self.pushButton_3.key_pressed.connect(Form.get_key)
        self.pushButton_4.key_pressed.connect(Form.get_key)
        self.pushButton_8.key_pressed.connect(Form.get_key)
        self.pushButton_7.key_pressed.connect(Form.get_key)
        self.pushButton_5.key_pressed.connect(Form.get_key)
        self.pushButton_6.key_pressed.connect(Form.get_key)
        self.pushButton_12.key_pressed.connect(Form.get_key)
        self.pushButton_11.key_pressed.connect(Form.get_key)
        self.pushButton_9.key_pressed.connect(Form.get_key)
        self.pushButton_10.key_pressed.connect(Form.get_key)
        self.pushButton_16.key_pressed.connect(Form.get_key)
        self.pushButton_20.key_pressed.connect(Form.get_key)
        self.pushButton_15.key_pressed.connect(Form.get_key)
        self.pushButton_13.key_pressed.connect(Form.get_key)
        self.pushButton_17.key_pressed.connect(Form.get_key)
        self.pushButton_14.key_pressed.connect(Form.get_key)
        self.pushButton_18.key_pressed.connect(Form.get_key)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_15.setText(_translate("Form", "2"))
        self.pushButton_15.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_15.setProperty("role", _translate("Form", "num"))
        self.pushButton_2.setText(_translate("Form", "+/-"))
        self.pushButton_2.setProperty("bg", _translate("Form", "lightgray"))
        self.pushButton_2.setProperty("role", _translate("Form", "num"))
        self.pushButton_12.setText(_translate("Form", "4"))
        self.pushButton_12.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_12.setProperty("role", _translate("Form", "num"))
        self.pushButton_11.setText(_translate("Form", "5"))
        self.pushButton_11.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_11.setProperty("role", _translate("Form", "num"))
        self.pushButton_9.setText(_translate("Form", "6"))
        self.pushButton_9.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_9.setProperty("role", _translate("Form", "num"))
        self.pushButton_17.setText(_translate("Form", "."))
        self.pushButton_17.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_17.setProperty("role", _translate("Form", "num"))
        self.pushButton_16.setText(_translate("Form", "1"))
        self.pushButton_16.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_16.setProperty("role", _translate("Form", "num"))
        self.pushButton_13.setText(_translate("Form", "3"))
        self.pushButton_13.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_13.setProperty("role", _translate("Form", "num"))
        self.pushButton_14.setText(_translate("Form", "+"))
        self.pushButton_14.setProperty("bg", _translate("Form", "orange"))
        self.pushButton_14.setProperty("role", _translate("Form", "operator"))
        self.pushButton.setText(_translate("Form", "AC"))
        self.pushButton.setProperty("bg", _translate("Form", "lightgray"))
        self.pushButton.setProperty("role", _translate("Form", "clear"))
        self.pushButton_7.setText(_translate("Form", "8"))
        self.pushButton_7.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_7.setProperty("role", _translate("Form", "num"))
        self.pushButton_6.setText(_translate("Form", "*"))
        self.pushButton_6.setProperty("bg", _translate("Form", "orange"))
        self.pushButton_6.setProperty("role", _translate("Form", "operator"))
        self.pushButton_18.setText(_translate("Form", "="))
        self.pushButton_18.setProperty("bg", _translate("Form", "equal"))
        self.pushButton_18.setProperty("role", _translate("Form", "calculator"))
        self.pushButton_3.setText(_translate("Form", "%"))
        self.pushButton_3.setProperty("bg", _translate("Form", "lightgray"))
        self.pushButton_3.setProperty("role", _translate("Form", "num"))
        self.pushButton_10.setText(_translate("Form", "-"))
        self.pushButton_10.setProperty("bg", _translate("Form", "orange"))
        self.pushButton_10.setProperty("role", _translate("Form", "operator"))
        self.pushButton_5.setText(_translate("Form", "9"))
        self.pushButton_5.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_5.setProperty("role", _translate("Form", "num"))
        self.pushButton_8.setText(_translate("Form", "7"))
        self.pushButton_8.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_8.setProperty("role", _translate("Form", "num"))
        self.pushButton_20.setText(_translate("Form", "0"))
        self.pushButton_20.setProperty("bg", _translate("Form", "gray"))
        self.pushButton_20.setProperty("role", _translate("Form", "num"))
        self.lineEdit.setText(_translate("Form", "0.0"))
        self.lineEdit.setProperty("bg", _translate("Form", "orange"))
        self.pushButton_4.setText(_translate("Form", "/"))
        self.pushButton_4.setProperty("bg", _translate("Form", "orange"))
        self.pushButton_4.setProperty("role", _translate("Form", "operator"))
from Pyqt5_demo.Calculator_Btn import CalculatorBtn
