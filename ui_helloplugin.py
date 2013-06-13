# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_helloplugin.ui'
#
# Created: Thu Jun 13 17:23:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HelloPlugin(object):
    def setupUi(self, HelloPlugin):
        HelloPlugin.setObjectName(_fromUtf8("HelloPlugin"))
        HelloPlugin.resize(400, 266)
        HelloPlugin.setAcceptDrops(False)
        self.formLayout = QtGui.QFormLayout(HelloPlugin)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.enterNameLabel = QtGui.QLabel(HelloPlugin)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.enterNameLabel.setFont(font)
        self.enterNameLabel.setObjectName(_fromUtf8("enterNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.enterNameLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nameLineEdit = QtGui.QLineEdit(HelloPlugin)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.OKPushButton = QtGui.QPushButton(HelloPlugin)
        self.OKPushButton.setObjectName(_fromUtf8("OKPushButton"))
        self.horizontalLayout.addWidget(self.OKPushButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.outputPlainTextEdit = QtGui.QPlainTextEdit(HelloPlugin)
        self.outputPlainTextEdit.setObjectName(_fromUtf8("outputPlainTextEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.outputPlainTextEdit)

        self.retranslateUi(HelloPlugin)
        QtCore.QMetaObject.connectSlotsByName(HelloPlugin)

    def retranslateUi(self, HelloPlugin):
        HelloPlugin.setWindowTitle(_translate("HelloPlugin", "Hello Plugin", None))
        self.enterNameLabel.setText(_translate("HelloPlugin", "Enter you name:", None))
        self.OKPushButton.setText(_translate("HelloPlugin", "OK", None))

