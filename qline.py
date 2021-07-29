# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(804, 404)
        self.log_te = QtWidgets.QPlainTextEdit(main)
        self.log_te.setGeometry(QtCore.QRect(380, 150, 331, 191))
        self.log_te.setObjectName("log_te")
        self.clean_pb = QtWidgets.QPushButton(main)
        self.clean_pb.setGeometry(QtCore.QRect(630, 130, 80, 21))
        self.clean_pb.setObjectName("clean_pb")
        self.widget = QtWidgets.QWidget(main)
        self.widget.setGeometry(QtCore.QRect(9, 9, 369, 333))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ip_lb = QtWidgets.QLabel(self.widget)
        self.ip_lb.setObjectName("ip_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ip_lb)
        self.ip_le = QtWidgets.QLineEdit(self.widget)
        self.ip_le.setMaximumSize(QtCore.QSize(16777215, 110))
        self.ip_le.setObjectName("ip_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ip_le)
        self.connect_pb = QtWidgets.QPushButton(self.widget)
        self.connect_pb.setMaximumSize(QtCore.QSize(250, 20))
        self.connect_pb.setObjectName("connect_pb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.connect_pb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.id_lb = QtWidgets.QLabel(self.widget)
        self.id_lb.setObjectName("id_lb")
        self.gridLayout.addWidget(self.id_lb, 0, 0, 1, 1)
        self.fnct_lb = QtWidgets.QLabel(self.widget)
        self.fnct_lb.setObjectName("fnct_lb")
        self.gridLayout.addWidget(self.fnct_lb, 0, 1, 1, 1)
        self.adr_lb = QtWidgets.QLabel(self.widget)
        self.adr_lb.setObjectName("adr_lb")
        self.gridLayout.addWidget(self.adr_lb, 0, 2, 1, 1)
        self.cnt_lb = QtWidgets.QLabel(self.widget)
        self.cnt_lb.setObjectName("cnt_lb")
        self.gridLayout.addWidget(self.cnt_lb, 0, 3, 1, 1)
        self.id_sb = QtWidgets.QSpinBox(self.widget)
        self.id_sb.setObjectName("id_sb")
        self.gridLayout.addWidget(self.id_sb, 1, 0, 1, 1)
        self.funct_cb = QtWidgets.QComboBox(self.widget)
        self.funct_cb.setObjectName("funct_cb")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.funct_cb.addItem("")
        self.gridLayout.addWidget(self.funct_cb, 1, 1, 1, 1)
        self.adr_sb = QtWidgets.QSpinBox(self.widget)
        self.adr_sb.setObjectName("adr_sb")
        self.gridLayout.addWidget(self.adr_sb, 1, 2, 1, 1)
        self.cnt_sb = QtWidgets.QSpinBox(self.widget)
        self.cnt_sb.setObjectName("cnt_sb")
        self.gridLayout.addWidget(self.cnt_sb, 1, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.send_pb = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_pb.sizePolicy().hasHeightForWidth())
        self.send_pb.setSizePolicy(sizePolicy)
        self.send_pb.setObjectName("send_pb")
        self.horizontalLayout.addWidget(self.send_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cycle_sending_cb = QtWidgets.QCheckBox(self.widget)
        self.cycle_sending_cb.setObjectName("cycle_sending_cb")
        self.horizontalLayout_2.addWidget(self.cycle_sending_cb)
        self.timeout_sb = QtWidgets.QSpinBox(self.widget)
        self.timeout_sb.setMaximum(10000)
        self.timeout_sb.setProperty("value", 100)
        self.timeout_sb.setObjectName("timeout_sb")
        self.horizontalLayout_2.addWidget(self.timeout_sb)
        self.timeout_lb = QtWidgets.QLabel(self.widget)
        self.timeout_lb.setObjectName("timeout_lb")
        self.horizontalLayout_2.addWidget(self.timeout_lb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.data_tw = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_tw.sizePolicy().hasHeightForWidth())
        self.data_tw.setSizePolicy(sizePolicy)
        self.data_tw.setMinimumSize(QtCore.QSize(309, 192))
        self.data_tw.setMouseTracking(False)
        self.data_tw.setTabletTracking(False)
        self.data_tw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_tw.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.data_tw.setObjectName("data_tw")
        self.data_tw.setColumnCount(3)
        self.data_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_tw.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.data_tw)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "modbus TCP client"))
        self.clean_pb.setText(_translate("main", "Clean"))
        self.ip_lb.setText(_translate("main", "IP"))
        self.connect_pb.setText(_translate("main", "connect"))
        self.id_lb.setText(_translate("main", "slave id"))
        self.fnct_lb.setText(_translate("main", "Function"))
        self.adr_lb.setText(_translate("main", "Address"))
        self.cnt_lb.setText(_translate("main", "Count"))
        self.funct_cb.setItemText(0, _translate("main", "Read Coil"))
        self.funct_cb.setItemText(1, _translate("main", "Read Discret input"))
        self.funct_cb.setItemText(2, _translate("main", "Read HR"))
        self.funct_cb.setItemText(3, _translate("main", "Read IR"))
        self.funct_cb.setItemText(4, _translate("main", "Write Multiple Coil"))
        self.funct_cb.setItemText(5, _translate("main", "Write Multiple Registers"))
        self.funct_cb.setItemText(6, _translate("main", "Write Single Coil"))
        self.funct_cb.setItemText(7, _translate("main", "Write Single Register"))
        self.send_pb.setText(_translate("main", "send"))
        self.cycle_sending_cb.setText(_translate("main", "Cyclic send"))
        self.timeout_lb.setText(_translate("main", "ms"))
        item = self.data_tw.horizontalHeaderItem(0)
        item.setText(_translate("main", "Data type"))
        item = self.data_tw.horizontalHeaderItem(1)
        item.setText(_translate("main", "Address"))
        item = self.data_tw.horizontalHeaderItem(2)
        item.setText(_translate("main", "Value"))
