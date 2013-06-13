# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_helloplugin.ui'
#
# Created: Thu Jun 13 16:13:50 2013
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
        HelloPlugin.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(HelloPlugin)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(HelloPlugin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HelloPlugin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HelloPlugin.reject)
        QtCore.QMetaObject.connectSlotsByName(HelloPlugin)

    def retranslateUi(self, HelloPlugin):
        HelloPlugin.setWindowTitle(_translate("HelloPlugin", "HelloPlugin", None))

